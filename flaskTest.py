# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:58:32 2020

@author: Michael
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Flask"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')