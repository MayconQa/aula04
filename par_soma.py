def encontrar_pares_soma(lista, alvo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6]
soma_desejada = 7
resultado = encontrar_pares_soma(numeros, soma_desejada)
print("Pares que somam", soma_desejada, ":", resultado)
