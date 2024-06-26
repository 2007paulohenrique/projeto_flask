from flask import Flask, render_template, request, redirect, url_for

def listar_produtos():
    with open("produtos.csv", "r") as file:
        lista_produtos = []

        for linha in file:
            nome, descricao, preco, imagem = linha.strip().split(",")

            produto = {
                "nome": nome,
                "descricao": descricao,
                "preco": preco,
                "imagem": imagem
            }

            lista_produtos.append(produto)

        return lista_produtos
    
def add_produto(p):
    with open("produtos.csv", "a") as file:
        file.write(f"\n{p['nome']},{p['descricao']},{p['preco']},{p['imagem']}")


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contato")
def contato():
    return "<h1>Conposttato</h1>"

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=listar_produtos())

@app.route("/produtos/<nome>")
def produto(nome):
    for produto in listar_produtos():
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
    produto = {"nome":nome, "descricao":descricao, "preco":preco, "imagem": imagem}

    add_produto(produto)

    return redirect(url_for("produtos"))

app.run(port=5000)