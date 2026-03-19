from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faleconosco')
@app.route('/email')
@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')

@app.route('/disciplinas')
def disciplinas():
    return render_template('disciplinas.html')

@app.route('/acessol')
def acessol():
    return render_template('acesSol.html')

if __name__ == '__main__':
    app.run()