import pygame
import time
import random
from pygame import Rect


pygame.init()

## set
FPS = 60 ## 60 hinh/
display_width = 800
display_height = 600
pause = False
black = (0, 0, 0)
white = (255, 255, 255)
brown = ( 241, 175, 0)


player_x = display_width * 0.45
player_y = display_height* 0.75
player_w = 73
player_h = 76

obj_w = 32
obj_h = 32
obj_x = random.randrange(10,(display_width - obj_w))
obj_y = -200

obj_w2 = 32
obj_h2 = 32
obj_x2 = random.randrange(5, 700)
obj_y2 = -300

boom_w = 42
boom_h = 40
boom_x = random.randrange(50,550)
boom_y = -300

boom_w2 = 42
boom_h2 = 40
boom_x2= random.randrange(100,650)
boom_y2 = boom_y - 300

heath_x = random.randrange(200,500)
heath_y = -display_height
heath_w = 40
heath_h = 47

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('KONG SKUll ISLAND')
clock = pygame.time.Clock()

### LOAD IMaGe
background_Img = pygame.image.load('image/background3.jpg')
background_Img1 = pygame.image.load('image/background4.png')
logo_intro = pygame.image.load('image/logointro1.jpg')
player_Img = pygame.image.load('kong/33s.png')
object_Img2 = pygame.image.load('banana/banana1.png')
heath_Img = pygame.image.load('image/heath_monkey.png')
## animation
object_Img = [
    pygame.image.load('king-kong/1.png'),
    pygame.image.load('king-kong/2.png'),
    pygame.image.load('king-kong/3.png'),
    pygame.image.load('king-kong/4.png'),
    pygame.image.load('king-kong/5.png'),
    pygame.image.load('king-kong/6.png'),
    pygame.image.load('king-kong/7.png'),
    pygame.image.load('king-kong/8.png'),
    pygame.image.load('king-kong/9.png'),
    pygame.image.load('king-kong/10.png'),
    pygame.image.load('king-kong/11.png'),
    pygame.image.load('king-kong/12.png'),
    pygame.image.load('king-kong/13.png'),
        ]
button_rs2 = pygame.image.load("image/button3b.png")
button_rs2_2 = pygame.image.load("image/button3_cl.png")
button_q2 = pygame.image.load("image/button4.png")
button_q2_2 = pygame.image.load("image/button4_click.png")
button_ = pygame.image.load("image/button0.png")
button_q = pygame.image.load("image/button1.png")
icon_pause = pygame.image.load("image/pause.png")
icon_play = pygame.image.load("image/play.png")
button_start0 = pygame.image.load("image/start0.png")
button_start1 = pygame.image.load("image/start1.png")
intro_Img = pygame.image.load("image/logointro1.jpg")
boom_Img = pygame.image.load("image/Bomb3.png")

### Load Sound
pygame.mixer.pre_init()
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("sound/coin2.wav")
lose_sound = pygame.mixer.Sound("sound/losesound1.wav")
fall_sound = pygame.mixer.Sound("sound/0024.wav")
coll_sound = pygame.mixer.Sound("sound/bomb2.wav")
up_sound = pygame.mixer.Sound("sound/0033.wav")
crash_sound = pygame.mixer.Sound("sound/Wave14.wav")
eat1_sound = pygame.mixer.Sound("sound/Wave36.wav")
neck_sound = pygame.mixer.Sound("sound/eats.wav")
die_sound = pygame.mixer.Sound("sound/Wave26.wav")
sound_ground = pygame.mixer.Sound("sound/4.wav")
sound_effect = pygame.mixer.Sound("sound/effect.wav")
sound_intro = pygame.mixer.Sound("sound/soundintro.wav")

class  ObjAnim: ## c
    def __init__(self, objs):
        self.objs = objs
        self.count = 0
        self.obj_index = 0
        self.state = True


    def run(self,x , y, gameDisplay):
        if self.state:
            gameDisplay.blit(self.objs[self.obj_index], (x, y))
            self.count += 1
            if self.count <= 3 :
                self.obj_index = (self.obj_index + 1) % len(self.objs)
                self.count = 0

obj_anim = ObjAnim(object_Img)
class GameModel:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height =height

    def get_rect(self):
        return Rect(self.x, self.y, self.width,self.height)

    def check_map(x):
        if x > display_width - player_w or x< 0:
            return False
        return True

player_model = GameModel(player_x,player_y, player_w, player_h)
obj_model = GameModel(obj_x,obj_y,obj_w,obj_h)
obj_model2 = GameModel(obj_x2,obj_y2,obj_w2,obj_h2)
boom_model = GameModel(boom_x, boom_y, boom_w, boom_h)
boom_model2 = GameModel(boom_x2, boom_y2, boom_w2, boom_h2)
heath_model = GameModel(heath_x,heath_y, heath_w, heath_h)

