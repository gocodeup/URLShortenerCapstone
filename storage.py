#!/usr/bin/env python3

import datetime
from xmlrpc.client import boolean
import psycopg  # use PostgreSQL
from typing import Optional
'''Storage layer for our URL shortener project.  Translates get/set requests into the backend storage interface.'''

CONNECTION_STRING = 'dbname=url_shortener user=url_shortener password=Passw0rd'

def get_info(short_code: Optional[str]=None, url: Optional[str]=None) -> Optional[dict]:
    '''
    Get the info for the requested short_code or url.
    Returns: 
        None if short_code doesn't exist
        info dictionary associated with short_code if short_code exists
    '''
    with psycopg.connect(CONNECTION_STRING) as db_connection:
        with db_connection.cursor() as cur:
            if short_code:
                param = 'shortcode'
                val = short_code
            elif url:
                param = 'url'
                val = url
            cur.execute(f'SELECT * FROM urls WHERE {param} = %s', (val, ))
            record = cur.fetchone()
            if record is None:
                return None
            else:
                return {'url': record[1], 'short_code': record[2], 'timestamp': record[3], 'ip_address': str(record[4])}
def store_url(url: str, timestamp: datetime.datetime, ip_address: str, short_code: str) -> boolean:
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