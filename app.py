#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)


# all links have form "/req/..."
from backend_requests import *






#random secret key
app.config['SECRET_KEY'] = 'InnopolisProjectSchool2019'

if __name__ =='__main__':
    app.run(port=8080, host='127.0.0.1')