### diem cua game
font_name = ("font/breakaway.ttf")
def player_count(count_game):
    # font = pygame.font.SysFont(None, 25)

    font = pygame.font.Font(font_name, 25)
    text = font.render("COUNT "+ str(count_game), True, brown)
    screen.blit(text, (650, 10))

## turn cua nguoi choi
def player_heaths(player_heath):
    # font = pygame.font.SysFont(None, 25)
    font = pygame.font.Font(font_name, 25)
    text = font.render("HEATH "+ str(player_heath), True, brown)
    screen.blit(text, (50, 10))


def level(game_level):
    font = pygame.font.Font(font_name, 18)
    text = font.render("LEVEL "+ str(game_level), True, brown)
    screen.blit(text, (380, 10))
## check player in MAP
def check_map(y):
    if y > display_width - 80 or y < 0:
        return False
    return True
def set_boom():
    boom_model.y = -400
    boom_model.x = random.randrange(10, display_width - boom_w)
def set_boom2():
    boom_model2.y = -700
    boom_model2.x = random.randrange(10, display_width - boom_w)

def set_hetath():
    heath_model.x = random.randrange(200,500)
    heath_model.y = -display_height
#
# def load_data():
#
#     dir = path.dirname(__file__)
#     with open(path.join(dir, HS_FILE ), "w") as f:
#         try
#             highscore = int(f.read())
#         except:
# #              highscore = 0
def lose():
    # global highscore
    # font = pygame.font.Font(font_name, 40)
    # text = font.render("HIGH SCORE"+str(highscore),True, brown)
    # screen.blit(text, (display_width * 0.45, display_height * 0.2))
    font = pygame.font.Font(font_name, 100)
    text = font.render("YOU LOSE", True, brown)
    screen.blit(text, (display_width * 0.3, display_height * 0.3))
    screen.blit(button_q2, (480, 300))
    screen.blit(button_rs2,(250, 300))
    global  restart_b
    restart_b = screen.blit(button_rs2,(250,300))
    global quit_b
    quit_b = screen.blit(button_q2,(480,300))
    lose_sound.play()
    lose_sound.set_volume(0.6)
    die_sound.play()
    die_sound.set_volume(0.4)
    sound_ground.stop()
    sound_effect.stop()

    set_obj()
    set_obj2()
    set_boom2()
    set_boom()
    while True:

        # pygame.time.wait(10000)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pos = pygame.mouse.get_pos()
            if restart_b.collidepoint(pos):
                screen.blit(button_rs2_2,(250,300))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        lose_sound.stop()
                        die_sound.stop()
                        game_loop()
            else:
                screen.blit(button_rs2,(250,300))
            if quit_b.collidepoint(pos):
                screen.blit(button_q2_2,(480,300))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pygame.quit()
                    quit()
            else:
                screen.blit(button_q2,(480,300))
        pygame.display.update()

def pause_game():
    global pause
    global dx
    pause = True
    font = pygame.font.Font(font_name, 100)
    text = font.render("PAUSE", True, brown)
    screen.blit(text, (display_width * 0.35, display_height * 0.3))
    screen.blit(icon_pause, (750, 40))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dx = 0
                    pause = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if restart_b.collidepoint(pos):
                    lose_sound.stop()
                    die_sound.stop()
                    game_loop()

                if quit_b.collidepoint(pos):
                    pygame.quit()
                    quit()
        pygame.display.update()
def intro_game():
    global gameExit
    gameExit = True
    screen.blit(intro_Img, (0, 0))
    global start_b
    start_b = screen.blit(button_start1,(660,550))
    screen.blit(button_start1,(660,550))
    sound_effect.play(-1)
    sound_intro.play(-1)
    sound_intro.set_volume(0.4)
    while gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pos = pygame.mouse.get_pos()
            if start_b.collidepoint(pos):
                screen.blit(button_start0,(660,550))
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    sound_intro.stop()
                    game_loop()
            else:
                screen.blit(button_start1, (660, 550))
        pygame.display.update()
def get_rect(x,y,width,height):
    return Rect(x,y,width,height)

def set_obj():
    obj_model.y = -600
    obj_model.x = random.randrange(10, display_width - obj_w)

def set_obj2():
    obj_model2.y = -300
    obj_model2.x = random.randrange(30, 700)
