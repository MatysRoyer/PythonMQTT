# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import RPi.GPIO as GPIO
import dht11
import paho.mqtt.client as mqtt

broker = '10.4.1.42'
client = mqtt.Client("Matys", clean_session=False)


def on_connect(client, userdata, flags, rc):
    print("I am connected " + str(rc) + str(flags))
    client.subscribe("SMILE", qos=2)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883)
client.loop_forever()
