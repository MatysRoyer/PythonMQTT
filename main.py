# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import RPi.GPIO as GPIO
import dht11
import paho.mqtt.client as mqtt

broker = '10.4.1.42'
client = mqtt.Client("Matys")


def on_connect(clientTest, userdata, flags, rc):
    print("I am connected " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe("SMILE")
client.loop_forever()
