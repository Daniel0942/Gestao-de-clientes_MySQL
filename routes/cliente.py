from flask import Blueprint, render_template, request
from models.table import db, Cliente

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route("/")
def lista_cliente():

    clientes = Cliente.select()
    return render_template("listar_clientes.html", clientes = clientes)

@cliente_route.route("/new")
def form_cliente():
    # formulário para inserir novo cliente
    return render_template("form.html")

@cliente_route.route("/", methods=["POST"])
def inserir_cliente():

    data = request.json
    
    novo_usuario = Cliente.create(
        Nome = data["nome"], 
        Email = data["email"]
        )
    
    return render_template("item_cliente.html", cliente=novo_usuario)

@cliente_route.route("/<int:cliente_id>/exibir")
def detalhe_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    return render_template("detalhe_cliente.html", cliente=cliente)

@cliente_route.route("/<int:cliente_id>/delete", methods=["DELETE"])
def deletar_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {"DELETAR": "OK"}


@cliente_route.route("/<int:cliente_id>/edit")
def form_edit_cliente(cliente_id):

    cliente = Cliente.get_by_id(cliente_id)
    return render_template("form.html", cliente=cliente)

@cliente_route.route("/<int:cliente_id>/update", methods=["PUT"])
def editar_cliente(cliente_id):
    """ atualizar informacoes do cliente """
    cliente_editado = None

    # obter dados do formulario de edicao
    data = request.json

    # obter usuario pelo id
    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.Nome = data["nome"]
    cliente_editado.Email = data["email"]
    cliente_editado.save()
            
    return render_template("item_cliente.html", cliente = cliente_editado)