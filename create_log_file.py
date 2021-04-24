# -*- coding: utf-8 -*-
"""
@author: DavidBaron
"""
import datetime as dt
import os


def generate_log(status, line):
    log_file_path = os.getcwd().replace('\\','/') + '/var/log/challenge.log'
    today = dt.datetime.now()
    
    with open(log_file_path, 'a+') as file:
       
        log_date = str(today.year) + '-' + str(today.month).zfill(2) + '-' + str(today.day).zfill(2) + '_' + \
                   str(today.hour).zfill(2) + ':' + str(today.minute).zfill(2) + ':' + str(today.second).zfill(2)
        log = log_date + '-' + line + '-' + str(status) + '\n'
        
        file.writelines(log)
        file.close()
