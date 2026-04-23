from flask import Flask, render_template, request, redirect, url_for
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

@app.route('/verificaridade/<int:idade>')
def verificaridade(idade):
    if idade >= 18:
        return 'Você é MAIOR de idade'
    else:
        return 'Você é MENOR de idade'

@app.route('/verificaridade2/<int:idade>')
def verificaridade2(idade):
    return render_template('idade.html', idade=idade)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/verificarlogin', methods=['POST'])
def verificarlogin():
    login = request.form.get("login")
    senha = request.form.get("senha")
    if login == "admin" and senha == "12345":
        return redirect (url_for('arearestrita'))
    else:
        return redirect (url_for('acessonegado'))

@app.route('/arearestrita')
def arearestrita():
    return render_template('arearestrita.html')

@app.route('/acessonegado')
def acessonegado():
    return render_template('acessonegado.html')

if __name__ == '__main__':
    app.run()