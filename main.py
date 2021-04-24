# -*- coding: utf-8 -*-
"""
@author: DavidBaron
"""
#Import libraries
import extract_data_from_nmea as extract_dfn
import load_data_to_sql as load_d2s
import send_request_endpoint as send_rgd
import create_log_file as create_lf
import sqlite3
import os

line = '$GPGGA,13506.000,1114.3351,N,07412.7416,W,1,12,0.77,17.8,M,-7.6,M,,*52'
data = line.split(',')
id_data = data[0][-3:]

#Extract data from gps
gps_data = extract_dfn.detect_message(line)
print('Data from gps extracted...')

#Create a connection betwwen python and sqlite
db_path = os.getcwd().replace('\\','/') +  '/sqlite/databases/dashfleet/'
db_name = 'dashfleet.db'
conn = sqlite3.connect(db_path + db_name)

#Create table and insert gps data
load_d2s.insert_data(conn, gps_data)
print('Data inserted in sqlite table...')

#Get status code from send request
status = send_rgd.send_request_gps_data(gps_data)
print('Request sended to endpoint and status extracted...')

#Generate log file
create_lf.generate_log(status, line)
print('Log file generated...')
