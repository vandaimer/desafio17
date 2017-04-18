from app import app
from csv_reader import UserCSVReader, TrasactionCSVReader
from flask import render_template


@app.route('/')
def index():
    user_reader = UserCSVReader('usuarios.csv')
    trasaction_reader = TrasactionCSVReader('transacoes.csv')
    print(trasaction_reader.get_data())
    return render_template('index.html',
                           users=user_reader.get_data(),
                           transactions=trasaction_reader.get_data(),
            )
