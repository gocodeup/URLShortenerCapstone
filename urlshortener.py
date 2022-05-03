#!/usr/bin/env python3

'''Simple Flask server that shortens URLs into 10 characters.'''

from flask import Flask, redirect, render_template, request
import logging
import storage
import datetime
import hashlib
import re

app_log = logging.getLogger(__name__)
app = Flask(__name__)

SHORTCODE_LENGTH = 10
shortcode_regex = re.compile(f'[0-9a-f]{{{SHORTCODE_LENGTH}}}')

@app.route('/')
def index():
    '''Root route to serve up the URL shortener interface'''
    return render_template('index.html')

@app.route('/url/<shortcode>')
def get_url(shortcode):
    '''Get the url for the given short code'''
    if not validate_short_code(shortcode):
        # TODO: return an error message about invalid shortcode
        return f'<h1>Invalid shortcode {shortcode}</h1>'
    info = storage.get_info(short_code=shortcode)
    if info:
        return redirect(info['url'])
    else:
        # TODO no entry for this shortcode - return an error template
        return f'<h1>Error: no entry for shortcode {shortcode}</h1>'

@app.route('/lookup', methods=['POST'])
def get_info():
    '''Get the info (created time, associated url, etc.) for the posted short code'''
    shortcode = request.form['shortcodeInput']
    if not validate_short_code(shortcode):
        # TODO: return an error message about invalid shortcode
        return f'<h1>Invalid shortcode {shortcode}</h1>'
    info = storage.get_info(short_code=shortcode)
    # TODO: run the info through a template
    return info

@app.route('/create', methods=['POST'])
def create():
    '''Create a shortened code using the info in the posted data'''
    url = request.form['urlInput']
    # TODO: validate that it is a url
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    ip_address = request.remote_addr
    short_code = generate_short_code(url)
    storage.store_url(url=url, timestamp=timestamp, ip_address=ip_address, short_code=short_code)
    # TODO: run the info through the template
    return {'url': url, 'short_code': short_code, 'timestamp': timestamp, 'ip_address': ip_address}

def generate_short_code(url):
    '''Generate a short code given the url'''
    return hashlib.sha256(url.encode()).hexdigest()[:SHORTCODE_LENGTH]

def validate_short_code(shortcode):
    '''Check to make sure a shortcode matches our rules for characters, length, etc.'''
    if len(shortcode) != SHORTCODE_LENGTH:
        return False
    if not shortcode_regex.match(shortcode):
        return False
    return True

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