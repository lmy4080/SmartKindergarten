'''
    mqtt module
'''

import paho.mqtt.client as mqtt
import sk_gpio

_TOKEN="koreauniv/comdp/1/smart-kindergarten"
_MQTT_CloudServer="mqtt.eclipse.org"

# callback func, when connected
def on_connect(client, userdata, flags, rc):
    print("Connected with result code:", str(rc))
    client.subscribe(_TOKEN)
    print("Subscribed token value::", _TOKEN)    

# callback func, when messages received
def on_message(client, userdata, msg):
    
    # bytes to utf8
    msg.payload = msg.payload.decode("utf-8")
    print("\n", msg.topic, "", str(msg.payload))

    # msg.payload -> LED, controls :LED sensor
    # msg.payload -> MOTOR, controls :MOTOR sensor
    _msgs=str(msg.payload).split('/')
    if _msgs[0] == "LED":
        flag=True if _msgs[1]=="1" else False

        sk_gpio.OperateLedSensor(flag)

    if _msgs[0] == "MOTOR":
        flag=True if _msgs[1]=="1" else False

        sk_gpio.OperateMotorSensor(flag)

# mqtt init func
def init():
    print("Initialized Mqtt\n")
    print("Mqtt Host IP: ",_MQTT_CloudServer) 
    client=mqtt.Client()
    client.on_connect=on_connect
    client.on_message=on_message

    client.connect(_MQTT_CloudServer, 1883, 60)
    client.loop_forever()
