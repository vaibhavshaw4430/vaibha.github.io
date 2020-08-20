import pygame
import sys
import random 
pygame.init()

WIDTH = 800
HEIGHT = 600
RED=(255,0,0)
BLUE = (0,0,255)
Yellow = (255,255,0)
BACKGROUND_COLOR = (0,0,0)
player_size= 50
player_pos = [WIDTH/2,HEIGHT-(2*player_size)]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size),0]
enemy_list = [enemy_pos]
speed=10
score = 0
screen = pygame.display.set_mode((WIDTH,HEIGHT))
game_over=False
clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace",35)


def set_level(score,speed):
	if score<20:
		speed = 8
	elif score<40:
		speed = 12
	elif score<60:
		speed=15
	else:
		speed=18
	return(speed)

# def show_go_screen(myFont,text,Yellow):
# 	background=myFont.render(text,1,Yellow)
#     screen.blit(background,(400,300))
#     draw_text(screen, "SHMUP!", 64, WIDTH / 2, HEIGHT / 4)
#     draw_text(screen, "Arrow keys move, Space to fire", 22,
#               WIDTH / 2, HEIGHT / 2)
#     draw_text(screen, "Press a key to begin", 18, WIDTH / 2, HEIGHT * 3 / 4)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.KEYUP:
#                 waiting = False


def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list)<10 and delay < 0.1:
		x_pos = random.randint(0,WIDTH-enemy_size)
		y_pos = 0
		enemy_list.append([x_pos,y_pos])


def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
			pygame.draw.rect(screen,BLUE,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))


def update_enemy_positions(enemy_list,score):
	for idx,enemy_pos in enumerate(enemy_list):
		if enemy_pos[1]>=0 and enemy_pos[1]<HEIGHT:
			enemy_pos[1]+=speed
		else:
			enemy_list.pop(idx)
			score +=1
	return(score)

def collision_check(enemy_list,player_pos):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos,player_pos):
			# text1 = "Your Score : " + str(score)
			# label1=myFont.render(text1,1,Yellow)
			# screen.blit(label1,(WIDTH/2,HEIGHT/2))
			return True
	return False



def detect_collision(player_pos,enemy_pos):
	p_x=player_pos[0]
	p_y=player_pos[1]

	e_x=enemy_pos[0]
	e_y=enemy_pos[1]

	if (e_x>=p_x and e_x<p_x+player_size) or (p_x>=e_x and p_x<e_x+enemy_size):
		if(e_y>=p_y and e_y<p_y+player_size) or (p_y>=e_y and p_y<e_y+enemy_size):
			return True
	return False


while not game_over:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()
		
		if event.type == pygame.KEYDOWN:

			x=player_pos[0]
			y=player_pos[1]

			if event.key == pygame.K_LEFT:
				x-=player_size
			elif event.key == pygame.K_RIGHT:
				x+=player_size
			player_pos = [x,y]

	screen.fill(BACKGROUND_COLOR)
	if detect_collision(player_pos,enemy_pos):
		game_over=True
		#screen.blit(label,(WIDTH/2,HEIGHT/2))

	drop_enemies(enemy_list)
	
	score = update_enemy_positions(enemy_list,score)

	speed = set_level(score,speed)

	text = "Score : " + str(score)
	label=myFont.render(text,1,Yellow)

	screen.blit(label,(WIDTH-250,HEIGHT-40))
	# screen.blit(label,(WIDTH/2,HEIGHT/2))

	#print(score)

	if collision_check(enemy_list,player_pos):
		game_over = True
		#show_go_screen(myFont,text,Yellow)
		# screen.blit(label,(WIDTH/2,HEIGHT/2))
		break	

	draw_enemies(enemy_list)
	
	
	clock.tick(30)

	pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))
	
	pygame.display.update()







