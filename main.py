import pygame
import math
import maca_pygame

# pygame setup
pygame.init()
som_comer = pygame.mixer.Sound("soundeffects/coin.mp3")
som_game_over = pygame.mixer.Sound("soundeffects/gameover.mp3")
pygame.mixer.music.load("music/ambience_nogap.mp3")
pygame.mixer.music.play(-1)
width = 720
height = 540
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height())
direcao = pygame.Vector2(0, 0)
vector_body = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)
counter = 0


spawn_apple = maca_pygame
tick_a = 0
tick_b = 0
snake_body = [player_pos]


block_size = 30
grid_x = []
grid_y = []
counter =0

number_colunms = math.ceil(width/block_size)
number_lines = math.ceil(height/block_size)

for x in range(0, number_colunms):
    grid_x.append(x)
    print(x)

for y in range(0, number_lines):
    grid_y.append(y)

maca_coletadas = 0
posicao_x = width/2
posicao_y = height/2
maca_pos = spawn_apple.spawn_maca(number_colunms, number_lines, block_size)
game_over = False
fonte = pygame.font.SysFont("arial", 40)
fonte_maca = pygame.font.SysFont("arial", 20) 
texto_surface_gameover = fonte.render("Game Over!", True, "White")
texto_surface_recomeçar = fonte.render("Pressione R para Recomeçar", True, "White")
pygame.display.set_caption("Snake Game")



while running:
    texto_surface_maca = fonte_maca.render(f"Maças: {maca_coletadas}", True, "White")
    tick_b = pygame.time.get_ticks()
    screen.fill("black")
    for i in range(0, len(snake_body)):
        pygame.draw.rect(screen, 'White', [snake_body[i].x, snake_body[i].y, block_size, block_size])



    teste = pygame.draw.circle(screen, 'Red', (maca_pos), block_size/2)
    screen.blit(texto_surface_maca, (width/1.2, height/10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                if direcao.y != 1:
                    direcao = pygame.Vector2(0, -1)

            if event.key == pygame.K_s:
                if direcao.y != -1:
                    direcao = pygame.Vector2(0, 1)

            if event.key == pygame.K_a:
                if direcao.x != 1:
                    direcao = pygame.Vector2(-1, 0)

            if event.key == pygame.K_d:
                if direcao.x != -1:
                    direcao = pygame.Vector2(1, 0)

            if event.key == pygame.K_r:

                game_over = False
                snake_body = [player_pos]
                direcao = pygame.Vector2(0, 0)
                maca_coletadas = 0
                pygame.mixer.music.play()



    if game_over == False:

        if tick_b - tick_a > 200:
            posicao_x += direcao.x*block_size
            posicao_y += direcao.y*block_size
            tick_a = tick_b
            snake_body.insert(0, vector_body)
            counter = 0

            snake_body.pop(-1) #remove pop and keeps growing

            for pos in snake_body:
                counter += 1
                if counter >1 and len(snake_body)>2:
                    if snake_body[0].x == pos.x and snake_body[0].y == pos.y:
                        som_game_over.play()
                        game_over = True
                        print("Você perdeu")
                        pygame.mixer.music.stop()

            
            if snake_body[0] == maca_pos:
                som_comer.play()
                snake_body.insert(0, vector_body)
                maca_pos = spawn_apple.spawn_maca(number_colunms, number_lines, block_size)
                maca_coletadas += 1


    if posicao_x > number_colunms*block_size:
        posicao_x = 0

    elif posicao_x < 0:
        posicao_x = (number_colunms-1) * block_size

    elif posicao_y > number_lines*block_size:
        posicao_y = 0

    elif posicao_y < 0:
        posicao_y = (number_lines-1) * block_size

    vector_body = pygame.Vector2(posicao_x, posicao_y)

    if game_over == True:
        screen.blit(texto_surface_gameover, (width/3, height/2))
        screen.blit(texto_surface_recomeçar, (width/5, height/1.5))


    pygame.display.flip()


    clock.tick(60)

pygame.quit()