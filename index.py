import socket
from time import sleep
from requests import get

rangeExpected = 73
errorSleep = 5

def getCurrentRangeIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        localIP = s.getsockname()[0]
        rangeIP = localIP.split('.')[2]
        return rangeIP
    except:
        return ''

def getPublicIP():
    ip = get('https://api.ipify.org').text
    return ip

def main():
    while True:
        rangeActual = getCurrentRangeIP()
        print(rangeActual)
        if rangeActual == '': # Quando o pc não receber IP via DHCP
            sleep(errorSleep)
            continue

        elif rangeActual != rangeExpected:
            ipPublic = getPublicIP()
            break
        else:
            print('Success')

main()