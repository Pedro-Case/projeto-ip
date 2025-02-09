import pygame
pygame.init()
# Caracteristicas da tela
# O display (tela do jogo) é uma superficie onde tudo que está sendo mostrado ao jogador ficará
LARGURA_TELA, ALTURA_TELA = 1200, 700
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA)) 
FPS = 60
# Mapa do jogo
TAMANHO_TILE = 50
MAPA1 = [
    "PPPPPPPPPPPPPPPPPPPPPPPP",
    "P00PP00000000000000PPs0P",
    "Ps0PPs0s0s0s0s0s0s0PP00P",
    "P000000PPPP00PPPP0000s0P",
    "P0s0000PPPP00PPPP000000P",
    "P0s000000000000000000s0P",
    "P0s00000000000000000000P",
    "P0s000000000000000000s0P",
    "P0s00000000000000000000P",
    "P0s0000PPPP00PPPP0000s0P",
    "P000000PPPP00PPPP000000P",
    "P00PPs0s0s0s0s0s0s0PPs0P",
    "P0sPP00000000000000PP00P",
    "PPPPPPPPPPPPPPPPPPPPPPPP"
]
MAPA2 = [
    "PPPPPPPPPPPPPPPPPPPPPPPP",
    "Ps000s00000PP00000s000sP",
    "P0s0s000000PP000000s0s0P",
    "P00s0000000PP0000000s00P",
    "P0s0s000000PP000000s0s0P",
    "Ps000s000000000000s000sP",
    "PPPPPPP0000000000PPPPPPP",
    "PPPPPPP0000000000PPPPPPP",
    "Ps000s000000000000s000sP",
    "P0s0s000000PP000000s0s0P",
    "P00s0000000PP0000000s00P",
    "P0s0s000000PP000000s0s0P",
    "Ps000s00000PP00000s000sP",
    "PPPPPPPPPPPPPPPPPPPPPPPP"
]
MAPA3 = [
    "PPPPPPPPPPPPPPPPPPPPPPPP",
    "P00s0000000000000000s00P",
    "P0s0s00000000000000s0s0P",
    "Ps000s000PPPPPP000s000sP",
    "P00PP0000PPPPPP0000PP00P",
    "P00PP00000000000000PP00P",
    "Pss000000000000000000ssP",
    "Pss000000000000000000ssP",
    "P00PP00000000000000PP00P",
    "P00PP0000PPPPPP0000PP00P",
    "Ps000s000PPPPPP000s000sP",
    "P0s0s00000000000000s0s0P",
    "P00s0000000000000000s00P",
    "PPPPPPPPPPPPPPPPPPPPPPPP"
]
MAPA4 = [
    'PPPPPPPPPPPPPPPPPPPPPPPP',
    'PPPPPPPPP000000PPP000PPP',
    'PPPPPPPPP0ss00s00P000PPP', 
    'PPPPPPPPP000000000000PPP', 
    'PPPPPPPPP00000P000000PPP', 
    'PPPPPPPPP00000P00P000PPP', 
    'PPPPPPPPP00000P00PP00PPP', 
    'PP000000000000P00PP00PPP', 
    'PP000000000000P00PP00PPP', 
    'PPPssPPPPPPPPPPs0PP00PPP', 
    'PPPPPPPPPPPPPPP00PP00PPP', 
    'PPPP00ss000000000PP00PPP', 
    'PPPP00s0000000000PPPPPPP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP'
]
MAPA5 =[
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'PPPPP00000P00000Ps0PPPPP', 
    'PPPPP00000P00000P00PPPPP', 
    'PPPPP00000000000000s00PP', 
    'PPPPP00000000000000000PP', 
    'PPPPP00000000000000000PP', 
    'PPPPP00000000000000000PP', 
    'PPPPPs00PPPPPPPPPPPP00PP', 
    'Pss00sss000000sssssP00PP', 
    'Pss00sss0000000ssssP00PP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP'
]
MAPA6 = [
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'PP000000PPPPPPPPPPPPPPPP', 
    'PP000ssss000PPPPPPPPPPPP', 
    'PP000ssss00PPPPPPPPPPPPP', 
    'PP0000000000000PPPPPPPPP', 
    'PP00000000000000000PPPPP', 
    'PP0000000000000P000PPPPP', 
    'PPPs00P0000000PPPP0PPPPP', 
    'PPP0s0P0000000000000ssPP', 
    'PPP0s0P0000000000000ssPP', 
    'PPP000PPPPP000PPPPPPPPPP', 
    'PPPPPPPPPPP00ss00PPPPPPP', 
    'PPPPPPPPPPP00ss00PPPPPPP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP'
    ]
