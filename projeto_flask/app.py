from flask import Flask, render_template

lista_produtos = [
    {"nome": "Coca-cola", "descricao": "veneno"},
    {"nome": "Doritos", "descricao": "suja a mão"},
    {"nome": "Agua", "descricao": "mata sede"},
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return render_template("produto.html", produto=produto)
    return "Produto não existe!"


app.run(port=5000)