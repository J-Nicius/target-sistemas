def conta_a(frase):
    conta_a_n = frase.count('a')
    conta_a_m = frase.count('A')
    soma_a = conta_a_n + conta_a_m

    print (f"A letra 'a' minúscula aparece {conta_a_n} vez(es).")
    print (f"A letra 'A' maiúscula aparece {conta_a_m} vez(es).")
    print (f"Na frase o total de letas 'A/a' é: {soma_a}")

    

# Exemplo de uso
frase = input("Digite uma string: ")
print(conta_a(frase))

