from flask import Flask, redirect, url_for, request
from PIL import Image
import requests
import random
import time
import os

app = Flask(__name__)

from flask import Flask

app = Flask(__name__)

ip = '127.0.0.1'
port = 57554

def GetPixelColors(detail):
    resX = 32
    resY = 32
    colors = []
    time.sleep(0.1)
    img = Image.open(detail)
    img = img.resize((32, 32))
    pixels = img.load()
    for y in range(resX):
        for x in range(resY):
            color = []
            color.insert(0, pixels[x, y][0])
            color.insert(1, pixels[x, y][1])
            color.insert(2, pixels[x, y][2])
            colors.insert(len(colors)-1, color)
    os.remove(detail)
    return colors

@app.route('/')
def index():
    return 'test'

@app.route('/get', methods=['POST','GET'])
def fetch():
    url = request.args.get('url')
    sessionText = f's{str(random.randint(1000, 9999))}.png'
    img_data = requests.get(url).content
    with open(sessionText, 'wb') as handler:
        handler.write(img_data)
    time.sleep(0.1)
    return str(GetPixelColors(sessionText))

app.run(ip, port)
