#!/usr/bin/env python3

import datetime
import psycopg  # use PostgreSQL
'''Storage layer for our URL shortener project.  Translates get/set requests into the backend storage interface.'''

CONNECTION_STRING = 'dbname=url_shortener user=url_shortener password=Passw0rd'

def get_info(short_code: str):
    '''
    Get the info for the requested short_code.
    Returns: 
      None if short_code doesn't exist
      info dictionary associated with short_code if short_code exists
    '''
    return None

def store_url(url: str, timestamp: datetime.datetime, ip_address: str, short_code: str):
    '''
    Store the given url with the extra metadata into the storage backend.
    Returns:
      False if there was an error storing the information
      True on successful storage
    '''
    with psycopg.connect(CONNECTION_STRING) as db_connection:
        with db_connection.cursor() as cur:
            cur.execute('INSERT INTO urls (url, shortcode, created, creator) VALUES (%s, %s, %s, %s);',
                        (url, short_code, timestamp, ip_address))
            db_connection.commit()
    return True

def get_short_code(url: str):
    '''
    Get the short_code associated with the given URL.
    Returns:
      None if no short_code exists for the URL
      short_code if the url is in the storage engine
    '''
    return None
