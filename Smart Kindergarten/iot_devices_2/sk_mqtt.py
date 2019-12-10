'''
    mqtt module
'''
import paho.mqtt.client as mqtt
import sk_gpio
import time

_MQTT_CloudServer="mqtt.eclipse.org"

# mqtt init func
def init():
    print("Initialized Mqtt\n")
    print("Mqtt Host IP: ",_MQTT_CloudServer) 
    mqtt_iot_devices=mqtt.Client("python_pub")
    mqtt_iot_devices.connect(_MQTT_CloudServer, 1883)
    startPublish(mqtt_iot_devices)

def startPublish(mqtt_iot_devices):
    print("startPublish Func Called")

    # Publish sensor data
    while(True):
        time.sleep(1)
        print(sk_gpio.getTempHumidity())
        print(sk_gpio.getUltra())        
        mqtt_iot_devices.publish("korea/sk/temp", sk_gpio.getTempHumidity())
        mqtt_iot_devices.publish("korea/sk/temp", sk_gpio.getUltra())
