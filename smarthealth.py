import time #to have some delays
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "wmwxfz"
deviceType = "raspberrypi"
deviceId = "1234"
authMethod = "token" #authmethod should only be token
authToken = "12345678"


try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken} #in jason data format
        deviceCli = ibmiotf.device.Client(deviceOptions)#command used to make a client with device credentials for connecting to platform
        #.............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times

deviceCli.connect()#connection is made to platform

while True:
        
        pulse=random.randint(10,40)
        #print(pulse)
        temp = random.randint(10,40)
        #Send Temperature & Humidity to IBM Watson
        data = { 'Temperature' : temp, 'Pulse_Rate': pulse }
        #print (data)
        def myOnPublishCallback():
            print ("Published Temperature = %s C" % temp, "Pulse Rate = %s %%" % pulse, "to IBM Watson")

        success = deviceCli.publishEvent("DHT11", "json", data, qos=0, on_publish=myOnPublishCallback) #used to publish events in the iot platfoem
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)

       
# Disconnect the device and application from the cloud
deviceCli.disconnect()

