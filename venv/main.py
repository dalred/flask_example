from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    search = request.args['search']
    return f'Ищем {search}'


app.run()