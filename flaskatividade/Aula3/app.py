from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/sobre")
def sobre():
    return "Este é um projeto criado na Aula 3 de Flask!"


@app.route("/sobre/<nome>")
def exibir_usuario(nome):
    return f"Olá, {nome}! Bem-vindo ao seu perfil."

if __name__ == '__main__':
    app.run(debug=True)