def game_loop():
    # gia tri cua game
    global pause
    pause = False
    global dx
    dx = 0
    count_tick = 0
    player_heath = 3 ## mang cua nguoi choi
    count_game = 0 ## diem
    game_level = 0
    obj_speed = 5

    ### speed
    boom_speed = random.randrange(6,15)
    ## Sound
    sound_ground.play(-1)
    sound_ground.set_volume(0.4)
    sound_effect.play(-1)
    sound_effect.set_volume(1)
    # dieu khien Player
    global gameExit
    gameExit = True
    global pause_count
    pause_count = 0
    #### LOOP CODE
    while gameExit:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT :
                    if game_level == 2:
                        dx = -16
                    elif game_level == 3:
                        dx = -17
                    elif game_level == 4:
                        dx = -18
                    else:
                        dx = -15


                elif event.key == pygame.K_RIGHT:
                    if game_level == 2:
                        dx = 16
                    elif game_level == 3:
                        dx = 17
                    elif game_level == 4:
                        dx = 18
                    else:
                        dx = 15
                elif event.key == pygame.K_SPACE:
                    dx = 0
                    pause_game()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    dx = 0
                elif event.key == pygame.K_RIGHT:
                    dx = 0


        ## Dieu Kien va di chuyen
        next_x = player_model.x + dx
        if  check_map(next_x):
            player_model.x += dx
        ## reset vi tri cua objects
        if obj_model.y > display_height:
            set_obj()
        elif obj_model2.y > display_height:
            set_obj2()
        elif boom_model.y > display_height:
            set_boom()
        elif boom_model2.y > display_height:
            set_boom2()
        elif heath_model.y > display_height or player_heath == 3:
            set_hetath()
        if player_heath == 0:

            die_sound.play()
            die_sound.set_volume(0.4)
            die_sound.fadeout(3)
            lose()
        ## check eat
        Rect1 = get_rect(player_model.x,player_model.y, player_model.width,player_model.height)
        Rect2 = get_rect(obj_model.x,obj_model.y,obj_model.width,obj_model.height)
        Rect3 = get_rect(boom_model.x, boom_model.y, boom_model.width, boom_model.height)
        Rect4 = get_rect(obj_model2.x, obj_model2.y, obj_model2.width, obj_model2.height)
        Rect5 = get_rect(boom_model2.x, boom_model2.y, boom_model2.width, boom_model2.height)
        Rect6 = get_rect(heath_model.x, heath_model.y, heath_model.width, heath_model.height)
        if count_game == 1:
            game_level = 1
        elif count_game == 5:
            game_level = 2
            obj_speed = 7

        elif count_game == 10:
            game_level = 3
            obj_speed = 8

        elif count_game == 30:
            game_level = 4
            obj_speed = 10

        else:
            None
        if Rect1.colliderect(Rect2) and obj_model.y < display_height - 100:
            set_obj()
            eat1_sound.play()
            eat1_sound.set_volume((0.4))
            eat_sound.play()
            eat_sound.set_volume(0.5)
            neck_sound.play()
            neck_sound.set_volume(0.4)
            count_game += 1
        elif Rect1.colliderect(Rect4) and obj_model2.y < display_height - 100:
            set_obj2()
            eat_sound.play()
            eat1_sound.play()
            eat1_sound.set_volume((0.4))
            eat_sound.set_volume(0.5)
            neck_sound.play()
            neck_sound.set_volume(0.2)
            count_game += 1

        if Rect1.colliderect(Rect3):
            player_heath -= 1
            coll_sound.play()
            coll_sound.set_volume(0.7)
            crash_sound.play()
            crash_sound.set_volume(0.2)
            set_boom()
        elif Rect1.colliderect(Rect5):
            player_heath -= 1
            coll_sound.play()
            coll_sound.set_volume(0.7)
            crash_sound.play()
            crash_sound.set_volume(0.4)
            set_boom2()
        elif Rect1.colliderect(Rect6):
            player_heath += 1
            set_hetath()
            eat1_sound.play()
            eat1_sound.set_volume((0.4))
            eat_sound.play()
            eat_sound.set_volume(0.5)

        elif obj_model.y > display_height - 5:
            fall_sound.play()
            fall_sound.set_volume(0.4)
            player_heath -= 1
        elif obj_model2.y > display_height - 5:
            fall_sound.play()
            fall_sound.set_volume(0.5)
            player_heath -= 1

        ### cho cac object roi sau moi tick
        if game_level >= 2:
            obj_model2.y += obj_speed - 1

        obj_model.y += obj_speed
        boom_model.y += boom_speed
        boom_model2.y += boom_speed
        if player_heath < 3:
            heath_model.y += 3
        # draw background
        screen.fill(white)

        screen.blit(background_Img, (0, 0))



        ## Draw Cac su kien game

        # gameDisplay.blit(player_Img, (player_model.x, player_model.y))
        screen.blit(object_Img2, (obj_model.x, obj_model.y))
        obj_anim.run(player_model.x, player_model.y, screen)
        # gameDisplay.blit(object_Img2, (obj_model.x, obj_model.y))
        screen.blit(heath_Img, (heath_model.x, heath_model.y))
        if game_level >= 2:
            screen.blit(object_Img2, (obj_model2.x, obj_model2.y))
        #     obj_anim.run(obj_model2.x, obj_model2.y, gameDisplay)

        # screen.blit(boom_Img, (boom_model.x, boom_model.y))
        # screen.blit(boom_Img, (boom_model2.x, boom_model2.y))
        screen.blit(icon_play, (750, 40))
        level(game_level)
        player_heaths(player_heath)
        player_count(count_game)
        screen.blit(background_Img1, (0, 0))
        pygame.display.update()
        clock.tick(FPS)

intro_game()
pygame.quit()
quit()