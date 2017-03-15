import pygame, sys
import time
import random
from pygame import Rect
pygame.init()

## set
FPS = 60 ## 60 hinh/
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
brown = ( 241, 175, 0)

player_width = 73
player_height = 87
object_width = 32
object_height = 32

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('KONG Skull Island')
clock = pygame.time.Clock()

### LOAD IMaGe
background_Img = pygame.image.load('image/background3s.jpg')
background_Img1 = pygame.image.load('image/background4.png')
logo_intro = pygame.image.load('image/logointro.png')
player_Img = pygame.image.load('image/10.png')
object_Img1 = pygame.image.load('image/mario.png')
lose_Img = pygame.image.load("image/logointro.png")

### Load Sound
pygame.mixer.init()
# eat_sound = pygame.mixer.Sound("")
# crash_sound = pygame.mixer.Sound("")
lose_sound = pygame.mixer.Sound("sound/losesound1.wav")
fall_sound = pygame.mixer.Sound("sound/sound_fall.wav")




## item cua game
def objects(object_Img,objectx, objecty):
    gameDisplay.blit(object_Img, [objectx, objecty])

### diem cua game
font_name = ("font/breakaway.ttf")
def player_count(count_game):
    # font = pygame.font.SysFont(None, 25)

    font = pygame.font.Font(font_name, 25)
    text = font.render("COUNT: " + str(count_game), True, brown)
    gameDisplay.blit(text, (650, 10))

## turn cua nguoi choi
def player_heaths(player_heath):
    # font = pygame.font.SysFont(None, 25)
    font = pygame.font.Font(font_name, 25)
    text = font.render("HEATH: " + str(player_heath), True, brown)
    gameDisplay.blit(text, (50, 10))

## ve player
def player(x, y):
    gameDisplay.blit(player_Img, (x, y))

## check player in MAP
def check_map(y):
    if y > display_width - player_width or y < 0:
        return False
    return True

## hien thi khi Thua
def lose():
    # font = pygame.font.SysFont(None, 100)
    font = pygame.font.Font(font_name, 100)
    text = font.render(" YOU LOSE", True, brown)
    gameDisplay.blit(text,(display_width* 0.27, display_height * 0.3))
    lose_sound.play()
    pygame.display.update()
    time.sleep(5) ## play again (s)
    game_loop()
def get_rect(x,y,width,height):
    return Rect(x,y,width,height)

def game_loop():

    ### vi tri cua Player
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    dx = 0
    player_heath = 3
    count_game = 0

    # thuoc tinh cua Object(diem bat dau: x va y, speed)
    object_startx = random.randrange(10, (display_width - object_width))
    object_starty = -display_height
    object_speed = 8



    # dieu khien Player
    gameExit = False

    #### LOOP CODE
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                # gameExit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -15
                elif event.key == pygame.K_RIGHT:
                    dx  = 15
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0

        ## Dieu Kien
        next_x = x + dx
        if  check_map(next_x):
            x += dx
        if object_starty > display_height:
            object_starty = - 100
            object_startx = random.randrange(10, display_width - object_width)





        ## check eat
        Rect1 = get_rect(x,y, player_width,player_height)
        Rect2 = get_rect(object_startx,object_starty,object_width,object_height)
        print(Rect1.colliderect(Rect2))
        if Rect1.colliderect(Rect2) == 1:
            print("AAA")
            count_game += 1

        ## thua
        if  object_starty > display_height -5:
            print("ssss")
            player_heath -= 1
            fall_sound.play()
            if player_heath == 0:
                player_heaths(player_heath)
                lose()
                lose_sound.play()




        # draw background
        gameDisplay.fill(white)

        gameDisplay.blit(background_Img,(0, 0))

        ## Draw Cac su kien game
        # collision = check_coll(x, y, player_width, player_height, object_startx, object_starty, object_width,object_height, count_game)
        player(x, y)
        objects(object_Img1,object_startx, object_starty)

        object_starty += object_speed


        player_heaths(player_heath)
        player_count(count_game)

        gameDisplay.blit(background_Img1, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

game_loop()
pygame.quit()
quit()