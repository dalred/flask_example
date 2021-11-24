import json, os
from flask import Flask, request

app = Flask(__name__)


#Функция для считывания JSON
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

#C регуляркой не делал специально
@app.route('/search')
def searching():
    k = 0
    html=''
    search = request.args.get("name")
    data = read_json("candidates.json")
    case_sensetive = read_json("settings.json")['case-sensitive']
    for item in data:
        if case_sensetive:
            if search.lower() in item['name']:
                k += 1
                html += f"<p><a href='/candidate/{item['id']}'>{item['name']}</a></p>"
        else:
            if search.lower() in item['name'].lower():
                k += 1
                html += f"<p><a href='/candidate/{item['id']}'>{item['name']}</a></p>"
    html = f'<h1>найдено кандидатов {k}</h1>' + html
    return html

#Если под лимитом подрузамевалось взятие всех данных и отсечка по лимиту, то можно использовать срезы
# return "".join(html[:limit])
@app.route('/skill/<search>')
def skill(search):
    html=[]
    data = read_json("candidates.json")
    limit = read_json("settings.json")['limit']
    for item in data:
        if search.lower() in item['skills'].lower().split(', '):
            html.append(f"<p><a href='/candidate/{item['id']}'>{item['name']}</a></p>")
        if len(html) == limit:
            return "".join(html)
    if len(html)==0:
        html.append(f"<h3>Кандидаты не найдены!</h3>")
    return "".join(html)


if __name__ == "__main__":
    app.run('127.0.0.1', 8000)