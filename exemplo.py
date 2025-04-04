import json

lista = ["Sapato", 39, 10.38, True]

produto_1: dict = {
    "nome": "sapato",
    "quatidade": 39,
    "preco": 12.30,
    "disponibilidade": True
}

produto_2: dict = {
    "nome": "Televisao",
    "quatidade": 10,
    "preco": 70.30,
    "disponibilidade": False
}


carrinho : list = []
carrinho.append(produto_1)
carrinho.append(produto_2)

print(carrinho)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)