MAPA7 = [
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'PPPPPPPP00PPPPPPPPPPPPPP', 
    'PPPPPs0P00P000000PPPPPPP', 
    'PPPPP00P00P000000PPPPPPP', 
    'PP00000P000000000PPPPPPP', 
    'PP00s00P00000000sP00PPPP', 
    'PP00PPPP000000000s00PPPP', 
    'PP00PPP0000000000000PPPP', 
    'PPs0PPP0000000000000PPPP', 
    'PP00PPP000P0000000s0PPPP', 
    'PP0000s000P000000P0000PP', 
    'PPs0000000P000000P0ss0PP', 
    'PPPPPPP000PPPPPPPPPssPPP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP'
    ]
MAPA8 = [
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'PPPPP000000ss0PPPPPPPPPP', 
    'PPPPP000000000s0000000PP', 
    'PPPPPPPPPPPP0000000000PP', 
    'PPPPPPPPPPPPs00PPPPPPPPP', 
    'PPs0000000000000000000PP', 
    'PP00000000000000000000PP', 
    'PPPPPPPPP0000000000000PP', 
    'PPPPPPPPP0000000000000PP', 
    'PPPPPPPPPPPP0000000000PP', 
    'PPPPPPPPPPPP0000000000PP', 
    'PPPPPPPPPPss0000000000PP', 
    'PPPPPPPPPPss0000000000PP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP'
    ]
MAPA9 = [
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'PPPPPPPPPPPPPPPPPPPP00PP', 
    'P0000PPPPPPPPPPPPPPP00PP', 
    'P000000000000000s00P00PP', 
    'P000000000000000P00P00PP', 
    'P0000P0000000000P00P00PP', 
    'P0000PP000000000000000PP',
    'PP00PPP00000000000s000PP', 
    'PP00s00000000000000000PP', 
    'PPs0s00000000000000s00PP', 
    'PP00s0000P000000000PPPPP', 
    'PPPPPPPPPP000000000sPPPP', 
    'PPPPPPPPPP0s0s0s0s0sPPPP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP'
    ]
MAPA10 = [
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'Pssss0PPPPPPsssPPPPPPPPP', 
    'P00sss0PPPPPsssPPPPPPPPP', 
    'PPPPsssPPPPP0000000000PP', 
    'PPPPP00000000000000000PP', 
    'PPPPP00000000000000000PP', 
    'Ps00000000000000000000PP', 
    'P000000000000000000000PP', 
    'PsssPP0000000000000000PP', 
    'PPPPPP0000000000000000PP', 
    'Ps00sss000000000000000PP', 
    'Ps00sss0000P0000000000PP', 
    'PPPPPPPPPPPP000sssss00PP', 
    'PPPPPPPPPPPPPPPPPPPPPPPP'
    ]
MAPA11 = [
    'PPPPPPPPPPPPPPPPPPPPPPPP', 
    'P00000s00ss0s00s0s0s00sP', 
    'P0s0s0s0s00s0s0s0000000P', 
    'P00s0s0s000000s00s00000P', 
    'P000s0000000000000000s0P', 
    'P00s00000000000000000s0P', 
    'Ps0000000000000000000s0P', 
    'P00s0s000000000000000s0P', 
    'Pss000000000000000000s0P', 
    'P00000000000000000000s0P', 
    'Ps00s0000000000000000s0P', 
    'Ps00s000000000000000000P', 
    'P00000ssssss00000000ss0P', 
    'PPPPPPPPPPPPPPPPPPPPPPPP'
]
LISTA_MAPAS = [MAPA1, MAPA2, MAPA3, MAPA4, MAPA5, MAPA6, MAPA7, MAPA8, MAPA9, MAPA10, MAPA11]

# CARACTERISTICAS JOGADOR
# Dimensões do jogador
LARGURA_JOGADOR, ALTURA_JOGADOR = TAMANHO_TILE, TAMANHO_TILE
# Intervalos para ações
EVENTO_INTERVALO_ATAQUE = pygame.USEREVENT + 1
INTERVALO_ATAQUE = 330
# CARACTERISTICAS INIMIGO
VIDA_INIMIGO = 2
# Dimensoes do Inimigo
LARGURA_INIMIGO, ALTURA_INIMIGO = TAMANHO_TILE * 0.85, TAMANHO_TILE * 0.85
# Intervalo para ações
EVENTO_INTERVALO_DANO = pygame.USEREVENT + 2
INTERVALO_DANO = 1000
EVENTO_ESPADA = pygame.USEREVENT + 3
TEMPO_ESPADA = 10000
    