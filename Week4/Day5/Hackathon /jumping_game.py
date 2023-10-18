# import libraries
import pygame, psycopg2, psycopg2.extras, os, json, random
from pygame import mixer

#initialise pygame
mixer.init()
pygame.init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 711

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GAME")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# load music and sounds
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1, 0.0) 
jump_fx = pygame.mixer.Sound('assets/jump.mp3')
jump_fx.set_volume(0.5)
death_fx = pygame.mixer.Sound('assets/death.mp3') 
death_fx.set_volume(0.5)

# game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0
game_over = False
data_high_score = {"name" : "player", "score" : 0 }
score =  0 
fade_counter = 0
high_score = score
if os.path.exists("scores.txt"):
    with open("scores.txt") as file:
       data_high_score = json.load(file)
else:
    high_score = 0

# connect with sql

# variables sql
DB_NAME = "score_data"
USER = "postgres" 
PASSWORD = "postgres" 
HOST = "localhost"
PORT = "5433"
connection = None

# start conection with sql
try:
    with psycopg2.connect(
        dbname = DB_NAME,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
        ) as connection:

        with connection.cursor(cursor_factory= psycopg2.extras.DictCursor) as cursor:
            
            #if table doesn't exist create one
            cursor.execute("drop table if exists scores")
            create_table = ''' create table scores(
                                id serial primary key,
                                name varchar (50) not null,
                                score int not null);'''
            cursor.execute(create_table)
            
            #inserting score to data
            insert_table = "insert into scores (name, score) values (%s, %s)"
            insert_values = (data_high_score["name"], data_high_score["score"])
            cursor.execute(insert_table, insert_values)
except Exception as e:
    print(f"Error: {e}")
finally:
    if connection is not None:
        connection.close()
print("MySQL connection is closed")

# define colours
WHITE = (251,236,254,255)
BLACK_ROCK = (19, 4, 35)
BG = (88,76,162,255)

# define font 
font_small = pygame.font.SysFont("Lucida Sans", 20)
font_big = pygame.font.SysFont("Lucida Sans", 24)

#load images 
cute_image = pygame.image.load("assets/cute.png").convert_alpha()
bg_image = pygame.image.load("assets/bg.png").convert_alpha()
bg = pygame.transform.scale(bg_image, (400, 711))
platform_png = pygame.image.load("assets/platform.png").convert_alpha()

# function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# function for drawing info panel
def draw_panel():
    pygame.draw.rect(screen, BG, (0, 0, SCREEN_WIDTH, 30))
    # pygame.draw.line(screen,WHITE,(0, 30),(SCREEN_WIDTH,30),2)
    draw_text("SCORE: "+ str(score), font_small, WHITE,8,8)

# function for drawing the background
def draw_bg(bg_scroll):
    screen.blit(bg,(0,0 + bg_scroll))
    screen.blit(bg,(0, -SCREEN_HEIGHT + bg_scroll))

# player class
class Player():
    def __init__(self,x,y):
        # self.image = cute_image
        self.image = pygame.transform.scale(cute_image, (100, 100))
        self.width = 40
        self.height = 58
        self.rect = pygame.Rect(0, 0,self.width, self.height)
        self.rect.center = (x,y)
        self.vel_y = 0
        self.flip = False

    def move(self):
        #reset variables
        scroll = 0
        dx = 0 
        dy = 0

        # process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx = -10
            self.flip = True
        if key[pygame.K_RIGHT]:
            dx = 10
            self.flip = False

        # gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # ensure player doesn"t go off the edge of the screen 
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.left + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        #check collision with the platflorms
        for platform in platform_group:
            #collision in the y direction
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if above the platform
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0 :
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = - 20
                        jump_fx.play()

        #check if the player has bounced to the top of the screen
        if self.rect.top <= SCROLL_THRESH:
            # if player is jumping
            if self.vel_y < 0:
                scroll = -dy

        #update rectangule position
        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x - 30,self.rect.y - 20))
        # pygame.draw.rect(screen, WHITE, self.rect, 2)
        
# platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width,moving):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_png,(width,60))
        self.moving = moving
        self.move_counter = random.randint(0, 50)
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(1, 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 


    def update(self,scroll):
        # moving platform side to side if it is a moving platform
        if self.moving == True:
            self.move_counter += 1
            self.rect.x += self.direction * self.speed

        #  change platform direction if it has moved fully or hit a wall
        if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right >SCREEN_WIDTH:
            self.direction *= -1
            self.move_counter = 0
    
        #update platform vertical position
        self.rect.y += scroll

        # check if the platform has gone off the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


# player instance
jump_1 = Player(SCREEN_WIDTH//2,SCREEN_HEIGHT -150)
    
#create sprite group
# operate like a list
platform_group = pygame.sprite.Group() 

# create start plataform
platform = Platform(SCREEN_WIDTH//2 - 80,SCREEN_HEIGHT - 50, 150, False)
platform_group.add(platform)

#game loop
run = True 
while run:
   
   clock.tick(FPS)

   if game_over == False:
        scroll = jump_1.move()
        
            
        #draw background 
        bg_scroll += scroll
        if bg_scroll >= SCREEN_HEIGHT:
            bg_scroll = 0
        draw_bg(scroll)

            #generate plataforms
        if len(platform_group) < MAX_PLATFORMS:
            p_w = random.randint(60, 80)
            p_x = random.randint(5, SCREEN_WIDTH - p_w)
            p_y = platform.rect.y - random.randint(80, 120)
            p_type = random.randint(1,2)
            if p_type == 1 and score > 500:
                p_moving = True
            else:
                p_moving = False
            platform = Platform(p_x, p_y, p_w,p_moving)
            platform_group.add(platform)

            print(len(platform_group))

        # update platforms
        platform_group.update(scroll)

        # update score
        if scroll > 0:
            score += scroll

        # draw line at previous high score 
        # pygame.draw.line(screen, WHITE, (0,score - data_high_score["score"] + SCROLL_THRESH),(SCREEN_WIDTH,score - high_score + SCROLL_THRESH),3)
        # draw_text("HIGH SCORE", font_small, WHITE, SCREEN_WIDTH - 90, score - high_score + SCROLL_THRESH)

        #draw sprites
        platform_group.draw(screen)
        jump_1.draw()

        draw_panel()
        
        #check game over
        if jump_1.rect.top > SCREEN_HEIGHT:
            game_over = True
            death_fx.play()
   else:
       if fade_counter < SCREEN_WIDTH:
           fade_counter += 10
           for y in range(0, 6, 2):
                pygame.draw.rect(screen, BLACK_ROCK, (0, y * 120, fade_counter, 120)) 
                pygame.draw.rect(screen, BLACK_ROCK, (SCREEN_WIDTH - fade_counter, (y+1) * 120, SCREEN_WIDTH,120 )) 
       else:
        draw_text("GAME OVER", font_big, WHITE, SCREEN_WIDTH//2 -50, 300)
        draw_text("SCORE: " + str(score), font_big, WHITE, SCREEN_WIDTH//2 - 42, 350)
        draw_text("PRESS SPACE TO PLAY AGAIN", font_big, WHITE, SCREEN_WIDTH//2 - 130, 400)
        #update high score
        if score > high_score:
            data_high_score["score"] = score
            with open("scores.txt", "w") as file:
                json.dump(data_high_score, file)     
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            # reset variables
            game_over = False
            score = 0
            scroll = 0
            fade_counter = 0
            # reposition jump_1
            jump_1.rect.center = (SCREEN_WIDTH//2,SCREEN_HEIGHT -150)
            # reset platforms
            platform_group.empty()
            # create start plataform
            platform = Platform(SCREEN_WIDTH//2 - 80,SCREEN_HEIGHT - 50, 150,False)
            platform_group.add(platform)

    
     



   #event handler
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score > high_score:
                data_high_score["score"] = score
                with open("scores.txt", "w") as file:
                    json.dump(data_high_score, file) 
            run = False

   #update display window
   pygame.display.update()




pygame.quit()