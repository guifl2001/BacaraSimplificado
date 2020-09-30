# BacaraSimplificado
EP1 de Design de Software INSPER
O jogo consiste em partidas onde se pode apostar se o jogador ou o banco conseguem uma soma de cartas mais próxima de 9, na prática não é uma disputa, você tanto pode apostar na área do jogador, como na do banco. A única interação do jogador é apostar em quem será o vencedor da partida (jogador, banco ou empate). Todo o restante do jogo é realizado pela mesa de acordo com as regras simplificadas apresentadas abaixo (elas não cobrem todas as possibilidades de um jogo real). As apostas serão sempre de números inteiros positivos de fichas e o jogador começa com uma quantidade de fichas definida por você.

Regras:

    Inicialmente o jogador realiza sua aposta colocando a quantidade de fichas que quiser (no máximo as fichas que o jogador possui naquele momento) em quem acredita ser o vencedor (jogador, banco ou empate). A partir desse momento a mesa realiza todo o restante do jogo automaticamente.

É utilizado um baralho completo, com 52 cartas. Inicialmente a mesa embaralha as cartas e distribui duas para o jogador e duas para o banco. Se a soma das cartas (veja as regras da soma das cartas aqui) do jogador ou do banco for igual a 8 ou 9 o jogo termina e as apostas são pagas (veja as regras do pagamento das apostas aqui).

Se a soma das cartas tanto do jogador quanto do banco forem diferentes de 8 ou 9, a mesa decide se distribuirá uma terceira carta a cada um de acordo com as regras a seguir, começando pelo jogador e depois distribuindo a carta do banco:

Se a soma das cartas for 6 ou 7, não distribui mais uma carta;
Se a soma das cartas for 5 ou menos, distribui mais uma carta e a soma é recalculada.

Pagamento das apostas

O jogador perde as fichas apostadas se não tiver apostado no vencedor. Caso contrário, a quantidade de fichas recebidas depende de quem foi o vencedor da partida:

Jogador: se o jogador venceu a partida (obteve a soma mais próxima de 9), a mesa paga a mesma quantidade de fichas apostadas. Por exemplo, se o jogador apostou 10 fichas, ele receberá outras 10 fichas.
Banco: se o banco venceu a partida, a mesa paga 95% das fichas apostadas. Por exemplo, se o jogador apostou 20 fichas, ele receberá outras 19. Caso o número não seja inteiro o jogador receberá as fichas sempre arredondando para baixo. Por exemplo, se o jogador apostou 25 fichas, ele vai receber só 23 a mais.
Empate: se ocorreu um empate, e o jogador apostou no empate, a mesa paga 8 vezes a quantidade de fichas apostadas. Por exemplo, se o jogador apostou 10 fichas, ele receberá outras 80.