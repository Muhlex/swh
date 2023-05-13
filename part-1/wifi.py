import network

ssid = ""
password = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
	print('Connecting to WiFi network...')
	wlan.connect(ssid, password)
	while not wlan.isconnected():
		pass

print('Network config:', wlan.ifconfig())
