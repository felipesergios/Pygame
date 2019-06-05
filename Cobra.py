import pygame , random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 600))
fund_img_intro=pygame.image.load('intro.jpg')
FPS = pygame.time.Clock()

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10*10,y//10*10)
def colissão(c1,c2):
    return (c1[0]==c2[0] and c1[1]==c2[1])


def game_intro():
    intro = True
    pygame.mixer.music.load('01.mp3')
    pygame.mixer.music.play()
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    intro=False
        screen.blit(fund_img_intro, [0, 0])
        pygame.display.update()
        FPS.tick(15)




def fim_de_jogo():
    while True :
        game_over_font = pygame.font.Font('freesansbold.ttf', 75)
        game_over_screen = game_over_font.render('Game Over', True, (255, 255, 255))
        game_over_rect = game_over_screen.get_rect()
        game_over_rect.midtop = (600 / 2, 10)
        screen.blit(game_over_screen, game_over_rect)
        pygame.display.update()
        pygame.time.wait(50)
        pygame.mixer.music.load('01.mp3')
        pygame.mixer.music.play()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_1:
                        global game_over
                        game_over = False


#Variaveis de Uso
def game_loop():
    UP = 0
    RIGHT =1
    DOWN = 2
    LEFT = 3



    pygame.mixer.music.load('01.mp3')
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('COBRINHA FULL PISTOLA')



    ##Criando o Jogador Cobra
    cobra  = [(200,200),(210,200),(220,200)]
    cobra_skin = pygame.Surface((10,10))
    cobra_skin.fill((255,255,255))
    #Criando a maça
    maça_pos = (on_grid_random())
    maça = pygame.Surface((10,10))
    maça.fill((255,0,0))

    my_direction = LEFT
    FPS = pygame.time.Clock()


    font = pygame.font.Font('freesansbold.ttf', 18)
    score = 0

    game_over = False
    velocidade=10

    while not game_over:
        FPS.tick(velocidade)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    my_direction = UP
                if event.key == K_DOWN:
                    my_direction = DOWN
                if event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_RIGHT:
                    my_direction = RIGHT

        if colissão(cobra[0],maça_pos):
            maça_pos = on_grid_random()
            cobra.append((0,0))
            score=score+1
            velocidade=velocidade+2
        if cobra[0][0] == 600 or cobra[0][1]==600 or cobra[0][0]<0 or cobra[0][1]<0:
            game_over=True
            fim_de_jogo()
            break
        for i in range(1, len(cobra) - 1):
            if cobra[0][0]==cobra[i][0] and cobra[0][1]==cobra[i][1]:
                game_over=True
                break
        if game_over:
            break

        for i in range(len(cobra)-1,0,-1):
            cobra[i]=(cobra[i-1][0],cobra[i-1][1])


        if my_direction == UP:
            cobra[0]=(cobra[0][0],cobra[0][1]-10)
        if my_direction == DOWN:
            cobra[0]=(cobra[0][0],cobra[0][1]+10)
        if my_direction == RIGHT:
            cobra[0]=(cobra[0][0]+10,cobra[0][1])
        if my_direction == LEFT:
            cobra[0]=(cobra[0][0]-10,cobra[0][1])


        screen.fill((0,0,0))#Função para limpar a tela
        screen.blit(maça,maça_pos)#Função para blitar a maça (brotar a maça no tabuleiro)
        #Visor de Pontuação
        score_font = font.render('Pontos: %s' % (score), True, (255, 255, 255))
        score_rect = score_font.get_rect()
        score_rect.topleft = (600 - 120, 10)
        screen.blit(score_font, score_rect)
        ###
        velocidade_font = font.render('Velocidade: %s' % (velocidade), True, (255, 255, 0))
        velocidade_rect = score_font.get_rect()
        velocidade_rect.topleft = (450 - 120, 10)
        screen.blit(velocidade_font, velocidade_rect)


        for pos in cobra:
            screen.blit(cobra_skin,pos)
        pygame.display.update()
game_intro()
game_loop()

