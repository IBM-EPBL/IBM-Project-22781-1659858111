from flask import Flask

app = Flask(__name__)

@app.rout('/')
def index():
  return "Hello, World!"
