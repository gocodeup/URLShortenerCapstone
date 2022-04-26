#!/usr/bin/env python3

'''Simple Flask server that shortens URLs into 10 characters.'''

from flask import Flask
import logging
import storage
import datetime
import hashlib

app_log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    '''Root route to serve up the URL shortener interface'''
    return

@app.route('/url/<short_code>')
def get_url(short_code):
    '''Get the url for the given short code'''
    return

@app.route('/info/<string:short_code>')
def get_info(short_code: str):
    '''Get the info (created time, associated url, etc.) for the given short code'''
    return

def generate_short_code(url):
    '''Generate a short code given the url'''
    length = 10
    return hashlib.sha256(url.encode()).hexdigest()[:length]

def test_storage():
    url = 'https://codeup.com'
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    ip_address = '127.0.0.1'
    short_code = generate_short_code(url)
    storage.store_url(url=url, timestamp=timestamp, ip_address=ip_address, short_code=short_code)

if __name__ == '__main__':
    test_storage()