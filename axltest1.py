import requests
import urllib3
urllib3.disable_warnings()

axlhost = '10.10.210.10'
axlusername = 'axl'
axlpassword = 'cisco'
axlversion = '11.5'

import xml.etree.ElementTree as ET

soaprequest = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/' + axlversion + '">' \
'<soapenv:Header />' \
'<soapenv:Body> \ ' \
'<ns:listPhone> ' \
'<searchCriteria>' \
'<name>SEP%</name>' \
'</searchCriteria>' \
'<returnedTags>' \
'<name></name>' \
'</returnedTags> /' \
'</ns:listPhone>' \
'</soapenv:Body>' \
'</soapenv:Envelope>'

soapheaders = {'Content-type': 'text/xml', 'SOAPAction': 'CUCM:DB ver=' + axlversion + ' listPhone'}

AXLRequest = requests.post('https://' + axlhost + ':8443/axl/', data=soaprequest, headers=soapheaders, verify=False,
                           auth=(axlusername, axlpassword))

root = ET.fromstring(AXLRequest.text)

DeviceNames = []

for phone in root.iter('phone'): #This will iterate through the phone element in root
    #DeviceNames.append(phone.find('name').text) # This appends each element to a python list

    print (phone.find('name').text)


    #print DeviceNames