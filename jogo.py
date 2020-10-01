from collections import namedtuple
from itertools import product
import random
# criando o baralho
Carta = namedtuple('Carta', ['face', 'naipe'])

faces = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
naipes = {'O', 'P', 'C', 'E'}

baralho = [Carta(face, naipe) for face, naipe in product(faces, naipes)]

# Perguntar quantas fichas o jogador quer comprar
Fichas = int(input("Quantas fichas gostaria de adquirir? "))
Preco = 10 * Fichas
print("Seu total é de R${0}!" .format(Preco))

# Perguntar quantas fichas deseja apostar
Aposta = int(input("Qual será sua aposta?"))
if Aposta < 1:
    print("Não tenha medo! Hoje senti que a sorte está do seu lado.")
elif Aposta > Fichas:
    Falta = Aposta - Fichas
    r = input("Você não tem todas essas fichas, gostaria de comprar mais {0} fichas?(s ou n) " .format(Falta))
    if r == 's':
        print('Você comprou {0} fichas! Vamos jogar!' .format(Falta))
    else:
        Aposta = int(input("Qual será sua aposta? "))
else:
    print('Vamos jogar!')

# embaralhando e selecionando as cartas dos jogadores
random.shuffle(baralho)

mao_jogador = baralho[0:2]
mao_banco = baralho[2:4]
print("Suas cartas são {0}" .format(mao_jogador))
print("As cartas do banco são {0}" .format(mao_banco))

# colocando os valores nas do jogador:
if mao_jogador[0][0] == 'A':
    pont1 = 1
elif mao_jogador[0][0] == '10' or mao_jogador[0][0] == 'J' or mao_jogador[0][0] == 'Q' or mao_jogador[0][0] == 'K' :
    pont1 = 0
elif int(mao_jogador[0][0]) < 10:
    pont1 = int(mao_jogador[0][0])

if mao_jogador[1][0] == 'A':
    pont2 = 1
elif mao_jogador[1][0] == '10' or mao_jogador[1][0] == 'J' or mao_jogador[1][0] == 'Q' or mao_jogador[1][0] == 'K' :
    pont2 = 0
elif int(mao_jogador[1][0]) < 10:
    pont2 = int(mao_jogador[1][0])
jogador = pont1 + pont2

# colocando valores nas cartas do banco:
if mao_banco[0][0] == 'A':
    pontu1 = 1
elif mao_banco[0][0] == '10' or mao_banco[0][0] == 'J' or mao_banco[0][0] == 'Q' or mao_banco[0][0] == 'K' :
    pontu1 = 0
elif int(mao_banco[0][0]) < 10:
    pontu1 = int(mao_banco[0][0])

if mao_banco[1][0] == 'A':
    pontu2 = 1
elif mao_banco[1][0] == '10' or mao_banco[1][0] == 'J' or mao_banco[1][0] == 'Q' or mao_banco[1][0] == 'K' :
    pontu2 = 0
elif int(mao_banco[1][0]) < 10:
    pontu2 = int(mao_banco[1][0])
banco = pontu1 + pontu2

# Descobrindo o vencedor

if jogador < 6:
    print('Você tem {0} pontos. Vamos lhe dar mais uma carta!' .format(jogador))
    mao_jogador += baralho[5]
    print("Sua carta é {0}" .format(mao_jogador[2]))
    if mao_jogador[2][0] == 'A':
        pont3 = 1
    elif mao_jogador[2][0] == '10' or mao_jogador[2][0] == 'J' or mao_jogador[2][0] == 'Q' or mao_jogador[2][0] == 'K' :
        pont3 = 0
    elif int(mao_jogador[2][0]) < 10:
        pont3 = int(mao_jogador[2][0])
    jogador += pont3
print("Você tem {0} pontos" .format(jogador))

if banco < 6:
    print('O banco tem {0} pontos. Vamos comprar mais uma carta!' .format(banco))
    mao_banco += baralho[6]
    print("A carta do banco é {0}" .format(mao_jogador[2]))
    if mao_banco[2][0] == 'A':
        pont3 = 1
    elif mao_banco[2][0] == '10' or mao_banco[2][0] == 'J' or mao_banco[2][0] == 'Q' or mao_banco[2][0] == 'K' :
        pont3 = 0
    elif int(mao_banco[2][0]) < 10:
        pont3 = int(mao_banco[2][0])
    banco += pont3
print("O banco tem {0} pontos" .format(banco))