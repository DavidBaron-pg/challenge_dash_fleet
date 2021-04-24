# -*- coding: utf-8 -*-
"""
@author: DavidBaron
"""

def create_table(conn):

    #Create the cursos to send and receive data
    c = conn.cursor()
    
    #Query to create the table to insert data
    query_create_table = """
    CREATE TABLE IF NOT EXISTS nmea_gps_data (
    TIMESTAMP_UNIX INTEGER,
    LATITUDE STRING,
    LONGITUDE STRING,
    SPEED FLOAT,
    HEADING INTEGER
    );
    """
    
    #Execute query to create table
    c.execute(query_create_table)
    
    #Save changes in database
    conn.commit()

def insert_data(conn, gps_data):
    
    #Execute query to create table in database
    create_table(conn)
    
    #Create the cursos to send and receive data
    c = conn.cursor()
    
    #Query to create the table to insert data
    query_insert_data_table = """
    INSERT INTO nmea_gps_data (
    TIMESTAMP_UNIX,
    LATITUDE,
    LONGITUDE,
    SPEED,
    HEADING
    )
    VALUES ({},{},{},{},{});
    """
    
    #Fill the data to query using the data from gps
    query_insert_data_table = query_insert_data_table.format(gps_data['timestamp_unix'],\
                                                             gps_data['latitude'],\
                                                             gps_data['longitude'],\
                                                             gps_data['speed'],\
                                                             gps_data['heading']
                                                             )
    
    #Execute query to insert data to table
    c.execute(query_insert_data_table)
    
    #Save changes in database
    conn.commit()
    conn.close()