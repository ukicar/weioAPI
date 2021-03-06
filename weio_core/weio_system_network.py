import re
import urllib

import ping, socket

from subprocess import check_output

interface = "wlan0"
 
def listAvailableWifiSpots() :
    """List available wifi spots will return list of wifi objects."""
    print("not yet implemented")

def connectToWifiSpot(wifiObject, password) :
    """Connect to wifi spot will connect to specified wifi network"""
    print("not yet implemented")

def createAP(ssid, password) :
    """This function creates Access Point network of specified ssid name and password. If password is omitted than network will be free to access"""
    print("not yet implemented")

def isConnected() :
    """Is connected checks if WEIO is connected to the wifi. Function returns : 1 - connected, 0 - not connected"""
    try :
       output = check_output(["iwinfo", interface, "assoclist"])
       #print output
       if "No station connected" in output :
           return 0
           #print "wifi is UP but not connected"
       else :
           return 1
           print "wifi is UP and connected!"
    except :
        return 0
        #print "wifi is DOWN"
    

def myIp() :
    """My Ip returns current ip address of WEIO device on wlan01 interface"""
    return [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]

def defineMyIpAddress(address) :
    """Define my Ip address function defines specified Ip address for wlan01 interfac"""
    print("not yet implemented")

def discoverOtherWeios() :
    print("not yet implemented")

def ping(ip) :   
     print("not yet implemented")

def myExternalIp():
    """My external Ip returns current Ip address accessible from Internet by pinging external server and returning Ip address"""
    #TODO : try except this call
    f = urllib.urlopen("http://www.canyouseeme.org/")
    html_doc = f.read()
    f.close()
    ipaddr = re.search('(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)',html_doc)
    return str(ipaddr.group(0))
