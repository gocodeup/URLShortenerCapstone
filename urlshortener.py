#!/usr/bin/env python3

'''Simple Flask server that shortens URLs into 10 characters.'''

from flask import Flask, render_template
import logging
import storage
import datetime
import hashlib

app_log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/')
def index():
    '''Root route to serve up the URL shortener interface'''
    return render_template('index.html')

@app.route('/url/<short_code>')
def get_url(short_code):
    '''Get the url for the given short code'''
    return

@app.route('/lookup', methods=['POST'])
def get_info():
    '''Get the info (created time, associated url, etc.) for the posted short code'''
    return

@app.route('/create', methods=['POST'])
def create():
    '''Create a shortened code using the info in the posted data'''
    return

def generate_short_code(url):
    '''Generate a short code given the url'''
    length = 10
    return hashlib.sha256(url.encode()).hexdigest()[:length]

def test_store_url():
    url = 'https://codeup.com'
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    ip_address = '127.0.0.1'
    short_code = generate_short_code(url)
    storage.store_url(url=url, timestamp=timestamp, ip_address=ip_address, short_code=short_code)

def test_get_info():
    # this one should exist
    short_code = generate_short_code('https://codeup.com')
    print(storage.get_info(short_code=short_code))
    # this one won't exist
    print(storage.get_info(short_code='-'*10))
    # pull based on url
    print(storage.get_info(url='https://codeup.com'))
    # this one won't exist
    print(storage.get_info(url='-'*10))

if __name__ == '__main__':
    app.run()