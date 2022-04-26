from flask import Flask, render_template, redirect, url_for
from threading import Thread

app = Flask('')

@app.route('/')
def index():
  return render_template('index.html')
  #return "It's quite remarkable that I am still alive"
  
def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()