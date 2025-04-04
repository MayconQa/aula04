lista: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

for numero in lista:
    numero = int(numero) 
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}")
