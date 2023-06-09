from machine import Pin, time_pulse_us
from time import sleep_ms, sleep_us, ticks_ms, ticks_diff
from netvars import initNet, getNetVar, setNetVar

ssid = ""
password = ""
writeKey = "task-18-vj13s2"
readKey = "task-18-vj13s2"
REPORT_MIN_DISTANCE_CHANGE_CM = 3.0 # how far our distance has to change to be reported to the server
REMOTE_MIN_DISTANCE_CHANGE_COUNT = 2 # how many remote changes must at least be remembered to light the LED
REMOTE_MAX_DISTANCE_CHANGE_AGE = 10 # max age in secs after which remote distance changes are forgotten

def getNetVarFloat(key: str):
	result = getNetVar(key)
	if result == 'NO':
		return 0.0
	else:
		return float(result)

class DistanceSensor:
	def __init__(self, triggerPinID: int | str, echoPinID: int | str, echoTimeoutUS=500*2*30):
		self.echoTimeoutUS = echoTimeoutUS
		self.trigger = Pin(triggerPinID, Pin.OUT)
		self.trigger.value(0)
		self.echo = Pin(echoPinID, Pin.IN)

	def _sendPulse(self):
		self.trigger.value(0)
		sleep_us(5)
		self.trigger.value(1)
		sleep_us(10)
		self.trigger.value(0)
		try:
			pulseTime = time_pulse_us(self.echo, 1, self.echoTimeoutUS)
			if pulseTime < 0:
				MAX_RANGE_IN_CM = 500
				pulseTime = int(MAX_RANGE_IN_CM * 29.1) # 1cm each 29.1us
			return pulseTime
		except OSError as ex:
			if ex.args[0] == 110: # 110 = ETIMEDOUT
				raise OSError('Out of range')
			raise ex

	def measureMM(self):
		pulseTime = self._sendPulse()
		mm = pulseTime * 100 // 582
		return mm

	def measureCM(self):
		pulseTime = self._sendPulse()
		cms = (pulseTime / 2) / 29.1
		return cms

sensor = DistanceSensor(15, 13)
led = Pin(12, Pin.OUT)

lastReportedDistance = -1

lastRemoteDistance = -1
remoteChangeTicks = []

try:
	initNet(ssid, password)
	lastReportedDistance = sensor.measureCM()
	lastRemoteDistance = getNetVarFloat(readKey)

	while True:
		sleep_ms(2000)

		# Read their value
		remoteDistance = getNetVarFloat(readKey)
		remoteDelta = remoteDistance - lastRemoteDistance
		currentTick = ticks_ms()
		remoteChangeTicks = list(filter(lambda tick: ticks_diff(currentTick, tick) < REMOTE_MAX_DISTANCE_CHANGE_AGE * 1000, remoteChangeTicks))
		if remoteDistance != lastRemoteDistance:
			remoteChangeTicks.append(currentTick)
		lastRemoteDistance = remoteDistance

		# Update LED to their value
		print(f'Their changes: {len(remoteChangeTicks)}/{REMOTE_MIN_DISTANCE_CHANGE_COUNT} in the last {REMOTE_MAX_DISTANCE_CHANGE_AGE} seconds.')
		if len(remoteChangeTicks) >= REMOTE_MIN_DISTANCE_CHANGE_COUNT:
			led.on()
		else:
			led.off()

		# Update our value
		distance = sensor.measureCM()
		delta = distance - lastReportedDistance

		if abs(delta) > 1.0:
			setNetVar(writeKey, distance)
			print('Updated our distance on server:', distance)
			lastReportedDistance = distance


except KeyboardInterrupt:
	print('Exited.')

finally:
	led.off()
