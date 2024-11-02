from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "Gestão de clientes"
    clientes = [
        {"nome": "Daniel", "membro_ativo": True},
        {"nome": "Maria", "membro_ativo": False},
        {"nome": "José", "membro_ativo": False}
    ]
    return render_template("index.html", titulo=titulo, clientes=clientes)


if __name__ == "__main__":
    app.run(debug=True)