numero = int(input("Escolha um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

idade = int(input("Informe a idade: "))

#                      ---------

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 18:
    print("Adolescente")
elif idade > 18:
    print("Adulto")
else:
    print(" - ERRO - ")

#                      ---------

x = int(input("Informe a coordenada x: "))
y = int(input("Informe a coordenada y: "))

if x > 0 and y > 0:
    print("1º quadrante")
elif x < 0 and 0 < y:
    print("2º quadrante")
elif x < 0 and y < 0:
    print("3º quadrante")
elif y < 0 and 0 < x:
    print("4º quadrante")
else:
    print("Origem/Eixo")