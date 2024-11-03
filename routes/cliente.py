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
    return render_template("item_cliente.html", cliente=novo_usuario)

@cliente_route.route("/<int:cliente_id>/exibir")
def detalhe_cliente(cliente_id):
    for c in CLIENTES:
        if c["id"] == cliente_id:
            cliente = c
    return render_template("detalhe_cliente.html", cliente=cliente)

@cliente_route.route("/<int:cliente_id>/delete", methods=["DELETE"])
def deletar_cliente(cliente_id):
    global CLIENTES
    CLIENTES = [c for c in CLIENTES if c["id"] != cliente_id]
    return {"DELETAR": "OK"}


@cliente_route.route("/<int:cliente_id>/edit")
def form_edit_cliente(cliente_id):

    cliente = None
    for c in CLIENTES:
        if c["id"] == cliente_id:
            cliente = c
    return render_template("form.html", cliente=cliente)

@cliente_route.route("/<int:cliente_id>/update", methods=["PUT"])
def editar_cliente(cliente_id):
    """ atualizar informacoes do cliente """
    cliente_editado = None

    # obter dados do formulario de edicao
    data = request.json

    # obter usuario pelo id
    for c in CLIENTES:
        if c["id"] == cliente_id:
            c["Nome"] = data["nome"]
            c["Email"] = data["email"]

            cliente_editado = c
            
    return render_template("item_cliente.html", cliente = cliente_editado)