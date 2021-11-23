import json, os
from flask import Flask, request

app = Flask(__name__)


def read_json(name):
    data = {}
    with open(name, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


@app.route('/')
def index():
    if read_json("settings.json")['online']:
        return 'Приложение работает'
    else:
        return 'Приложение не работает'


@app.route('/candidate/<int:x>/')
def candidat(x):
    data = read_json("candidates.json")
    id_lst = [i['id'] for i in data]
    if x not in id_lst:
        return ('<html lang="ru"><p><b>Кандидат не найден!</b></p>')
    else:
        data = data[x - 1]
        return f"<h1>{data['name']}</h1>" \
               f"<p>{data['position']}</p>" \
               f"<img src='{data['picture']}' width=200/>" \
               f"<p>{data['skills']}</p>"

@app.route('/list/')
def allcandidat():
    html = '<h1>Все кандидаты</h1>'
    data = read_json("candidates.json")
    for item in data:
        html += f"<p><a href='/candidate/{item['id']}'>{item['name']}</a></p>"
    return html

if __name__ == "__main__":
    app.run('127.0.0.1', 8000)
