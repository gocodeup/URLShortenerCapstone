#!/usr/bin/env python3

import datetime
'''Storage layer for our URL shortener project.  Translates get/set requests into the backend storage interface.'''

def get_info(short_code: str):
    '''
    Get the info for the requested short_code.
    Returns: 
      None if short_code doesn't exist
      info dictionary associated with short_code if short_code exists
    '''
    return None

def store_url(url: str, timestamp: datetime.datetime):
    '''
    Store the given url with the extra metadata into the storage backend.
    Returns:
      None if there was an error storing the information
      new short_code on successful storage
    '''
    return None

def get_short_code(url: str):
    '''
    Get the short_code associated with the given URL.
    Returns:
      None if no short_code exists for the URL
      short_code if the url is in the storage engine
    '''
    return None

def initialize_db_connection():
    pass