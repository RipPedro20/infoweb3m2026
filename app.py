from flask import Flask, render_template, request
from datetime import datetime 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faleconosco')
@app.route('/email')
@app.route('/contato')
def contato():
    dados = {"nome" : "PG", "email" : "f.coutinho", "tel" : "(84) 9 8892-5492"}
    return render_template('contato.html', dados = dados)

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/disciplinas')
def disciplinas():
    return render_template('disciplinas.html')

@app.route('/acessol')
def acessol():
    return render_template('acesSol.html')

@app.route('/usuario', defaults={"nome" : "Desconhecido", "sobrenome" : "Desconhecido"})
@app.route('/usuario/<nome>/<sobrenome>')
def usuario(nome, sobrenome):
    info = {"nome" : nome, "sobrenome" : sobrenome}
    return render_template('usuario.html', info = info)

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/recebedados', methods=['POST'])
def recebedados():
    nome = request.form.get('nome')
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    datanasc = request.form['datanasc']
    estado = request.form.get('estado')
    escola = request.form.getlist('escola')
    # data_objeto = datetime.strptime(datanasc, "%Y-%m-%d")
    # data_formatada = data_objeto.strptime("%d/%m/%Y")
    return render_template('recebedados.html', nome=nome, sobrenome=sobrenome, email=email, datanasc=datanasc, estado=estado, escola=escola)

@app.route('/compras')
def compras():
    return render_template('compras.html')

@app.route('/recebecompras', methods=['POST'])
def recebecompras():
    itens = request.form.getlist('item')
    return render_template('lista.html', itens=itens)

if __name__ == '__main__':
    app.run()