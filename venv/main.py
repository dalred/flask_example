from flask import Flask, request

app = Flask(__name__)
#Тест2

@app.route('/')
def hello():
    search = request.args['search']
    return f'Ищем {search}'


app.run()
