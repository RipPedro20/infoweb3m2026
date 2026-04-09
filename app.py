from flask import Flask, render_template

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

@app.route('/perfil/<usuario>')
def perfil(usuario):
	return render_template('perfil.html', usuario=usuario)

# @app.route('/semestre/<int:x>')
# def semestre(x):
#     dados = {}
#     dados=["atual"] = x
#     dados=["anterior"] = x - 1
#     return render_template('semestre.html', dados = dados)

if __name__ == '__main__':
    app.run()