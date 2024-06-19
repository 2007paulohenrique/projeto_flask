from flask import Flask, render_template, request, redirect, url_for

lista_produtos = [
    {"nome": "Coca-cola", "descricao": "veneno", "preco": "10.00", "url_image": "https://www.shutterstock.com/image-vector/novi-sad-serbia-january-21-600nw-1008479416.jpg"},
    {"nome": "Doritos", "descricao": "suja a mão", "preco": "8.00", "url_image": "https://m.media-amazon.com/images/I/610trEtCQuS._AC_UF1000,1000_QL80_.jpg"},
    {"nome": "Agua", "descricao": "mata sede", "preco": "5.00", "url_image": "https://www.imigrantesbebidas.com.br/bebida/images/products/full/2893-agua-mineral-crystal-sem-gas-500ml.jpg"},
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Conposttato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto['nome'] == nome:
            return render_template("produto.html", produto=produto)
    return "Produto não existe!"

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = request.form["preco"]
    imagem = request.form["imagem"]
    produto = {"nome":nome, "descricao":descricao, "preco":preco, "url_image": imagem}

    lista_produtos.append(produto)

    return redirect(url_for("produtos"))

app.run(port=5000)