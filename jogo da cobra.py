import pygame
import random

# 1. Inicialização
pygame.init()

# 2. Configurações Globais
largura = 800
altura = 600
tamanho_bloco = 20
velocidade = 15

# 3. Definição de Cores 
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (213, 50, 80)
VERDE = (0, 255, 0)

# 4. Configuração da Tela e Relógio
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobra')
relogio = pygame.time.Clock()

def jogar():
    x, y = largura // 2, altura // 2  # Posição inicial
    dx, dy = 0, 0                      # Velocidade inicial
    corpo_snake = [[x, y]]
    comprimento = 1
    
    # Gera a primeira comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -tamanho_bloco, 0
                elif evento.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = tamanho_bloco, 0
                elif evento.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -tamanho_bloco
                elif evento.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, tamanho_bloco

        # Atualiza a posição da cabeça
        x += dx
        y += dy
        
        # Lógica de morte (paredes ou corpo)
        if x < 0 or x >= largura or y < 0 or y >= altura or [x, y] in corpo_snake[:-1]:
            rodando = False

        corpo_snake.append([x, y])
        
        # Verifica se comeu
        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento += 1
        
        if len(corpo_snake) > comprimento:
            del corpo_snake[0]

        # Desenho
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        for bloco in corpo_snake:
            pygame.draw.rect(tela, VERDE, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])
        
        pygame.display.flip()
        relogio.tick(velocidade) # Usa a variável velocidade definida no topo

# Inicia o jogo
jogar()
pygame.quit()