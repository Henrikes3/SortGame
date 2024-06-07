import random

while True:
    mcdu = input('Digite uma Milhar: ')
    if mcdu == str('pare'):
        break
    resultado = []
    for r in range(4):
        numeros = random.randint(1, 9)
        resultado.append(numeros)


    if len(mcdu) != int(4):
        print('digite um numero valido')
        continue

    u = int(mcdu[3])
    d = int(mcdu[2])
    c = int(mcdu[1])
    m = int(mcdu[0])
  
    print(resultado)
    print(mcdu)


    if resultado[3] == u:
        print("voce acertou a Unidade")
    elif resultado[2] == d and resultado[3] == u:
        print("voce acertou a Dezena")
    elif resultado[1] == c and resultado[2] == d and resultado[3] == u:
        print("voce acertou a Centena")
    elif resultado[0] == m and resultado[1] == c and resultado[2] == d and resultado[3] == u:
        print("voce acertou a Milhar")
    else:
        print("Tente novamente")
