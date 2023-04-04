# road map
# [ ] Every character has 20 hit points

#   [ ] Power-Ups drop from the sky
#     [ ] Hearts regenerates 1 HP
#     [ ] Speed boosts
#     [ ] Rare super power up - invulnerability, extra damage? 

#   [ ] Mask's attacks
#     [X] Arrow
#       [ ] Arrow does 2 damage
#       [ ] Ranged attack to end of screen that travels horizontally
#     [X] Slash
#       [ ] Slash does 2 damage

#   [ ] Astro's attacks
#     [X] Laser
#       [ ] Works the same as Mask's arrow, but has different graphics
#     [X] Ice Stab
#       [ ] Short-ranged projectile
#       [ ] 1 damage

#   [ ] Ninja's attacks
#     [ ] Sword
#       [ ] 1 damage
#     [ ] Ninja star
#       [ ] Same as Mask's arrow

#   [ ] Every character has a shield
#     [ ] Shield is activiated by pressing down
#     [ ] Characters take no damage when shield is up
#     [ ] Astro and Ninja have 15 second shields
#     [ ] Mask's shield lasts 30 second
#     [ ] Shield cooldowns

# close game with key H



#TROUBLESHOOTING:
#EDGAR: .GET_RECT() BAD
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# imports
import sys
import os
import pygame
from pygame.locals import *
import random
import time
import threading
from threading import Timer
pygame.init()
clock = pygame.time.Clock()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#attack timers
mask_attacks_1 = []
mask_attacks_2 = []
astro_attacks = []
ninja_attacks = []
item_drops = []
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#timers
class ThreadJob(threading.Thread):
    def __init__(self,callback,event,interval):
        '''runs the callback function after interval seconds

        :param callback:  callback function to invoke
        :param event: external event for controlling the update operation
        :param interval: time in seconds after which are required to fire the callback
        :type callback: function
        :type interval: int
        '''
        self.callback = callback
        self.event = event
        self.interval = interval
        super(ThreadJob,self).__init__()

    def run(self):
        while not self.event.wait(self.interval):
            self.callback()
    def stop(self):
        self.event.clear()

event = threading.Event()


def mask_attacking_1():
    global mask_attacks_1
    if len(mask_attacks_1) > 0:
        mask_attacks_1.pop(0)

def mask_attacking_2():
    global mask_attacks_2
    if len(mask_attacks_2) > 0:
        mask_attacks_2.pop(0)

def astro_attacking():
    global astro_attacks
    if len(astro_attacks) > 0:
        astro_attacks.pop(0)

def ninja_attacking():
    global ninja_attacks
    if len(ninja_attacks) > 0:
        ninja_attacks.pop(0)


m1 = ThreadJob(mask_attacking_1, event, 0.1)
m2 = ThreadJob(mask_attacking_2, event, 0.1)
n = ThreadJob(ninja_attacking, event, 0.1)
a = ThreadJob(astro_attacking, event, 0.15)

m1.start()
m2.start()
n.start()
a.start()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

width,height = 840,525
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#backgroun paths
background_file_path = "background.png"
ground_file_path = "ground-564x64.png"
FloatingPlatform_file_path = "floatingPlatform-640x410.png"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#player 1 variables

player1_health = 20
player1_direction = "right"
player1_run_acceleration =  20 # 7.5 # acceleration is a todo
player1_velocity_x = 0
player1_velocity_y = 0
player1_jump_timer = 0
player1_x = 100
player1_y = 300
player1_can_jump = True
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#player 2 variables

