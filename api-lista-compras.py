from flask import Flask, jsonify, request

app = Flask(__name__)

itens = [
    {"id": 1, "nome": "Arroz 5kg", "quantidade": 2, "categoria": "Alimentos", "prioridade": "alta", "comprado": False},
    {"id": 2, "nome": "Feijão 1kg", "quantidade": 10, "categoria": "Alimentos", "prioridade": "alta", "comprado": False}
]

@app.route("/compras", methods=["GET"])
def get_compras():
    return jsonify({"mensagem": "Lista de compras", "itens":itens, "total": len(itens)})

@app.route("/compras/<int:id>", methods=["GET"])
def get_compra_by_id(id):
    for item in itens:
        if item["id"] == id:
            return jsonify({"mensagem": "Item encontrado!", "item": item})
        
    return jsonify({"mensagem": "Item não encontrado"}), 404

@app.route("/compras", methods=["POST"])
def add_item():
    novo_item = request.json

    novo_item["id"] = len(itens) + 1
    itens.append(novo_item)
    return jsonify({"mensagem": "Item cadastrado!", "item": novo_item})

@app.route("/compras/<int:id>", methods=["PUT"])
def update_item(id):
    dados = request.json

    for item in itens:
        if item["id"] == id:
            item.update(dados)
            return jsonify({"mensagem": "Item atualizado!"})
        
    return jsonify({"mensagem": "Item não encontrado!"}), 404

@app.route("/compras/<int:id>", methods=["DELETE"])
def delete_item(id):
    for item in itens:
        if item["id"] == id:
            itens.remove(item)
            return jsonify({"mensagem": "Item deletado!"})
        
    return jsonify({"mensagem": "Item não encontrado!"}), 404