import pygame
from sys import exit
from random import randrange
from random import randint
class meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('elements/meteorv02.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom =(meteor.x,randrange(height + random_y)))
        self.speed = 7

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < randoffcenter:
            self.rect.x = width
            self.rect.y = randrange(height)

class meteor1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('elements/meteorv03.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom =(meteor.x,randrange(height + random_y)))
        self.speed = 7

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < randoffcenter - 150:
            self.rect.x = width
            self.rect.y = randrange(height)

class meteor2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('elements/meteorv04.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom =(meteor.x,randrange(height + random_y)))
        self.speed = 7

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < randoffcenter - 100:
            self.rect.x = width
            self.rect.y = randrange(height)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()    
        self.image = pygame.image.load("player/rocket01.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom =(meteor.x,height))
    
    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.centerx = mouse_x
        self.rect.centery = mouse_y

def display_score():
    current_time = int(pygame.time.get_ticks()/1000)
    score = Score_font.render(f'{current_time}',False,'cornsilk2')
    score_rect = score.get_rect(center = (height/3, width/2) )
    screen.blit(score,score_rect)

pygame.init()
width = 1080
meteor.x = width
height = 400
screen = pygame.display.set_mode((1080,566))
pygame.display.set_caption('Spacedebris')
clock = pygame.time.Clock()
background_font = pygame.font.Font('fonts/Major_Mono_Display/MajorMonoDisplay-Regular.ttf',100)
Score_font = pygame.font.Font('fonts/Major_Mono_Display/MajorMonoDisplay-Regular.ttf',40)
running = True
random_y = randint(120, 140)
randoffcenter = randint(-100, 0)

all_sprites = pygame.sprite.Group()

player_sprite = Player()
meteor_sprite = meteor()
meteor1_sprite = meteor1()
meteor2_sprite = meteor2()
all_sprites.add(meteor_sprite, meteor1_sprite, meteor2_sprite)

background_surface = pygame.image.load('background/bg.jpg')
background_text = background_font.render('SPACEDEBRIS',False,'cornsilk2')

meteor_surface = pygame.image.load('elements/meteorv02.png')
meteor_surface1 = pygame.image.load('elements/meteorv03.png')
meteor_surface2 = pygame.image.load('elements/meteorv04.png')

    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background_surface,(0,0))
    screen.blit(background_text,(125,200))

    all_sprites.update()
    all_sprites.draw(screen)
    player_sprite.update()
    screen.blit(player_sprite.image, player_sprite.rect)
    display_score()

    if pygame.sprite.spritecollideany(player_sprite, all_sprites):
         running = False
         screen.fill('black')

    pygame.display.update()
    clock.tick(60)


# Devlog : 30/03 add start screen and end screens