player2_health = 20
player2_direction = "left"
player2_run_acceleration =  25
player2_velocity_x = 0
player2_velocity_y = 0
player2_jump_timer = 0
player2_x = 600
player2_y = 300
player2_can_jump = True
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#mask variables
mask_y_speed_limit = 15
mask_arrows = []
mask_frame_scale_factor = (85,85)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#mask frames
mask_health_1 = pygame.transform.scale(pygame.image.load("pixilart-drawing.png"),(400,500))
mask_idle = pygame.transform.scale(pygame.image.load("mask_idle_frame1.png"),(160,160))
mask_idle2 = pygame.transform.scale(pygame.image.load("mask_idle_frame1.png"),(160,160))
mask_idle_frame1 = pygame.transform.scale(pygame.image.load("mask_idle_frame1.png"),mask_frame_scale_factor)
mask_idle_frame2 = pygame.transform.scale(pygame.image.load("mask_idle_frame2.png"),mask_frame_scale_factor)
mask_idle_frame3 = pygame.transform.scale(pygame.image.load("mask_idle_frame3.png"),mask_frame_scale_factor)
mask_idle_frame4 = pygame.transform.scale(pygame.image.load("mask_idle_frame4.png"),mask_frame_scale_factor)
mask_idle_frame5 = pygame.transform.scale(pygame.image.load("mask_idle_frame5.png"),mask_frame_scale_factor)
mask_idle_frame6 = pygame.transform.scale(pygame.image.load("mask_idle_frame6.png"),mask_frame_scale_factor)
mask_idle_frame7 = pygame.transform.scale(pygame.image.load("mask_idle_frame7.png"),mask_frame_scale_factor)
mask_idle_frame8 = pygame.transform.scale(pygame.image.load("mask_idle_frame8.png"),mask_frame_scale_factor)
mask_idle_frame9 = pygame.transform.scale(pygame.image.load("mask_idle_frame9.png"),mask_frame_scale_factor)
mask_idle_frame10 = pygame.transform.scale(pygame.image.load("mask_idle_frame10.png"),mask_frame_scale_factor)
mask_idle_frame11 = pygame.transform.scale(pygame.image.load("mask_idle_frame11.png"),mask_frame_scale_factor)
mask_idle_left_frame1 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame1.jpg"),mask_frame_scale_factor)
mask_idle_left_frame2 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame2.jpg"),mask_frame_scale_factor)
mask_idle_left_frame3 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame3.jpg"),mask_frame_scale_factor)
mask_idle_left_frame4 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame4.jpg"),mask_frame_scale_factor)
mask_idle_left_frame5 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame5.jpg"),mask_frame_scale_factor)
mask_idle_left_frame6 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame6.jpg"),mask_frame_scale_factor)
mask_idle_left_frame7 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame7.jpg"),mask_frame_scale_factor)
mask_idle_left_frame8 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame8.jpg"),mask_frame_scale_factor)
mask_idle_left_frame9 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame9.jpg"),mask_frame_scale_factor)
mask_idle_left_frame10 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame10.jpg"),mask_frame_scale_factor)
mask_idle_left_frame11 = pygame.transform.scale(pygame.image.load("mask_idle_left_frame11.jpg"),mask_frame_scale_factor)
arrow_right_frame = pygame.transform.scale(pygame.image.load("arrow-right.png"),mask_frame_scale_factor)
arrow_left_frame = pygame.transform.scale(pygame.image.load("arrow-left.png"),mask_frame_scale_factor)
mask_attack_p1 = pygame.transform.scale(pygame.image.load("slash.png"),(30,50))
mask_left_attack_p1 = pygame.transform.scale(pygame.image.load("slash_left.png"),(30,50))
mask_attack_p2 = pygame.transform.scale(pygame.image.load("slash.png"),(30,50))
mask_left_attack_p2 = pygame.transform.scale(pygame.image.load("slash_left.png"),(30,50))
mask_idle_frames = [mask_idle_frame1,mask_idle_frame2,mask_idle_frame3,mask_idle_frame4,
mask_idle_frame5,mask_idle_frame6,mask_idle_frame7,mask_idle_frame8,mask_idle_frame9,mask_idle_frame10,mask_idle_frame11]
mask_idle_left_frames = [mask_idle_left_frame1,mask_idle_left_frame2,mask_idle_left_frame3,mask_idle_left_frame4,
mask_idle_left_frame5,mask_idle_left_frame6,mask_idle_left_frame7,mask_idle_left_frame8,mask_idle_left_frame9,mask_idle_left_frame10,mask_idle_left_frame11]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#astro variables

