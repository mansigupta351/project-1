# importing the library i.e; pygame 
import pygame
#importing random variable to describing random variable and system
import random
import sys

#initialising pygame so that it takes command of pygame properly
pygame.init()

#initialising the height and width of the box 
WIDTH = 800
HEIGHT = 600

#deciding the color of blocks,text,backgroundcolor
RED = (255 , 0,0)
BLUE = (0 ,0 ,255)
black = (0 ,0, 0)
BACKGROUND_COLOR = (11,238,207)

#deciding the size of block of player
player_size = 50
player_pos = [WIDTH/2 ,HEIGHT-2*player_size]

#deciding the size of block of enemy
enemy_size = 50
enemy_pos = [random.randint(0 ,WIDTH-enemy_size) , 0]
enemy_list = [enemy_pos]

#speed of droping of blue block
SPEED = 10

#initialisg the game window by taking height and width mention above
window = pygame.display.set_mode((WIDTH , HEIGHT)) 

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

#defining the level which helps in defining the speed of blue block
def set_level(score ,SPEED):
    if score < 20:
        SPEED = 5
    elif score < 40:
        SPEED = 8
    elif score < 60:
        SPEED = 10
    else :
        SPEED = 15
    return SPEED
    
#defing the droping of enemies
def drop_enemies(enemy_list):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0 , WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos ,y_pos])

#defining the structure of enemy
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(window ,BLUE ,(enemy_pos[0],enemy_pos[1] , enemy_size , enemy_size))


#updating the position of enemy
def update_enemy_positions(enemy_list,score):
    for idx ,enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return score


# define the collision of enemy and player
def collision_check(enemy_list , player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos,player_pos):
            return True
    return False

#detect the collision
def detect_collision(player_pos ,enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
    	if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
            return True
    return False

#initialising the while loop to run the program
while not game_over:
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_RIGHT:
                x += 5

            player_pos = [x,y]

    window.fill(BACKGROUND_COLOR)
   
    #calling of the above functions
    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list,score)
    SPEED = set_level(score ,SPEED)
    text = "score:" + str(score)
    label = myFont.render(text , 1, black) 

    window.blit(label , (WIDTH -200 , HEIGHT-40))
    
    if collision_check(enemy_list, player_pos):
        game_over = True
        break

    draw_enemies(enemy_list)

    pygame.draw.rect(window ,RED ,(player_pos[0],player_pos[1] , player_size , player_size))

    clock.tick(30)
    
    pygame.display.update()
   
print(f" your score is {score}")
