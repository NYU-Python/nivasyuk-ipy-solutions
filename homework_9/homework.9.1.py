#!/usr/bin/env python

import flask
import requests

app = flask.Flask(__name__)

# make the wsgi interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# what this url will represent
# server/

@app.route('/') # root url
def home():
    return flask.render_template("home.html")

@app.route('/favicon.ico')
def favicon():
    return flask.send_from_directory(os.path.join(app.root_path, 'resources'),
                                    'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/input.html')
def input():
    return flask.render_template("input.html")

@app.route('/results.html')
def results():
    ticker = flask.request.args.get('ticker')
    yahoo_url = "http://download.finance.yahoo.com/d/quotes.csv?s={0}&f=a".format(ticker)
    stock_price = requests.get(yahoo_url).content
    return flask.render_template("results.html", ticker=ticker, stock_price=stock_price)

# Launching our server
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)


