from flask import Flask, render_template, request, redirect, url_for, flash
from validate_docbr import CPF, CNPJ
from forms import CPFForm, CNPJForm

app = Flask(__name__)
app.secret_key = '1234'

cpf = CPF()
cnpj = CNPJ()

@app.route('/')
def home2():
    return render_template('home2.html')

@app.route('/gerar/<tipo>')
def gerar(tipo):
    if tipo == 'cpf':
        documento = cpf.generate()
    elif tipo == 'cnpj':
        documento = cnpj.generate()
    else:
        documento = 'Tipo inválido'
    return render_template('gerar.html', documento=documento, tipo=tipo)

@app.route('/validar/<tipo>', methods=['GET', 'POST'])
def validar(tipo):
    if tipo == 'cpf':
        form = CPFForm()
        validador = cpf
    elif tipo == 'cnpj':
        form = CNPJForm()
        validador = cnpj
    else:
        return redirect(url_for('home2'))

    if form.validate_on_submit():
        documento = form.documento.data
        valido = validador.validate(documento)
        flash(f'O {tipo.upper()} é {"válido" if valido else "inválido"}.')
        return redirect(url_for('validar', tipo=tipo))

    return render_template('validar.html', form=form, tipo=tipo)

app.run(port=5000)
