def conta_a(frase):
    conta_a_n = frase.count('a')
    conta_a_m = frase.count('A')
    soma_a = conta_a_n + conta_a_m

    return f"A letra 'a' minúscula aparece {conta_a_n} vez(es) e a letra 'A' maiúscula aparece {conta_a_m} vez(es) na string. Total: {soma_a}."

# Exemplo de uso
frase = input("Digite uma string: ")
print(conta_a(frase))

