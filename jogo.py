# EP - Design de Software
# Equipe: Guilherme Fontana
# Data: 01/10/2020
from collections import namedtuple
from itertools import product
import random
import time
# criando o baralho
Carta = namedtuple('Carta', ['face', 'naipe'])

faces = {'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'}
naipes = {'O', 'P', 'C', 'E'}

baralho = [Carta(face, naipe) for face, naipe in product(faces, naipes)]

# Perguntar quantas fichas o jogador quer comprar
Fichas = int(input("Quantas fichas gostaria de adquirir? "))
Preco = 10 * Fichas
print("Seu total é de R${0}!" .format(Preco))

while True:
    # Perguntar quantas fichas deseja apostar

    Aposta = int(input("Qual será sua aposta?"))
    if Aposta < 1:
        print("Não tenha medo! Hoje senti que a sorte está do seu lado.")
    elif Aposta > Fichas:
        Falta = Aposta - Fichas
        r = input("Você não tem todas essas fichas, gostaria de comprar mais {0} fichas?(s ou n) " .format(Falta))
        if r == 's':
            print('Você comprou {0} fichas! Vamos jogar!' .format(Falta))
            Fichas += Falta
            Fichas -= Aposta
        else:
            Aposta = int(input("Qual será sua aposta? "))
    else:
        print('Vamos jogar!')
        Fichas -= Aposta

    time.sleep(2)

    # Perguntar em quem deseja apostar

    Apostado = input("Em quem você deseja apostar?(jogador, banco ou empate) ")

    # embaralhando e selecionando as cartas dos jogadores
    random.shuffle(baralho)

    mao_jogador = baralho[0:2]
    mao_banco = baralho[2:4]
    print("Suas cartas são {0}" .format(mao_jogador))
    time.sleep(2)
    print("As cartas do banco são {0}" .format(mao_banco))

    # colocando os valores nas do jogador:
    if mao_jogador[0][0] == 'A':
        pont1 = 1
    elif mao_jogador[0][0] == '10' or mao_jogador[0][0] == 'J' or mao_jogador[0][0] == 'Q' or mao_jogador[0][0] == 'K':
        pont1 = 0
    elif int(mao_jogador[0][0]) < 10:
        pont1 = int(mao_jogador[0][0])

    if mao_jogador[1][0] == 'A':
        pont2 = 1
    elif mao_jogador[1][0] == '10' or mao_jogador[1][0] == 'J' or mao_jogador[1][0] == 'Q' or mao_jogador[1][0] == 'K':
        pont2 = 0
    elif int(mao_jogador[1][0]) < 10:
        pont2 = int(mao_jogador[1][0])
    jogador = pont1 + pont2

    # colocando valores nas cartas do banco:
    if mao_banco[0][0] == 'A':
        pontu1 = 1
    elif mao_banco[0][0] == '10' or mao_banco[0][0] == 'J' or mao_banco[0][0] == 'Q' or mao_banco[0][0] == 'K':
        pontu1 = 0
    elif int(mao_banco[0][0]) < 10:
        pontu1 = int(mao_banco[0][0])

    if mao_banco[1][0] == 'A':
        pontu2 = 1
    elif mao_banco[1][0] == '10' or mao_banco[1][0] == 'J' or mao_banco[1][0] == 'Q' or mao_banco[1][0] == 'K':
        pontu2 = 0
    elif int(mao_banco[1][0]) < 10:
        pontu2 = int(mao_banco[1][0])
    banco = pontu1 + pontu2

    # Definindo a pontuação

    # Checando o vencedor
    
    j_venceu = False
    b_venceu = False
    if jogador >= 10:
        jogador -= 10
    if jogador == 9 or jogador == 8:
        print('O jogador alcançou a pontuação desejada')
        j_venceu = True
    if banco >= 10:
        banco -= 10
    if banco == 9 or banco == 8:
        print('O banco alcançou a pontuação desejada')
        b_venceu = True

    # Caso os valores estejam abaixo de 6

    if jogador < 6 and b_venceu == False:
        print('Você tem {0} pontos. Vamos lhe dar mais uma carta!' .format(jogador))
        mao_jogador += baralho[5]
        time.sleep(2)
        print("Sua carta é {0}" .format(mao_jogador[2]))
        if mao_jogador[2][0] == 'A':
            pont3 = 1
        elif mao_jogador[2][0] == '10' or mao_jogador[2][0] == 'J' or mao_jogador[2][0] == 'Q' or mao_jogador[2][0] == 'K':
            pont3 = 0
        elif int(mao_jogador[2][0]) < 10:
            pont3 = int(mao_jogador[2][0])
        jogador += pont3
    if jogador == 9 or jogador == 8 and j_venceu == False:
        print('O jogador alcançou a pontuação desejada')
        j_venceu = True
    elif jogador >= 10:
        jogador -= 10
    time.sleep(1)
    print("Você tem {0} pontos" .format(jogador))


    if banco < 6 and j_venceu == False:
        print('O banco tem {0} pontos. Vamos comprar mais uma carta!' .format(banco))
        mao_banco += baralho[6]
        time.sleep(2)
        print("A carta do banco é {0}" .format(mao_banco[2]))
        if mao_banco[2][0] == 'A':
            pont3 = 1
        elif mao_banco[2][0] == '10' or mao_banco[2][0] == 'J' or mao_banco[2][0] == 'Q' or mao_banco[2][0] == 'K':
            pont3 = 0
        elif int(mao_banco[2][0]) < 10:
            pont3 = int(mao_banco[2][0])
        banco += pont3
    if banco == 9 or banco == 8 and b_venceu == False:
        print('O banco alcançou a pontuação desejada')
        b_venceu = True
    if banco >= 10:
        banco -= 10
    time.sleep(1)
    print("O banco tem {0} pontos" .format(banco))

    # Definindo o vencedor

    time.sleep(2)
    if jogador == 9 and banco != 9 or jogador > banco:
        if Apostado == 'jogador':
            print('Você ganhou!!! Aqui está suas {0} fichas' .format(2 * Aposta))
            Fichas += Aposta * 2
        else:
            print("Você perdeu! Deveria ter apostado em si mesmo hein?")
    elif jogador == banco:
        if Apostado == 'empate':
            print('Você ganhou!!! Aqui está suas {0} fichas' .format(9 * Aposta))
            Fichas += Aposta * 9
        else:
            print('Você perdeu! O jogo empatou.')
    elif banco == 9 and jogador != 9 or banco > jogador:
        if Apostado == 'banco':
            print('Você ganhou!!! Aqui está suas {0} fichas' .format(
            round(0.95 * Aposta)))
            Fichas += round(Aposta * 1.95)
        else:
            print("Você perdeu! A casa sempre sai vencendo.")

    jogar_mais = input("Vamos mais uma?(S ou N)")
    if jogar_mais == 'N':
        print('Ok, aqui estão suas {0} fichas, obrigado por jogar!' .format(Fichas))
        break
