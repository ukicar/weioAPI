"""
    geoipy.py
    A simple IP geolocation python script.
    Uses geody.com geolocation web service.
    Requires BeautifulSoup library.

    ksaver, June 18, 2011.
    Public Domain Code.
"""

import re
import sys
from urllib import urlopen
from BeautifulSoup import BeautifulSoup as Soup
#TODO some global import for all weio functions
from weio_system_network import myExternalIp

def whereIam() :
    """Where I am function tries to geolocate WEIO board"""

    ipAddress = myExternalIp()
    geody = "http://www.geody.com/geoip.php?ip=" + ipAddress
    html_page = urlopen(geody).read()
    soup = Soup(html_page)

    # Filter paragraph containing geolocation info.
    paragraph = soup('p')[3]

    # Remove html tags using regex.
    geo_txt = re.sub(r'<.*?>', '', str(paragraph))
    return geo_txt[32:].strip()
    