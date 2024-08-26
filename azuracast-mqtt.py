#!/usr/bin/env python

#################################################################################

# Azuracast To MQTT
# Developed by: Jeff Lehman, N8ACL
# Current Version: 1.0
# https://github.com/n8acl/azuracast_to_mqtt

# Questions? Comments? Suggestions? Contact me one of the following ways:
# E-mail: n8acl@qsl.net
# Discord: Ravendos
# Mastodon: @n8acl@mastodon.radio
# Website: https://www.qsl.net/n8acl

###################   DO NOT CHANGE BELOW   #########################

# Import Libraries
import json
import paho.mqtt.publish as publish
import requests
from time import sleep

#############################
# import config json file

with open("config.json", "r") as read_file:
    config = json.load(read_file)

#############################
# Set variables

mqtt_broker = config["mqtt_broker"]
mqtt_port = config["mqtt_port"]
base_topic = config["mqtt_topic_prefix"]
azuracast_status_url = config["azuracast_status_url"]

#############################
# Define Functions
def get_api_data(url):
    # get JSON data from api's with just a URL
    return requests.get(url=url).json()

#############################
# Main Driver

while True:

    status_json = get_api_data(azuracast_status_url)

    for x in range(0,len(status_json)):
        station_name = (status_json[x]['station']['shortcode']).lower()
        topic = base_topic + station_name + '/nowplaying'
        message = status_json[x]['now_playing']['song']['text']
        publish.single(topic,message,hostname=mqtt_broker,port=1883)
        # print(topic)
    sleep(15)