#!/usr/bin/env python3

'''Simple Flask server that shortens URLs into 8 characters or less.'''

from flask import Flask
import logging

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