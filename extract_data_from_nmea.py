# -*- coding: utf-8 -*-
"""
David Baron
"""

import time

def readGGA(data):
    timestamp_unix = int(time.time())
    latitude = data[2]
    longitude = data[4]
    speed = 'NULL'
    heading = 'NULL'
    json_data = {'timestamp_unix' : timestamp_unix,\
                 'latitude': latitude,\
                 'longitude': longitude, \
                 'speed':speed,\
                 'heading' : heading}
    return json_data

def readGLL(data):
    timestamp_unix = int(time.time())
    latitude = data[1]
    longitude = data[3]
    speed = 'NULL'
    heading = 'NULL'
    json_data = {'timestamp_unix' : timestamp_unix,\
                 'latitude': latitude,\
                 'longitude': longitude, \
                 'speed':speed,\
                 'heading' : heading}
    return json_data

def readRMC(data):
    timestamp_unix = int(time.time())
    latitude = data[3]
    longitude = data[5]
    speed = float(data[7])
    heading = 'NULL'
    json_data = {'timestamp_unix' : timestamp_unix,\
                 'latitude': latitude,\
                 'longitude': longitude, \
                 'speed':speed,\
                 'heading' : heading}
    return json_data

def readVTG(data):
    timestamp_unix = int(time.time())
    latitude = 'NULL'
    longitude = 'NULL'
    speed = float(data[7])
    heading = int(data[3])
    json_data = {'timestamp_unix' : timestamp_unix,\
                 'latitude': latitude,\
                 'longitude': longitude, \
                 'speed':speed,\
                 'heading' : heading}
    return json_data

def detect_message(line):
    data = line.split(',')
    id_data = data[0][-3:]
    if id_data == 'GGA':
        gps_data = readGGA(data)
    elif id_data == 'GLL':
        gps_data = readGLL(data)
    elif id_data == 'RMC':
        gps_data = readRMC(data)
    elif id_data == 'VTG':
        gps_data = readVTG(data)
    return gps_data