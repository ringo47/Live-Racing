import paho.mqtt.client as mqtt , os, urlparse
import time

import RPi.GPIO as GPIO

user=""
password=""


GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setwarnings(False)

fPin = 18
bPin = 23
lPin = 17
rPin = 27

GPIO.setup(fPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)
GPIO.setup(lPin, GPIO.OUT)
GPIO.setup(rPin, GPIO.OUT)

"""GPIO.output(lPin, 1)
time.sleep(1)
GPIO.output(lPin, 0)
time.sleep(1)"""
client = mqtt.Client()


# Define event callbacks
    
def on_connect(mosq, obj, rc):
    print ("on_connect:: Connected with result code "+ str ( rc ) )
    print("rc: " + str(rc))
    
    client.subscribe ("/frommothership" ,0 )

def on_message(mosq, obj, msg):
    #print ("on_message:: this means  I got a message from brokerfor this topic")
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if(len(msg.payload)!=4):
        return
    if ( msg.payload[0] == "1" ):
    	print "forward"
    	GPIO.output(fPin, 1)
    else:
        GPIO.output(fPin, 0)
        
    if ( msg.payload[1] == "1" ):
    	print "forward"
    	GPIO.output(bPin, 1)
    else:
        GPIO.output(bPin, 0)

    if ( msg.payload[2] == "1" ):
    	print "forward"
    	GPIO.output(lPin, 1)
    else:
        GPIO.output(lPin, 0)

    if ( msg.payload[3] == "1" ):
    	print "forward"
    	GPIO.output(rPin, 1)
    else:
        GPIO.output(rPin, 0)
 		

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("This means broker has acknowledged my subscribe request")
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)



# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

# Uncomment to enable debug messages
client.on_log = on_log


# user name has to be called before connect - my notes.
client.username_pw_set(user, password)

client.connect('m12.cloudmqtt.com', 10538, 60)

# Continue the network loop, exit when an error occurs
#rc = 0
#while rc == 0:
#    rc = client.loop()
#print("rc: " + str(rc))

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_forever()





    
client.loop_forever()



