from flask import Flask, request

app = Flask(__name__)
#Тест3

@app.route('/')
def hello():
    search = request.args['search']
    return f'Ищем {search}'


app.run()
