texto = input("Digite uma palavra ou frase: ")

ocorrencias = {}  # Dicionário vazio para armazenar a contagem

for caractere in texto:
    if caractere in ocorrencias:
        ocorrencias[caractere] += 1
    else:
        ocorrencias[caractere] = 1

print("\n🔍 Frequência de cada caractere:")
for caractere, quantidade in ocorrencias.items():
    print(f"'{caractere}': apareceu {quantidade} vez(es)")
