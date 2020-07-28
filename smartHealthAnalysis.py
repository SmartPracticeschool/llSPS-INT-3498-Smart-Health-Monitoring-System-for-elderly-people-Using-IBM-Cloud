#try to use jupyter notebook while executing the program wait for atleast 40 seconds for the entire program to run

import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
#Provide your IBM Watson Device Credentials
organization = "ytissp"
deviceType = "raspberrypi"
deviceId = "12345678"
authMethod = "token"
authToken = "12345678"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect() #try with different values

while True:
        temp=round(random.uniform(96,102),1)   # print temperature
        pul=random.randint(10,180)   # print pulse
        #enter your mobile number
        if (temp <= 97) or (temp >=100):
            r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=sDNoOkViHbSXQAxwBU0q753IPKdJ6L4mYatgCFZy8fElnWGR1hPZK2UbvViosYwWEA0B9haIOLGjx4X3&sender_id=FSTSMS&message=ABNORMAL TEMPERATURE DETECTED&language=english&route=p&numbers=7893836463')
        if (pul <= 50) or (pul >= 110):
            r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=sDNoOkViHbSXQAxwBU0q753IPKdJ6L4mYatgCFZy8fElnWGR1hPZK2UbvViosYwWEA0B9haIOLGjx4X3&sender_id=FSTSMS&message=ABNORMAL PULSE DETECTED&language=english&route=p&numbers=7893836463')
        data = { 'temp': temp , 'pul':pul}
        #print (data)
        def myOnPublishCallback():
            print ("Published  temp = %s " % temp,"pul = %s" % pul,"to IBM Watson")

        success = deviceCli.publishEvent("kitchen", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(10)
        
        deviceCli.commandCallback = myCommandCallback


# Disconnect the device and application from the cloud
deviceCli.disconnect()
