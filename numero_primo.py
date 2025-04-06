def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Exemplos de uso
print(eh_primo(2))   # True
print(eh_primo(15))  # False
print(eh_primo(17))  # True
