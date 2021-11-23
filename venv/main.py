import json, os
from flask import Flask, request


app = Flask(__name__)

def read_json(name):
  data = {}
  with open(name, "r", encoding = 'utf-8') as file:
        data = json.load(file)
  return data

@app.route('/')
def index():
    if read_json("settings.json")['online']:
        return 'Приложение работает'
    else:
        return 'Приложение не работает'

if __name__ == "__main__":
    app.run('127.0.0.1',8000)