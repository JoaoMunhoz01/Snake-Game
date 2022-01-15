import pygame, random
from pygame.locals import *

#Renderizar a maça em uma posição multipla de 10
def on_grid_random():
    x = random.randint(0,790)
    y = random.randint(0,790)
    return (x//10 * 10, y//10 * 10)

#Colisões
def collision(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

#Direções 
UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3

#Placar
count = 0

pygame.init()
#Declarando o Tamanho da interface do game 
screen = pygame.display.set_mode((800,800))

#Declarando o nome do game 
pygame.display.set_caption('Snake')

#Declarando o Tamanho inicial  da cobrinha
snake = [(200, 200), (210, 200), (220, 200)] 
snake_skin = pygame.Surface((10,10)) 

#Cor da Cobrinha
snake_skin.fill((255,255,255))

#Tamanho da Maça 
apple = pygame.Surface((10,10))

#Posição da maça
apple_pos = on_grid_random()

#Cor da Maça
apple.fill((255,0,0))

#Direção inicial
my_direction = LEFT

#Limitar velocidade
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 24)

game_over = False
while not game_over:
    clock.tick(20) #Limitar velocidade
    
    for event in pygame.event.get():
        if event.type == QUIT: #Fechar Jogo
            pygame.quit()
        
        if event.type == KEYDOWN:#Movimentação da cobrinha
            
            if event.key == K_UP:
                if my_direction != DOWN :
                    my_direction = UP
                
            if event.key == K_DOWN:
                if my_direction != UP :
                    my_direction = DOWN
            
            if event.key == K_LEFT:
                if my_direction != RIGHT :
                    my_direction = LEFT
            
            if event.key == K_RIGHT:
                if my_direction != LEFT :
                    my_direction = RIGHT
                
    #Comer a maça
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        count = count+1
        print(count)
        
    #Verificação se a cobrinha bateu na borda
    if snake[0][0] == 800 or snake[0][1] == 800 or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
        break
    
    #Verificação se a cobrinha bateu nela mesma
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
            break

    if game_over:
        break
        
    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

            
    #Logica da movimentação       
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
        
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
        

    #Cor da tela 
    screen.fill((0,100,0))
    
    #mostrar a maça
    screen.blit(apple, apple_pos)
    
    placar = font.render('Pontos %s' % (count), True, (255,255,255))
    placar_pos = placar.get_rect()
    placar_pos.topleft = (600 - 125, 25)
    screen.blit(placar, placar_pos)
    
    
    #Mostrar a cobrinha
    for pos in snake:
        screen.blit(snake_skin, pos)
    
    pygame.display.update()