from netvars import initNet, getNetVar, setNetVar

ssid = ""
password = ""

initNet(ssid, password)

winner = getNetVar("csgo-major-winner-prediction")
print('winner:', winner)

setNetVar("csgo-major-winner-prediction", "vitality")
myWinner = getNetVar("csgo-major-winner-prediction")
print('myWinner:', myWinner)
