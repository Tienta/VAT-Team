import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

player_size = 73
object_size = 32

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('KONG Skull Island')
clock = pygame.time.Clock()


player_Img = pygame.image.load('image/10.png')
object_Img1 = pygame.image.load('image/mario.png')
object_Img2 = pygame.image.load('image/square.png')
object_Img3 = pygame.image.load('image/gate.png')
list_Img = (object_Img1,object_Img2,object_Img3)



#######
def objects(object_Img,objectx, objecty):
    gameDisplay.blit(object_Img, [objectx, objecty])


#######


def player(x, y):
    gameDisplay.blit(player_Img, (x, y))


def check_map(y):
    if y > display_width - player_size or y < 0:
        return False
    return True


def game_loop():

    ### vi tri cua Player
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    dx = 0
    player_heath = 3
    # thuoc tinh cua Object(diem bat dau: x va y, speed)
    object_startx = random.randrange(10, (display_width - object_size))
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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -15
                if event.key == pygame.K_RIGHT:
                    dx  = 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    dx = 0

        ## Dieu Kien
        next_x = x + dx
        if  check_map(next_x):
            x += dx
        if object_starty > display_height:
            object_starty = - 100
            object_startx = random.randrange(10, display_width -  object_size)
        ### Check THua
        if  object_starty > display_height - 5 and object_startx != x and object_starty != y:
            player_heath -= 1
            print(player_heath, "<3")
            if player_heath == 0:
                gameExit = True
                print("YOU LOSE")
        # draw background
        gameDisplay.fill(white)

        ## Draw Cac su kien game

        objects(object_Img1,object_startx, object_starty)
        object_starty += object_speed
        player(x, y)


        pygame.display.update()
        clock.tick(60)



game_loop()
pygame.quit()
quit()