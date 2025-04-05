frutas =  ["maçã", "banana", "cereja"]

preco_frutas =  {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

total= 0

for item in frutas:
    if item in preco_frutas:
        total += preco_frutas[item]
    else:
        print(f"⚠️ Atenção: '{item}' não tem preço definido!")

print(f"\n🛒 Preço total da lista de compras: R$ {total:.2f}")