astro_lasers = []
astro_frame_scale_factor = (85,85)
astro_speed_y_limit = 15
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#astro frames
astro_idle = pygame.transform.scale(pygame.image.load("astro_idle_frame1.png"),(160,160))
astro_idle2 = pygame.transform.scale(pygame.image.load("astro_idle_frame1.png"),(160,160))
astro_idle_frame1 = pygame.transform.scale(pygame.image.load("astro_idle_frame1.png"),astro_frame_scale_factor)
astro_idle_frame2 = pygame.transform.scale(pygame.image.load("astro_idle_frame2.png"),astro_frame_scale_factor)
astro_idle_frame3 = pygame.transform.scale(pygame.image.load("astro_idle_frame3.png"),astro_frame_scale_factor)
astro_idle_frame4 = pygame.transform.scale(pygame.image.load("astro_idle_frame4.png"),astro_frame_scale_factor)
astro_idle_frame5 = pygame.transform.scale(pygame.image.load("astro_idle_frame5.png"),astro_frame_scale_factor)
astro_idle_frame6 = pygame.transform.scale(pygame.image.load("astro_idle_frame6.png"),astro_frame_scale_factor)
astro_idle_frame7 = pygame.transform.scale(pygame.image.load("astro_idle_frame7.png"),astro_frame_scale_factor)
astro_idle_frame8 = pygame.transform.scale(pygame.image.load("astro_idle_frame8.png"),astro_frame_scale_factor)
astro_idle_frame9 = pygame.transform.scale(pygame.image.load("astro_idle_frame9.png"),astro_frame_scale_factor)
astro_idle_frame10 = pygame.transform.scale(pygame.image.load("astro_idle_frame10.png"),astro_frame_scale_factor)
astro_idle_frame11 = pygame.transform.scale(pygame.image.load("astro_idle_frame11.png"),astro_frame_scale_factor)
astro_idle_left_frame1 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame1.jpg"),astro_frame_scale_factor)
astro_idle_left_frame2 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame2.jpg"),astro_frame_scale_factor)
astro_idle_left_frame3 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame3.jpg"),astro_frame_scale_factor)
astro_idle_left_frame4 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame4.jpg"),astro_frame_scale_factor)
astro_idle_left_frame5 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame5.jpg"),astro_frame_scale_factor)
astro_idle_left_frame6 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame6.jpg"),astro_frame_scale_factor)
astro_idle_left_frame7 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame7.jpg"),astro_frame_scale_factor)
astro_idle_left_frame8 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame8.jpg"),astro_frame_scale_factor)
astro_idle_left_frame9 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame9.jpg"),astro_frame_scale_factor)
astro_idle_left_frame10 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame10.jpg"),astro_frame_scale_factor)
astro_idle_left_frame11 = pygame.transform.scale(pygame.image.load("astro_idle_left_frame11.jpg"),astro_frame_scale_factor)
laser_frame = pygame.transform.scale(pygame.image.load("laser.png"),mask_frame_scale_factor)
astro_attack = pygame.transform.scale(pygame.image.load("blue_crystal.png"),(50,25))
astro_left_attack = pygame.transform.scale(pygame.image.load("blue_crystal_left.png"),(50,25))
astro_idle_frames = [astro_idle_frame1,astro_idle_frame2,astro_idle_frame3,astro_idle_frame4,
astro_idle_frame5,astro_idle_frame6,astro_idle_frame7,astro_idle_frame8,astro_idle_frame9,astro_idle_frame10,astro_idle_frame11]
astro_idle_left_frames = [astro_idle_left_frame1,astro_idle_left_frame2,astro_idle_left_frame3,astro_idle_left_frame4,
astro_idle_left_frame5,astro_idle_left_frame6,astro_idle_left_frame7,astro_idle_left_frame8,astro_idle_left_frame9,astro_idle_left_frame10,astro_idle_left_frame11]


