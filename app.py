#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)


# all links have form "/req/..."
from backend_requests import *


app.config['SECRET_KEY'] = 'e70lIUUoXRKlXc5VUBmiJ9Hdi'
#if __name__ =='__main__':
app.run(host='0.0.0.0', port=8024, debug=False)