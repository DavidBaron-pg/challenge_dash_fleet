# -*- coding: utf-8 -*-
"""
@author: DavidBaron
"""

# importing the requests library
import requests
import base64

def str2base64(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message      


# Function to send the request to endpoint using gps_data
def send_request_gps_data(gps_data):    

    base64_message = str2base64(str(gps_data))
      
    #Send the get request with encoded message
    URL = "https://api.aipass.io/API/v1/test/challenge?data={}".format(base64_message)
    r = requests.get(url = URL)
      
    # extracting data in json format
    status = r.status_code
    
    return status

