import network

def initNet(ssid, passwd):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, passwd)
        while not wlan.isconnected():

            pass
    print('network config:', wlan.ifconfig())

def http_get(url):
    #print(url)
    #print("............")
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    retStr =""
    while True:
        data = s.recv(500)
        if data:
            # this would be all
            # retStr = retStr +str(data, 'utf8') 
            # Only the last line
            retStr = str(data, 'utf8') 
            #print(str(data, 'utf8'), end='')
        else:
            break
    s.close()
    return retStr


def setNetVar(varName, varVal):
    urlStr = "https://ubicomp.net/sw/db1/var2db.php?varName=" + str(varName) + "&varValue=" + str(varVal)
    # print(urlStr)
    # http_get("https://ubicomp.net/sw/db1/var2db.php?varName=test3&varValue=14")
    # http_get("https://ubicomp.net/sw/db1/var2db.php?varName=test222&varValue=valTest222")
    http_get(urlStr)


def getNetVar(varName):
    urlStr = "https://ubicomp.net/sw/db1/var2db.php?varName=" + str(varName) 
    # print(urlStr)
    # http_get("https://ubicomp.net/sw/db1/var2db.php?varName=test3&varValue=14")
    # http_get("https://ubicomp.net/sw/db1/var2db.php?varName=test222&varValue=valTest222")
    resStr = http_get(urlStr)
    # import re # standrad python
    import ure
    #_, retVar0 = ure.split('\r\n\r\n|\n\n',resStr)
    # retVar = ure.split(' |\n|\r',retVar0)
    reg1 = ure.compile('\r\n\r\n|\n\n')
    reg2 = ure.compile(' |\n|\r')
    _, retVar0 = reg1.split(resStr)
    retVar = reg2.split(retVar0)
    return retVar[0]

#Example usage
# from netvars import setNetVar, getNetVar, http_get, initNet
# # assuming there is a network with ssid hotspot1 and password 123456789
# initNet("hotspot1", "123456789")
# setNetVar("test222", "valTest222")
# a=getNetVar("test222")
# print(a) # will print valTest222






