# import libraries
import pygame
import random


#initialise pygame
pygame.init()

#game window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 550

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("GAME")

# set frame rate
clock = pygame.time.Clock()
FPS = 60

# game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0


# define colours
WHITE = (255, 255, 255)

#load images 
cute_image = pygame.image.load("cute.png").convert_alpha()
bg_image = pygame.image.load("bg.png").convert_alpha()
bg = pygame.transform.scale(bg_image, (800, 550))
platform_png = pygame.image.load("platform.png").convert_alpha()

# function for drawing the background
def draw_bg(bg_scroll):
    screen.blit(bg,(0,0 + bg_scroll))
    screen.blit(bg,(0, -550 + bg_scroll))

# player class
class Player():
    def __init__(self,x,y):
        # self.image = cute_image
        self.image = pygame.transform.scale(cute_image, (100, 100))
        self.width = 40
        self.height = 40
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
            dx = -15
            self.flip = True
        if key[pygame.K_RIGHT]:
            dx = 15
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


        # check collision with the ground
        if self.rect.bottom + dy > SCREEN_HEIGHT:
            dy = 0
            self.vel_y = - 20

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
        screen.blit(pygame.transform.flip(self.image, self.flip, False),(self.rect.x - 30,self.rect.y - 30))
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        
# platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_png,(width,10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

    def update(self,scroll):
        #update platfrom vertical position
        self.rect.y += scroll


# player instance
jump_1 = Player(SCREEN_WIDTH//2,SCREEN_HEIGHT -150)
    
#create sprite group
# operate like a list
platform_group = pygame.sprite.Group() 

# create start plataform
platform = Platform(SCREEN_WIDTH//2 - 80,SCREEN_HEIGHT -50, 150)
platform_group.add(platform)

#game loop
run = True 
while run:
   
   clock.tick(FPS)
   
   scroll = jump_1.move()
   
    
   #draw background 
   bg_scroll += scroll
   if bg_scroll >= 550:
       bg_scroll = 0
   draw_bg(scroll)

#generate platafroms
if len(platform_group) < MAX_PLATFORMS:
   platform = Platform(SCREEN_WIDTH//2 - 80,SCREEN_HEIGHT -50, 150)
   platform_group.add(platform)

   print(len(platform_group))

# update platforms
   platform_group.update(scroll)

   #draw sprites
   platform_group.draw(screen)
   jump_1.draw()
   
   #event handler
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

   #update display window
   pygame.display.update()




pygame.quit()