import pygame
import time
import random

pygame.init()
#Configuração de Tela
tela_largura = 800
tela_altura = 600
#Cores:
preto = (0,0,0)
branco = (255,0,0)
vermelho=(255,255,0)
#Configuração dos Blocos :
bloco_cor=(53,115,55)
#Configuração de Carro:
car_largura = 50
#Tela:
Tela_de_jogo=pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Corrida Maluca')
relogio = pygame.time.Clock()
#Carro e Fundo
car_Img=pygame.image.load('02a.png')
fund_img = pygame.image.load('back.jpg')
fund_img_intro=pygame.image.load('intro.jpg')
#Função de para contar so blocos projetados:
def blocos_projetados(count):
    font = pygame.font.SysFont(None,25)
    text = font.render('Pontos:'+str(count),True,preto)
    Tela_de_jogo.blit(text,(0,0))
#Função para Projetar coisas na Tela:
def pontos (p_x,p_y,p_w,p_h,color):
    pygame.draw.rect(Tela_de_jogo,color,[p_x,p_y,p_w,p_h])
#Função para Projetar o Carro na Tela :
def car(x,y):
    Tela_de_jogo.blit(car_Img, (x, y))
#Definições de Texto
def objetos_texto(texto, font):
    textSurface = font.render(texto, True, preto)
    return textSurface, textSurface.get_rect()
#Definições de Mensagem na Tela do Jogo :
def mensagem_tela(texto):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurd , TextReact = objetos_texto(texto,largeText)
    TextReact.center = (tela_largura/2),(tela_altura/2)
    Tela_de_jogo.blit(TextSurd,TextReact)
    pygame.display.update()
    time.sleep(2)
    game_loop()
def mensagens(texto):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurd , TextReact = objetos_texto(texto,largeText)
    TextReact.center = (tela_largura/5),(tela_altura/5)
    Tela_de_jogo.blit(TextSurd,TextReact)
    pygame.display.flip()

#Mensagem de Colissão:
def colissão():
    mensagem_tela('Fim de Jogo')
def Level():
    mensagens('Level-2')

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    intro=False
        Tela_de_jogo.fill(branco)
        Tela_de_jogo.blit(fund_img_intro, [0, 0])
        largeText = pygame.font.Font('freesansbold.ttf', 70)
        TextSurf, TextRect = objetos_texto("Corrida de Blocos", largeText)
        TextRect.center = ((tela_largura / 2), (tela_altura / 2))
        Tela_de_jogo.blit(TextSurf, TextRect)
        pygame.display.update()
        relogio.tick(15)



#Ate aqui foram definidas todas as funções Preload do Jogo
#A partir desse ponto as configurações vão ser inicalizadas de fato
def game_loop():
    pygame.mixer.music.load('01.mp3')
    pygame.mixer.music.play()
    x = (tela_largura * 0.45)
    y = (tela_altura  * 0.8)

    x_muda = 0

    ponto_inicioX = random.randrange(0,tela_largura)
    ponto_inicioY = -600
    ponto_velocidade = 4
    ponto_largura = 100
    ponto_altura = 100
    ponto_count = 1
    pontos_esquiva = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_muda = -10
                if event.key == pygame.K_RIGHT:
                    x_muda = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_muda = 0

        x += x_muda
        Tela_de_jogo.fill(branco)
        Tela_de_jogo.blit(fund_img,[0,0])
        #Aqui entram os pontos
        pontos(ponto_inicioX, ponto_inicioY, ponto_largura, ponto_altura, bloco_cor)

        ponto_inicioY += ponto_velocidade
        car(x,y)
        blocos_projetados(pontos_esquiva)

        if x > tela_largura - car_largura or x < 0:
            colissão()


        if ponto_inicioY > tela_altura:
            ponto_inicioY = 0 - ponto_altura
            ponto_inicioX = random.randrange(0,tela_largura)
            pontos_esquiva += 1
            ponto_velocidade +=1
            ponto_largura += (pontos_esquiva * 1.2)
        if pontos_esquiva > 2:
            Level()
        if y < ponto_inicioY + ponto_altura :
            print('Y Cross')

            if x > ponto_inicioX and x < ponto_inicioX + ponto_largura or x + car_largura > ponto_inicioX and x + car_largura < ponto_inicioX + ponto_largura:
                print('x crossover')
                colissão()

        pygame.display.update()
        relogio.tick(50)




#Funções Principais

game_intro()
game_loop()
pygame.quit()
quit()

