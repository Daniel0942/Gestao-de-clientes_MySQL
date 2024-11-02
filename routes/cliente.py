from flask import Blueprint, render_template, request
from database.clientes import CLIENTES

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route("/")
def lista_cliente():
    return render_template("listar_clientes.html", clientes = CLIENTES)

@cliente_route.route("/new")
def form_cliente():
    # formulário para inserir novo cliente
    return render_template("form.html")

@cliente_route.route("/", methods=["POST"])
def inserir_cliente():
    data = request.json

    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "Nome": data["nome"],
        "Email": data["email"]
    }
    CLIENTES.append(novo_usuario)
    return {"Data": novo_usuario}

