from collections import namedtuple
from itertools import product
import random
# criando o baralho
Carta = namedtuple('Carta', ['face', 'naipe'])

faces = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
naipes = {'O', 'P', 'C', 'E'}

baralho = [Carta(face, naipe) for face, naipe in product(faces, naipes)]

# embaralhando e selecionando as cartas dos jogadores
random.shuffle(baralho)

mao_jogador = baralho[0:2]
mao_banco = baralho[2:4]
print("Suas cartas são {0}" .format(mao_jogador))
print("As cartas do banco são {0}" .format(mao_banco))

# colocando os valores nas do jogador:
if mao_jogador[0][0] == 'A':
    pont1 = 1
elif mao_jogador[0][0] == '10':
    pont1 = 0
elif mao_jogador[0][0] == 'J':
    pont1 = 0
elif mao_jogador[0][0] == 'Q':
    pont1 = 0
elif mao_jogador[0][0] == 'K':
    pont1 = 0
elif int(mao_jogador[0][0]) < 10:
    pont1 = int(mao_jogador[0][0])

if mao_jogador[1][0] == 'A':
    pont2 = 1
elif mao_jogador[1][0] == '10':
    pont2 = 0
elif mao_jogador[1][0] == 'J':
    pont2 = 0
elif mao_jogador[1][0] == 'Q':
    pont2 = 0
elif mao_jogador[1][0] == 'K':
    pont2 = 0
elif int(mao_jogador[1][0]) < 10:
    pont2 = int(mao_jogador[1][0])
jogador = pont1 + pont2
print("Você tem {0} pontos" .format(jogador))

# colocando valores nas cartas do banco:
if mao_banco[0][0] == 'A':
    pontu1 = 1
elif mao_banco[0][0] == '10':
    pontu1 = 0
elif mao_banco[0][0] == 'J':
    pontu1 = 0
elif mao_banco[0][0] == 'Q':
    pontu1 = 0
elif mao_banco[0][0] == 'K':
    pontu1 = 0
elif int(mao_banco[0][0]) < 10:
    pontu1 = int(mao_banco[0][0])

if mao_banco[1][0] == 'A':
    pontu2 = 1
elif mao_banco[1][0] == '10':
    pontu2 = 0
elif mao_banco[1][0] == 'J':
    pontu2 = 0
elif mao_banco[1][0] == 'Q':
    pontu2 = 0
elif mao_banco[1][0] == 'K':
    pontu2 = 0
elif int(mao_banco[1][0]) < 10:
    pontu2 = int(mao_banco[1][0])
banco = pontu1 + pontu2
print("O banco tem {0} pontos" .format(banco))