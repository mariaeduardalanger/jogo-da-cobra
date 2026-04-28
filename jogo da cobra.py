import pygame
import random

# Inicialização
pygame.init()
largura, altura = 800, 600
tamanho_bloco = 20
PRETO, BRANCO, VERMELHO, VERDE = (0,0,0), (255,255,255), (213,50,80), (0,255,0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobra - Reiniciável')
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 25)

def mostrar_pontos(p):
    valor = fonte.render(f"Pontos: {p}", True, BRANCO)
    tela.blit(valor, [10, 10])

def jogar():
    # Variáveis iniciais
    x, y = largura // 2, altura // 2
    dx, dy = 0, 0
    corpo_snake = [[x, y]]
    comprimento = 1
    velocidade = 15
    
    comida_x = random.randrange(0, largura - tamanho_bloco, tamanho_bloco)
    comida_y = random.randrange(0, altura - tamanho_bloco, tamanho_bloco)

    game_over = False
    rodando = True

    while rodando:
        # TELA DE GAME OVER (A mágica acontece aqui)
        while game_over:
            tela.fill(PRETO)
            msg = fonte.render("Você perdeu! Pressione R para Reiniciar ou Q para Sair", True, VERMELHO)
            tela.blit(msg, [largura // 6, altura // 3])
            mostrar_pontos(comprimento - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        rodando = False
                        game_over = False
                    if evento.key == pygame.K_r:
                        jogar() # Chama a função novamente (Recursão)

        # CONTROLES NORMAIS
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT and dx == 0: dx, dy = -tamanho_bloco, 0
                elif evento.key == pygame.K_RIGHT and dx == 0: dx, dy = tamanho_bloco, 0
                elif evento.key == pygame.K_UP and dy == 0: dx, dy = 0, -tamanho_bloco
                elif evento.key == pygame.K_DOWN and dy == 0: dx, dy = 0, tamanho_bloco

        # LÓGICA DE MOVIMENTO
        x += dx
        y += dy
        
        # COLISÕES
        if x < 0 or x >= largura or y < 0 or y >= altura or [x, y] in corpo_snake[:-1]:
            game_over = True

        corpo_snake.append([x, y])
        if x == comida_x and y == comida_y:
            comida_x = random.randrange(0, largura - tamanho_bloco, tamanho_bloco)
            comida_y = random.randrange(0, altura - tamanho_bloco, tamanho_bloco)
            comprimento += 1
        
        if len(corpo_snake) > comprimento:
            del corpo_snake[0]

        # DESENHO
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])
        for bloco in corpo_snake:
            pygame.draw.rect(tela, VERDE, [bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])
        
        mostrar_pontos(comprimento - 1)
        pygame.display.flip()
        relogio.tick(velocidade)

jogar()
pygame.quit()