#mask variables
ninja_y_speed_limit = 15
ninja_stars = []
ninja_frame_scale_factor = (85,85)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#mask frames
ninja_idle = pygame.transform.scale(pygame.image.load("ninja_idle_frame1.png"),(160,160))
ninja_idle2 = pygame.transform.scale(pygame.image.load("ninja_idle_frame1.png"),(160,160))
ninja_idle_frame1 = pygame.transform.scale(pygame.image.load("ninja_idle_frame1.png"),ninja_frame_scale_factor)
ninja_idle_frame2 = pygame.transform.scale(pygame.image.load("ninja_idle_frame2.png"),ninja_frame_scale_factor)
ninja_idle_frame3 = pygame.transform.scale(pygame.image.load("ninja_idle_frame3.png"),ninja_frame_scale_factor)
ninja_idle_frame4 = pygame.transform.scale(pygame.image.load("ninja_idle_frame4.png"),ninja_frame_scale_factor)
ninja_idle_frame5 = pygame.transform.scale(pygame.image.load("ninja_idle_frame5.png"),ninja_frame_scale_factor)
ninja_idle_frame6 = pygame.transform.scale(pygame.image.load("ninja_idle_frame6.png"),ninja_frame_scale_factor)
ninja_idle_frame7 = pygame.transform.scale(pygame.image.load("ninja_idle_frame7.png"),ninja_frame_scale_factor)
ninja_idle_frame8 = pygame.transform.scale(pygame.image.load("ninja_idle_frame8.png"),ninja_frame_scale_factor)
ninja_idle_frame9 = pygame.transform.scale(pygame.image.load("ninja_idle_frame9.png"),ninja_frame_scale_factor)
ninja_idle_frame10 = pygame.transform.scale(pygame.image.load("ninja_idle_frame10.png"),ninja_frame_scale_factor)
ninja_idle_frame11 = pygame.transform.scale(pygame.image.load("ninja_idle_frame11.png"),ninja_frame_scale_factor)
ninja_idle_left_frame1 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame1.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame2 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame2.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame3 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame3.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame4 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame4.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame5 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame5.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame6 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame6.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame7 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame7.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame8 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame8.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame9 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame9.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame10 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame10.jpg"),ninja_frame_scale_factor)
ninja_idle_left_frame11 = pygame.transform.scale(pygame.image.load("ninja_idle_left_frame11.jpg"),ninja_frame_scale_factor)
ninja_star = pygame.transform.scale(pygame.image.load("star_left.png"),(50,50))
ninja_left_star = pygame.transform.scale(pygame.image.load("star.png"),(50,50))
ninja_attack = pygame.transform.scale(pygame.image.load("slash.png"),(30,50))
ninja_left_attack = pygame.transform.scale(pygame.image.load("slash_left.png"),(30,50))
ninja_idle_frames = [ninja_idle_frame1,ninja_idle_frame2,ninja_idle_frame3,ninja_idle_frame4,
ninja_idle_frame5,ninja_idle_frame6,ninja_idle_frame7,ninja_idle_frame8,ninja_idle_frame9,ninja_idle_frame10,ninja_idle_frame11]
ninja_idle_left_frames = [ninja_idle_left_frame1,ninja_idle_left_frame2,ninja_idle_left_frame3,ninja_idle_left_frame4,
ninja_idle_left_frame5,ninja_idle_left_frame6,ninja_idle_left_frame7,ninja_idle_left_frame8,ninja_idle_left_frame9,ninja_idle_left_frame10,ninja_idle_left_frame11]
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#display
screen = pygame.display.set_mode((840,525))# half of 1080p
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# #platforms

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(background_file_path)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Ground(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(ground_file_path)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class FloatingPlatform(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(FloatingPlatform_file_path)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#unknown

# class Player1(object):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.vel = 5
#         self.is_jump = False
#         self.jump_count = 10
#         self.is_walking_left = False
#         self.is_walking_right = Falses
#         self.walk_count = 0
#         self.is_standing = True

#     def drawPlayer(self, game_window):
#         if self.walk_count + 1 >= 27:
#             self.walk_count = 0
#         if not self.is_standing:
#             if self.is_walking_left:
#                 game_window.blit(ninja_idle_left_frames[self.walk_count//3], (self.x, self.y))
#                 self.walk_count+=1
#             elif self.is_walking_right:
#                 game_window.blit(mask_idle_frames[self.walk_count//3], (self.x, self.y))
#                 self.walk_count+=1
#         else:
#         # now we want to check what he was previously, was he left before or right?
#         # game_window.blit(char, (self.x, player.y))
#             if self.is_walking_right:
#                 game_window.blit(mask_idle_frames[0], (self.x, self.y))
#             else:
#                 game_window.blit(mask_idle_left_frames[0], (self.x, self.y))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#image loading
health_power_up = pygame.transform.scale(pygame.image.load("health-power-up.png"),(300,300))
speed_boost = pygame.transform.scale(pygame.image.load("speed-boost.png"),(200,200))

player_select1 = pygame.transform.scale(pygame.image.load("pixilart-drawing (1).png"),(350,350))
player_select2 = pygame.transform.scale(pygame.image.load("pixilart-drawing (2).png"),(350,350))    
backGround = Background('background.png', [0,0])
backGround.image = pygame.transform.scale(backGround.image,(width,height))

ground = Ground('ground-564x64.png', [0,450])
ground.image = pygame.transform.scale(ground.image,(840,75))

floatingPlatform = FloatingPlatform('floatingPlatform-640x410.png', [50,175])
floatingPlatform.image = pygame.transform.scale(floatingPlatform.image,(320,175))

floatingPlatform2 = FloatingPlatform('floatingPlatform-640x410.png', [450,175])
floatingPlatform2.image = pygame.transform.scale(floatingPlatform2.image,(320,175))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#item droping
def item_drop():
    global item_drops
    item_drops.append({'x':random.randint(-100,700),'y':-100,"power_up":random.randint(1,2)})
    print(item_drops)
item = ThreadJob(item_drop, event, 10)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#animation 

mask_idle_current_frame = mask_idle_frames[0]
astro_idle_current_frame = astro_idle_frames[0]
ninja_idle_current_frame = ninja_idle_frames[0]
# ninja_idle_current_frame = ninja_idle_frames[0]
player_idle_i = 0
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#game variables
mask_attacks_grouped = None
start_game = True
player1_selected = None
player2_selected = None
flag = True




#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#game  loop
while True:
    # jumping
    clock.tick(20)                    
    keys = pygame.key.get_pressed()
    if player1_jump_timer > 0:
        player1_jump_timer -= 1
    if player2_jump_timer > 0:
        player2_jump_timer -= 1
    # player1 jump
    if keys[pygame.K_w] and player1_can_jump == True and player1_velocity_y == 0 and player1_jump_timer == 0:
        player1_can_jump = False
        player1_velocity_y -= 70
        player1_jump_timer = 5


    # player2 jump
    if keys[pygame.K_i] and player2_can_jump == True and player2_velocity_y == 0 and player2_jump_timer == 0:
        player2_can_jump = False
        player2_velocity_y -= 70
        player2_jump_timer = 4
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#gravity
    if player1_selected == "Mask":
        player1_velocity_y += 7.5
    if player1_selected == "Astro":
        player1_velocity_y += 6
    if player1_selected == "Ninja":
        player1_velocity_y += 7        
    if player2_selected == "Mask":
        player2_velocity_y += 7.5
    if player2_selected == "Astro":
        player2_velocity_y += 6
    if player2_selected == "Ninja":
        player2_velocity_y += 7   
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#player selection
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_game == True: 
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if player1_selected == None:
                    if (mouse_x < 160 and mouse_x > 50)and (mouse_y < 260 and mouse_y > 120):
                        player1_selected = "Mask"
                    if (mouse_x < 360 and mouse_x > 250)and (mouse_y < 260 and mouse_y > 120):
                        player1_selected = "Astro"
                    if (mouse_x < 260 and mouse_x > 140)and (mouse_y < 400 and mouse_y > 290):
                        player1_selected = "Ninja"
                if player2_selected == None:
                    if (mouse_x < 560 and mouse_x > 450)and (mouse_y < 260 and mouse_y > 120):
                        player2_selected = "Mask"
                    if (mouse_x < 760 and mouse_x > 650)and (mouse_y < 260 and mouse_y > 120):
                        player2_selected = "Astro"
                    if (mouse_x < 650 and mouse_x > 540)and (mouse_y < 400 and mouse_y > 290):
                        player2_selected = "Ninja"
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
# player left right movement       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: # Stop mask from sliding left
                player1_velocity_x = 0
            if event.key == pygame.K_d: # Stop mask from sliding right
                player1_velocity_x = 0
            if event.key == pygame.K_j: # Stop astro from sliding left
                player2_velocity_x = 0
            if event.key == pygame.K_l: # Stop astro from sliding right
                player2_velocity_x = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player1_direction = "right"
                player1_velocity_x += player1_run_acceleration
            if event.key == pygame.K_a:
                player1_direction = "left"
                player1_velocity_x -= player1_run_acceleration
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                player2_direction = "right"
                player2_velocity_x += player2_run_acceleration
            if event.key == pygame.K_j:
                player2_direction = "left"
                player2_velocity_x -= player2_run_acceleration
            
                
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#player attacks
            if event.key == pygame.K_e:
                if player1_selected == "Mask":
                    player1_attack_offset = +20
                    if player1_direction == "left":
                        player1_attack_offset = -20
                    else:
                        player1_attack_offset = 70
                    mask_attacks_1.append({'direction': player1_direction, "x":player1_x + player1_attack_offset, "y": player1_y + 20})
                    
                if player1_selected =="Astro":
                    player1_offset = +10
                    if player1_direction == "left":
                        player1_offset = -10
                    else:
                        player1_offset = 10
                    astro_attacks.append({'direction': player1_direction, 'x':player1_x + player1_offset,'y': player1_y + 35})
                if player1_selected == "Ninja":
                    player1_attack_offset = +20
                    if player1_direction == "left":
                        player1_attack_offset = -20
                    else:
                        player1_attack_offset = 70
                    ninja_attacks.append({'direction': player1_direction, "x":player1_x + player1_attack_offset, "y": player1_y + 20})
            if event.key == pygame.K_q:
                if player1_selected == "Mask":
                    player1_offset = +10
                    if player1_direction == "left":
                        player1_offset = -10
                    else:
                        player1_offset = 10
                    mask_arrows.append({'direction': player1_direction, "x":player1_x + player1_offset, "y": player1_y})
                if player1_selected == "Astro":
                    player1_offset = +10
                    if player1_direction == "left":
                        player1_offset = -10
                    else:
                        player1_offset = 10
                    astro_lasers.append({'direction': player1_direction, 'x':player1_x + player1_offset,'y': player1_y})
                if player1_selected == "Ninja":
                    player1_offset = +10
                    if player1_direction == "left":
                        player1_offset = -10
                    else:
                        player1_offset = 10
                    ninja_stars.append({'direction': player1_direction, 'x':player1_x + player1_offset,'y': player1_y + 20})

            if event.key == pygame.K_u:
                if player2_selected == "Astro":
                    player2_offset = +10
                    if player2_direction == "left":
                        player2_offset = -10
                    else:
                        player2_offset = 10
                    astro_lasers.append({'direction': player2_direction, 'x':player2_x + player2_offset,'y': player2_y})
                if player2_selected == "Mask":
                    player2_offset = +10
                    if player2_direction == "left":
                        player2_offset = -10
                    else:
                        player2_offset = 10
                    mask_arrows.append({'direction': player2_direction, "x":player2_x + player2_offset, "y": player2_y})   
                if player2_selected == "Ninja":
                    player2_offset = +10
                    if player2_direction == "left":
                        player2_offset = -10
                    else:
                        player2_offset = 10
                    ninja_stars.append({'direction': player2_direction, 'x':player2_x + player2_offset,'y': player2_y+20})                 
            if event.key == pygame.K_o:
                if player2_selected == "Mask":
                    mask_attack_offset = +20
                    if player2_direction == "left":
                        mask_attack_offset = -20
                    else:
                        mask_attack_offset = 70
                    mask_attacks_2.append({'direction': player2_direction, "x":player2_x + mask_attack_offset, "y": player2_y + 20})
                if player2_selected =="Astro":
                    astro_offset = +10
                    if player2_direction == "left":
                        astro_offset = -10
                    else:
                        astro_offset = 10
                    astro_attacks.append({'direction': player2_direction, 'x':player2_x + astro_offset,'y': player2_y + 35})
                if player2_selected == "Ninja":
                    player2_attack_offset = +20
                    if player2_direction == "left":
                        player2_attack_offset = -20
                    else:
                        player2_attack_offset = 70
                    ninja_attacks.append({'direction': player2_direction, "x":player2_x + player2_attack_offset, "y": player2_y + 20})
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#close game

        if event.type == QUIT:
            m1.stop()
            m2.stop()
            n.stop()
            a.stop()
            pygame.quit()
            os._exit(0)
            # sys.exit("closing now.....")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
# postion update
    player1_x += player1_velocity_x
    player1_y += player1_velocity_y
    
    player2_x += player2_velocity_x
    player2_y += player2_velocity_y

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#collisions
    # edge of screen boundary detection
    if player1_x >= 775:
        player1_x = 774
    if player1_x <= -25:
        player1_x = -24
    if player1_y >= 370:
        player1_y = 369
        player1_can_jump = True
        player1_velocity_y = 0
    if player2_x >= 775:
        player2_x = 774
    if player2_x <= -25:
        player2_x = -24
    if player2_y >= 370:
        player2_y = 369
        player2_can_jump = True
        player2_velocity_y = 0
    #Platform Collision
    if player1_y >= 150 and player1_x >= 50 and player1_x <= 275 and player1_y <= 200:
         player1_y = 149
         player1_can_jump = True
         player1_velocity_y = 0
    if player1_y >= 150 and player1_x >= 450 and player1_x <= 675 and player1_y <= 200:
         player1_y = 149
         player1_can_jump = True
         player1_velocity_y = 0

    if player2_y >= 150 and player2_x >= 50 and player2_x <= 275 and player2_y <= 200:
         player2_y = 149
         player2_can_jump = True
         player2_velocity_y = 0
    if player2_y >= 150 and player2_x >= 450 and player2_x <= 675 and player2_y <= 200:
         player2_y = 149
         player2_can_jump = True
         player2_velocity_y = 0
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#drop_collision
    for drop in item_drops:
        if drop['y'] >350:
            drop['y'] = 349
        if drop['y'] >= 130 and drop['x'] >= 0 and drop['x'] <= 190:
            drop['y'] = 129
        if drop['y'] >= 130 and drop['x'] >= 400 and drop['x'] <= 590:
            drop['y'] = 129



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#animations
    if player1_selected == "Mask":
        player1_idle_frames = mask_idle_frames
        player1_idle_left_frames = mask_idle_left_frames
    if player1_selected == "Astro":
        player1_idle_frames = astro_idle_frames
        player1_idle_left_frames = astro_idle_left_frames
    if player1_selected == "Ninja":
        player1_idle_frames = ninja_idle_frames
        player1_idle_left_frames = ninja_idle_left_frames
    if player2_selected == "Mask":
        player2_idle_frames = mask_idle_frames
        player2_idle_left_frames = mask_idle_left_frames
    if player2_selected == "Astro":
        player2_idle_frames = astro_idle_frames
        player2_idle_left_frames = astro_idle_left_frames
    if player2_selected == "Ninja":
        player2_idle_frames = ninja_idle_frames
        player2_idle_left_frames = ninja_idle_left_frames
    if player_idle_i == 10:
        player_idle_i = 0
    player_idle_i += 1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# background
    screen.blit(backGround.image, backGround.rect)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#player selection variables
    if player1_selected != None and player2_selected != None:
        if flag == True:
            if player1_selected == "Mask":
                player1_run_acceleration = 20
            if player1_selected == "Astro":
                player1_run_acceleration = 25
            if player1_selected == "Ninja":
                player1_run_acceleration = 30
            if player2_selected == "Mask":
                player2_run_acceleration = 20
            if player2_selected == "Astro":
                player2_run_acceleration = 25
            if player2_selected == "Ninja":
                player2_run_acceleration = 30
            if player1_selected == "Mask":
                player1_jump_timer = 5
            if player1_selected == "Astro":
                player1_jump_timer = 4
            if player1_selected == "Ninja":
                player1_jump_timer = 4
            if player2_selected == "Mask":
                player2_jump_timer = 5
            if player2_selected == "Astro":
                player2_jump_timer = 4
            if player2_selected == "Ninja":
                player2_jump_timer = 4
            item.start()
            flag = False
        start_game = False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    screen.fill([255, 255, 255])
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#screen updates
    #player select
    if start_game == True:

        screen.blit(backGround.image, backGround.rect)
        screen.blit(player_select1, (25,-100))
        screen.blit(player_select2, (425,-100))
        if player1_selected == 'Mask':
            screen.blit(mask_idle, (20,100))
        elif player1_selected == "Astro":
            screen.blit(astro_idle,(220,100))
        elif player1_selected == "Ninja":
            screen.blit(ninja_idle,(120,250))
        else:  
            screen.blit(mask_idle, (20,100))
            screen.blit(astro_idle,(220,100))
            screen.blit(ninja_idle,(120,250))
        if player2_selected == 'Mask':
            screen.blit(mask_idle2, (420,100))
        elif player2_selected == "Astro":
            screen.blit(astro_idle2,(620,100))
        elif player2_selected == "Ninja":
            screen.blit(ninja_idle2,(520,250))
        else:
            screen.blit(mask_idle2, (420,100))
            screen.blit(astro_idle2,(620,100))
            screen.blit(ninja_idle2,(520,250))
    else:        
    #in game updates
        player1_idle_current_frame = player1_idle_frames[player_idle_i]
        player1_idle_left_current_frame = player1_idle_left_frames[player_idle_i]
        player2_idle_current_frame = player2_idle_frames[player_idle_i]
        player2_idle_left_current_frame = player2_idle_left_frames[player_idle_i]
        screen.blit(backGround.image, backGround.rect)
        screen.blit(ground.image, ground.rect)
        screen.blit(floatingPlatform.image, floatingPlatform.rect)
        screen.blit(floatingPlatform2.image, floatingPlatform2.rect)
        if player1_direction == 'left':
            screen.blit(player1_idle_left_current_frame,(player1_x, player1_y))
        elif player1_direction == 'right':
            screen.blit(player1_idle_current_frame,(player1_x, player1_y))
        if player2_direction == 'left':
            screen.blit(player2_idle_left_current_frame,(player2_x, player2_y))
        elif player2_direction == 'right':
            screen.blit(player2_idle_current_frame,(player2_x, player2_y))
        # attacks update
        #mask
        for arrow in mask_arrows:
            if arrow['direction'] == "left":
                screen.blit(arrow_left_frame, (arrow["x"], arrow["y"]))
            else:
                screen.blit(arrow_right_frame, (arrow["x"], arrow["y"]))

        for attack in mask_attacks_1:
            if mask_left_attack_p1.get_rect().colliderect(player2_idle_current_frame.get_rect()) or mask_attack_p1.get_rect().colliderect(player2_idle_left_current_frame.get_rect()):
                print('I have hit Player 2')
            if attack['direction'] == "left":
                screen.blit(mask_left_attack_p1, (attack["x"], attack["y"]))
            else:
                screen.blit(mask_attack_p1, (attack["x"], attack["y"]))
        for attack in mask_attacks_2:
            # add if collision exists
            if mask_left_attack_p2.get_rect().colliderect(player1_idle_current_frame.get_rect()) or mask_attack_p2.get_rect().colliderect(player1_idle_left_current_frame.get_rect()):
                print('I have hit Player 1')
            if attack['direction'] == "left":
                screen.blit(mask_left_attack_p2, (attack["x"], attack["y"]))
            else:
                screen.blit(mask_attack_p2, (attack["x"], attack["y"]))
        #ninja
        for attack in ninja_attacks:

            if attack['direction'] == "left":
                screen.blit(ninja_left_attack, (attack["x"], attack["y"]))
            else:
                screen.blit(ninja_attack, (attack["x"], attack["y"]))
        for star in ninja_stars:
            if star['direction'] == "left":
                screen.blit(ninja_left_star, (star["x"], star["y"]))
            else:
                screen.blit(ninja_star, (star["x"], star["y"]))
        #astro
        for attack in astro_attacks:
            if attack['direction'] == "left":
                screen.blit(astro_left_attack, (attack["x"], attack["y"]))
            else:
                screen.blit(astro_attack, (attack["x"], attack["y"]))
        for laser in astro_lasers:
            screen.blit(laser_frame, (laser["x"], laser["y"]))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#item drops
        for drop in item_drops:
            #print(health_power_up.get_rect(topleft=(200,200)),player1_idle_current_frame.get_rect())
            print('Soemthing: ', player1_idle_current_frame.get_rect().collidepoint(health_power_up.get_rect().center))
            if drop["power_up"] == 1:
                screen.blit(health_power_up,(drop["x"], drop["y"]))
            if drop["power_up"] == 2:
                screen.blit(speed_boost,(drop["x"], drop["y"]))
            # if health_power_up.get_rect(topleft=(200,200)).collidepoint(player1_idle_current_frame.get_rect(center=(100,100)).centerx):
            #     print('hbvjhdfg')
            #     player1_health += 1

        for drop in item_drops:
            drop['y'] += 10
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#projectile update
        for arrow in mask_arrows:
            if arrow['direction'] == "left":
                arrow["x"] -= 40
                
            else:
                arrow["x"] += 40

        for laser in astro_lasers:

            if laser['direction'] == "left":
                laser["x"] -= 45
                
            else:
                laser["x"] += 45
        for attack in astro_attacks:

            if attack['direction'] == "left":
                attack["x"] -= 40
                
            else:
                attack["x"] += 40
        for star in ninja_stars:
            if star['direction'] == "left":
                star["x"] -= 50
                
            else:
                star["x"] += 50

    pygame.display.update()
