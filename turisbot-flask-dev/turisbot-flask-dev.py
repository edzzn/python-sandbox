from flask import Flask
import os
import requests
from fb import getData, searchPage
from sys import argv

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
