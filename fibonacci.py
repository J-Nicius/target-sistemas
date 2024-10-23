def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence

def check_fibonacci(num):
    sequence = fibonacci_sequence(num)
    if num in sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso
num = int(input("Informe um número: "))
print(check_fibonacci(num))
