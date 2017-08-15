from datetime import datetime
from src import app
from src.libs.YahooConnector import YahooConnector
from flask import request

@app.route('/')
def index():
    return ''

@app.route('/yahoo')
def yahoo_connect():
    if request.method == 'POST':
        stock = request.form.get('stock', default='', type=str) 
        try:
            return YahooConnector.connect(stock)
        except Exception as ex:
            return ex.message