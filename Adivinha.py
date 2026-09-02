print("jogo de adivinhação")
print("tente adivinhar o número que estou pensando entre 1 e 100")
print("você tem apenas 7 tentativa para acertar o número secreto")

import random
numero_secreto = random.randint(1, 100)


contador = 7
acertou = False
while contador > 0 and not acertou:
    tentativas = int(input("digite seu palpite:"))
    if tentativas == numero_secreto:
        print("parabéns! você acertou!")
        acertou = True
        break
    elif tentativas < numero_secreto:
        print("O número secreto é maior do que o seu palpite. Tente novamente!")
else:
    print("O número secreto é menor do que o seu palpite. Tente novamente!")

print("O número secreto era:", numero_secreto)