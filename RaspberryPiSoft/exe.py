#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqttClient
import serial
import time

x=""
y=""
z=""

def on_connect(client, userdata, flags, rc):
    print('connected (%s)' % client._client_id)
    client.subscribe(topic='Test', qos=2)

ser = serial.Serial(
port='/dev/ttyACM0',\
baudrate=115200,\
parity=serial.PARITY_NONE,\
stopbits=serial.STOPBITS_ONE,\
bytesize=serial.EIGHTBITS,\
timeout=0)
client = mqttClient.Client(client_id='Raspberry', clean_session=False)
client.on_connect = on_connect
client.connect(host='172.20.10.3', port=1883)
client.loop_start()
client.publish("Data","RPi Connected")
try:
    while True:
        line = ser.readline()
        subline = line.decode()
        if (subline[:2] == "x:"):
            x=subline[0:len(subline)-2]
            client.publish("Data",x)
        elif (subline[:2] == "y:"):
            y=subline[0:len(subline)-2]
            client.publish("Data",y)
        elif (subline[:2] == "z:" and x != "" and y != ""):
            z=subline[0:len(subline)-2]
            client.publish("Data",z)
        time.sleep((0.01)/3)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()




