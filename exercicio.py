numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

    idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você é obrigado a votar.")
elif idade == 16 or idade == 17:
    print("Seu voto é opcional.")
else:
    print("Você ainda não pode votar.")

    numero = 27  # Você pode alterar este número para testar

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

    lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Verificação do tipo de triângulo
if lado1 == lado2 == lado3:
    print("O triângulo é Equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é Isósceles.")
else:
    print("O triângulo é Escaleno.")

    numero = int(input("Digite um número para verificar se é múltiplo de 5 e 7: "))

if numero % 5 == 0 and numero % 7 == 0:
    print(f"O número {numero} é múltiplo de 5 e de 7.")
else:
    print(f"O número {numero} NÃO é múltiplo de 5 e 7 ao mesmo tempo.")

    numero = float(input("Digite um número: "))

if numero > 0 and numero > 10:
    print("O número é positivo e maior que 10.")
else:
    print("O número não atende a ambas as condições.")

    numero = int(input("Digite um número: "))

if numero % 3 == 0 or numero % 5 == 0:
    print(f"O número {numero} é divisível por 3 ou por 5.")
else:
    print(f"O número {numero} NÃO é divisível nem por 3 nem por 5.")



    ('cliente 1','cliente 2','cliente 3')
    'nome'('cliente 1')
    'nome'('cliente 2') 
    'nome'('cliente 3')
print('cliente')
   
'cliente 1'(idade)
'cliente 2'(idade)
'cliente'3(idade)

'quartos'
'simples 100.00'
'duplo 150.00'
'luxo 250.00'
print('quartos')