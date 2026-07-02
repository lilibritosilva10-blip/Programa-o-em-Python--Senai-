import random


def atividade1():
    return random.randint(5, 10)


def atividade2():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(1, 100)
    return x, y, z 




import random


def atividade1():
    return random.randint(5, 10)

def atividade2():
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(1, 100)
    return x, y, z

def atividade3():
    return random.choice(range(10, 31))

def atividade4():
    for i in range(10, 0, -1):
        print(i)
    print("Fogo!")

def atividade5(numero):
    soma = 0
    for i in range(2, numero + 1):
        if i % 2 == 0:
            soma += i
    return soma

def atividade6(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def atividade7():
    for i in range(99, 0, -2):
        print(i)



print("--- Atividade 1 ---")
print("Número aleatório entre 5 e 10:", atividade1())

print("\n--- Atividade 2 ---")
num1, num2, num3 = atividade2()
print(f"Três números aleatórios: {num1}, {num2}, {num3}")

print("\n--- Atividade 3 ---")
print("Número aleatório entre 10 e 30 (usando range):", atividade3())

print("\n--- Atividade 4 ---")
atividade4()

print("\n--- Atividade 5 ---")
num_usuario5 = int(input("Digite um número inteiro positivo para somar os pares: "))
resultado_soma = atividade5(num_usuario5)
print(f"A soma dos números pares de 2 até {num_usuario5} é: {resultado_soma}")

print("\n--- Atividade 6 ---")
num_usuario6 = int(input("Digite um número para ver a tabuada: "))
atividade6(num_usuario6)

print("\n--- Atividade 7 ---")
print("Contagem regressiva de ímpares (99 a 1):")
atividade7()