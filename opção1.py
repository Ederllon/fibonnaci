def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False
num = int(input("Digite um número: "))
if fibonacci(num):
    print(f"O número {num} pertence à sequência de fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de fibonacci.")
