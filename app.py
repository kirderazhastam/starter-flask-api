from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    url = "https://thoughtful-train-tick.cyclic.app/duc"
    req = requests.get(url)
    return req.text


