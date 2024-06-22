import pygame
import random

def aumentar_cobra(lista_cobra: list):
    for e in lista_cobra:

        pygame.draw.rect(app, (0, 200, 0), (e[0], e[1] , 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, cobra_x, cobra_y, lista_cabeca, lista_cobra, maca_x, maca_y, morreu
    pontos =  0
    comprimento_inicial = 5
    cobra_x = int(largura / 2)
    cobra_y = int(altura / 2)
    lista_cabeca = []
    lista_cobra = []
    maca_x = random.randint(20, 720)
    maca_y = random.randint(20, 520)
    morreu = False

lista_cobra = []
comprimento_inicial = 5
morreu = False

pygame.init()

largura = 800
altura = 600

app = pygame.display.set_mode([largura, altura])
fonte = pygame.font.SysFont('georgia', 30, True, True)
pontos = 0

gameLoop = True

pygame.display.set_caption("Snake Game")
relogio = pygame.time.Clock()

cobra_x = largura // 2
cobra_y = altura // 2
speed = 3

mover_x = 0
mover_y = 0
    
maca_x = random.randint(20, 720)
maca_y = random.randint(20, 520)

while gameLoop:      
   relogio.tick(60)
   app.fill((255, 255, 255))
   mensagem = f"Score: {pontos}"
   texto_formatado = fonte.render(mensagem, True, "black")
   
   for event in pygame.event.get():

      if event.type == pygame.QUIT:
          gameLoop = False
       
      elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
               if mover_x == speed:
                   pass
               else:
                   mover_x = -speed
                   mover_y = 0

           elif event.key == pygame.K_d:
               if mover_x == -speed:
                   pass
               else:    
                  mover_x = speed
                  mover_y = 0

           elif event.key == pygame.K_w:
               if mover_y == speed:
                   pass
               else:
                   mover_y = -speed
                   mover_x = 0

           elif event.key == pygame.K_s:
               if mover_y == -speed:
                   pass
               else:
                   mover_y = speed
                   mover_x = 0
   
   cobra_x += mover_x
   cobra_y += mover_y

   if cobra_x >= largura:
       cobra_x = 0
   if cobra_x < 0:
       cobra_x = largura

   if cobra_y >= altura:
       cobra_y = 0
   if cobra_y < 0:
       cobra_y = altura
    
   cobra = pygame.draw.rect(app, (0, 200, 0), (cobra_x, cobra_y, 20, 20))
   maca = pygame.draw.rect(app, (255, 0, 0), (maca_x, maca_y, 20, 20))

   if cobra.colliderect(maca):
       maca_x = random.randint(20, 720)
       maca_y = random.randint(20, 520)
       pontos += 1
       comprimento_inicial += 10

   cobra_cabeca = [cobra_x, cobra_y]
   if cobra_cabeca in lista_cobra[5:-1]:
        
        fonte2 = pygame.font.SysFont('arial', 25, True, True)
        mensagem = """Game Over! Pressione a tecla SPACE para jogar novamente."""
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        morreu = True

        while morreu:
            app.fill((255, 255, 255))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        reiniciar_jogo()
            app.blit(texto_formatado, (40, altura // 2))
            pygame.display.update()

   lista_cabeca = []
   lista_cabeca.append(cobra_x)
   lista_cabeca.append(cobra_y)
   lista_cobra.append(lista_cabeca)
   
   if len(lista_cobra) > comprimento_inicial:
        lista_cobra.pop(0)

   aumentar_cobra(lista_cobra)

   app.blit(texto_formatado, (100, 20))
   pygame.display.update()