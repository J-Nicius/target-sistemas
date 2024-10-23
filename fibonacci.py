def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        soma = sequencia[-1] + sequencia[-2]
        sequencia.append(soma)
    print (sequencia)

def verificar_fibonacci(num):
    sequence = fibonacci(num)
    if num in sequence:
        print (f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print (f"O número {num} não pertence à sequência de Fibonacci.")

num = int(input("Informe um número: "))
print(verificar_fibonacci(num))
