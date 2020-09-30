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
print(mao_jogador)

# colocando os valores nas cartas
if mao_jogador[0][0] == 'A':
    valor = 1
elif mao_jogador[0][0] == '10' or 'J' or 'Q' or 'K':
    valor = 0
else:
    valor = mao_jogador[0][0]
print(valor)