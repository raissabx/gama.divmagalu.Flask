import re
from flask import Flask
from flask import render_template 
from flask import url_for, redirect
from flask import request
import pandas as pd

app = Flask(__name__)

serie = pd.read_csv('produtos.csv', header=None, names=['produtos', 'valores'])
serie = serie.set_index('produtos')
serie = serie['valores']
print(serie)

@app.route('/')
def index():
    print("Hello print")
    return "Hello return"

#criar segunda rota
@app.route('/gama')
def gama():
    return 'sou uma nova rota'

@app.route('/hello/<name>')
def hello(name):
    return f'Olá, {name}'

lista_produto = []

@app.route('/listar')
def listar():
    return lista_produto

@app.route('/adicionar/<produto>')
def adicionar(produto):
    lista_produto.append(produto)
    return 'Produto adicionado'

produtos = {}

#rota para adicionar produtos, valores no dicionario
@app.route('/listar2')
def listar2():
    #return produtos
    return serie.to_dict()

#rota para adicionar produtos, valores no dicionario
@app.route('/adicionar/<produto>/<valor>') # essa url substitui o input
def adicionar2(produto, valor):
    produtos[produto] = float(valor)
    #transfomar valor (texto) para float
    #Insira um código para adicionar a chava produto com o valor no dicionario
    return 'Produto adicionado'

@app.route('/cadastro')
def cadastro():
    argumentos = request.args.to_dict()
    preco = argumentos['preco']
    nome = argumentos['produto']
    serie[nome] = preco
    serie.to_csv('produtos.csv', header=False)
    print()
    return argumentos


if __name__ == "__main__":
    app.run(debug=True)