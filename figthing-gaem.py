# road map
# [ ] Every character has 10 hit points

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
#     [ ] Ice Stab
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

import os
import pygame
from pygame.locals import *
import random
import time
import threading
pygame.init()
clock = pygame.time.Clock()

width,height = 840,525

background_file_path = "background.png"
ground_file_path = "ground-564x64.png"
FloatingPlatform_file_path = "floatingPlatform-640x410.png"

mask_health = 20
mask_direction = "right"
mask_run_acceleration =  20 # 7.5 # acceleration is a todo
mask_velocity_x = 0
mask_velocity_y = 0
mask_jump_timer = 0
mask_y_speed_limit = 15
mask_x = 100
mask_y = 100
mask_can_jump = True
mask_arrows = []
mask_attacks = []
mask_frame_scale_factor = (85,85)
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
mask_attack = pygame.transform.scale(pygame.image.load("slash.png"),(30,50))
mask_left_attack = pygame.transform.scale(pygame.image.load("slash_left.png"),(30,50))
mask_idle_frames = [mask_idle_frame1,mask_idle_frame2,mask_idle_frame3,mask_idle_frame4,
mask_idle_frame5,mask_idle_frame6,mask_idle_frame7,mask_idle_frame8,mask_idle_frame9,mask_idle_frame10,mask_idle_frame11]
mask_idle_left_frames = [mask_idle_left_frame1,mask_idle_left_frame2,mask_idle_left_frame3,mask_idle_left_frame4,
mask_idle_left_frame5,mask_idle_left_frame6,mask_idle_left_frame7,mask_idle_left_frame8,mask_idle_left_frame9,mask_idle_left_frame10,mask_idle_left_frame11]


#astro_velocity_movement_speed = 10
astro_health = 20
astro_direction = "left"
astro_run_acceleration =  25
astro_velocity_x = 0
astro_velocity_y = 0
astro_jump_timer = 0
astro_speed_y_limit = 15
astro_x = 200
astro_y = 200
astro_can_jump = True
astro_lasers = []
astro_attacks = []
astro_frame_scale_factor = (85,85)

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

# ninja_velocity = 12.5
# ninja_x = 500 
# ninja_y = 450
# ninja_frame_scale_factor = (85,85)
# ninja_idle_frame1 = pygame.transform.scale(pygame.image.load("ninja_idle_frame1.png"),ninja_frame_scale_factor)
# ninja_idle_frame2 = pygame.transform.scale(pygame.image.load("ninja_idle_frame2.png"),ninja_frame_scale_factor)
# ninja_idle_frame3 = pygame.transform.scale(pygame.image.load("ninja_idle_frame3.png"),ninja_frame_scale_factor)
# ninja_idle_frame4 = pygame.transform.scale(pygame.image.load("ninja_idle_frame4.png"),ninja_frame_scale_factor)
# ninja_idle_frame5 = pygame.transform.scale(pygame.image.load("ninja_idle_frame5.png"),ninja_frame_scale_factor)
# ninja_idle_frame6 = pygame.transform.scale(pygame.image.load("ninja_idle_frame6.png"),ninja_frame_scale_factor)
# ninja_idle_frame7 = pygame.transform.scale(pygame.image.load("ninja_idle_frame7.png"),ninja_frame_scale_factor)
# ninja_idle_frame8 = pygame.transform.scale(pygame.image.load("ninja_idle_frame8.png"),ninja_frame_scale_factor)
# ninja_idle_frame9 = pygame.transform.scale(pygame.image.load("ninja_idle_frame9.png"),ninja_frame_scale_factor)
# ninja_idle_frame10 = pygame.transform.scale(pygame.image.load("ninja_idle_frame10.png"),ninja_frame_scale_factor)
# ninja_idle_frame11 = pygame.transform.scale(pygame.image.load("ninja_idle_frame11.png"),ninja_frame_scale_factor)

# ninja_idle_frames = [ninja_idle_frame1,ninja_idle_frame2,ninja_idle_frame3,ninja_idle_frame4,
# ninja_idle_frame5,ninja_idle_frame6,ninja_idle_frame7,ninja_idle_frame8,ninja_idle_frame9,ninja_idle_frame10,ninja_idle_frame11]

screen = pygame.display.set_mode((840,525))# half of 1080p

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
#         self.is_walking_right = False
#         self.walk_count = 0
#         self.is_standing = True

#     def drawPlayer(self, game_window):
#         if self.walk_count + 1 >= 27:
#             self.walk_count = 0
#         if not self.is_standing:
#             if self.is_walking_left:
#                 game_window.blit(mask_idle_left_frames[self.walk_count//3], (self.x, self.y))
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

mask_idle_current_frame = mask_idle_frames[0]
astro_idle_current_frame = astro_idle_frames[0]
# ninja_idle_current_frame = ninja_idle_frames[0]
player_idle_i = 0
mask_count = 0

mask_attacks_grouped = None
start_game = True

while True:

    clock.tick(20)                    
    keys = pygame.key.get_pressed()
    if mask_jump_timer > 0:
        mask_jump_timer -= 1
    if astro_jump_timer > 0:
        astro_jump_timer -= 1
    # Mask's controlsqd

    if keys[pygame.K_w] and mask_can_jump == True and mask_velocity_y == 0 and mask_jump_timer == 0:
        mask_can_jump = False
        mask_velocity_y -= 70
        mask_jump_timer = 5


    # Astro's controls
    if keys[pygame.K_i] and astro_can_jump == True and astro_velocity_y == 0 and astro_jump_timer == 0:
        astro_can_jump = False
        astro_velocity_y -= 70
        astro_jump_timer = 4

    #if keys[K_k]:
    #    astro_y += astro_velocity

    # if keys[K_8]:
    #     ninja_y -= ninja_velocity
    # if keys[K_5]:
    #     ninja_y += ninja_velocity
    # if keys[K_4]:
    #     ninja_x -= ninja_velocity
    # if keys[K_]:
        # ninja_x += ninja_velocity

    #gravity
    mask_velocity_y += 7.5
    astro_velocity_y += 5.5

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if start_game == True: 
            #    if mask_idle.get_rect().collidepoint(pygame.mouse.get_pos()):
                if mask_idle.get_rect().colliderect(mask_idle.get_rect(), astro_idle.get_rect()):
                    print("moose")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: # Stop mask from sliding left
                mask_velocity_x = 0
            if event.key == pygame.K_d: # Stop mask from sliding right
                mask_velocity_x = 0
            if event.key == pygame.K_j: # Stop astro from sliding left
                astro_velocity_x = 0
            if event.key == pygame.K_l: # Stop astro from sliding right
                astro_velocity_x = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                mask_offset = +10
                if mask_direction == "left":
                    mask_offset = -10
                else:
                    mask_offset = 10
                mask_arrows.append({'direction': mask_direction, "x":mask_x + mask_offset, "y": mask_y})
            if event.key == pygame.K_d:
                mask_direction = "right"
                mask_velocity_x += mask_run_acceleration
                mask_count += 1
            if event.key == pygame.K_a:
                mask_direction = "left"
                mask_velocity_x -= mask_run_acceleration
                mask_count += 1
            if event.key == pygame.K_e:
                mask_attack_offset = 20
                if mask_direction == "left":
                    mask_attack_offset = -20
                else:
                    mask_attack_offset = 70
                mask_attacks.append({'direction': mask_direction, "x":mask_x + mask_attack_offset, "y": mask_y + 20})

            if event.key == pygame.K_u:
                astro_offset = +10
                if astro_direction == "left":
                    astro_offset = -10
                else:
                    astro_offset = 10
                astro_lasers.append({'direction': astro_direction, 'x':astro_x + astro_offset,'y': astro_y})
            if event.key == pygame.K_o:
                astro_offset = +10
                if astro_direction == "left":
                    astro_offset = -10
                else:
                    astro_offset = 10
                astro_attacks.append({'direction': astro_direction, 'x':astro_x + astro_offset,'y': astro_y + 35})
            if event.key == pygame.K_l:
                astro_direction = "right"
                astro_velocity_x += astro_run_acceleration
            if event.key == pygame.K_j:
                astro_direction ="left"
                astro_velocity_x -= astro_run_acceleration
            if event.key == pygame.K_h:
               sys.exit()
            # if mask_attacks_grouped == None:
            #     mask_attacks_grouped = pygame.sprite.groupcollide(mask_attacks, backGround.rect, True, False)
            # elif mask_attacks_grouped:
            #     mask_attacks_grouped = None
            #     mask_attacks_grouped = pygame.sprite.groupcollide(mask_attacks, backGround.rect, True, False)
                
        if event.type == QUIT:
            sys.exit()

#projectile update
    for arrow in mask_arrows:

        if arrow['direction'] == "left":
            arrow["x"] -= 40
            
        else:
            arrow["x"] += 40

    for laser in astro_lasers:

        if laser['direction'] == "left":
            laser["x"] -= 40
            
        else:
            laser["x"] += 40
    for attack in astro_attacks:

        if attack['direction'] == "left":
            attack["x"] -= 40
            
        else:
            attack["x"] += 40




    # postion update
    mask_x += mask_velocity_x
    mask_y += mask_velocity_y
    
    astro_x += astro_velocity_x
    astro_y += astro_velocity_y

    # collision detection
    #                      SIZE            LOCATIONd
    #  LEFT PLATFORM       450 x 175       50 x 175
    #  RIGHT PLATFORM      450 x 175       450 x 175

    # edge of screen boundary detection
    if mask_x >= 775 :
        mask_x = 774
    if mask_x <= -25:
        mask_x = -24
    if mask_y >= 370:
        mask_y = 369
        mask_can_jump = True
        mask_velocity_y = 0

    #Platform Collision
    if mask_y >= 150 and mask_x >= 50 and mask_x <= 275 and mask_y <= 200:
         mask_y = 149
         mask_can_jump = True
         mask_velocity_y = 0
    if mask_y >= 150 and mask_x >= 450 and mask_x <= 675 and mask_y <= 200:
         mask_y = 149
         mask_can_jump = True
         mask_velocity_y = 0

    if astro_y >= 150 and astro_x >= 50 and astro_x <= 275 and astro_y <= 200:
         astro_y = 149
         astro_can_jump = True
         astro_velocity_y = 0
    if astro_y >= 150 and astro_x >= 450 and astro_x <= 675 and astro_y <= 200:
         astro_y = 149
         astro_can_jump = True
         astro_velocity_y = 0


    if astro_x >= 775:
        astro_x = 774
    if astro_x <= -25:
        astro_x = -24
    if astro_y >= 370:
        astro_y = 369
        astro_can_jump = True
        astro_velocity_y = 0

    # animation
    if player_idle_i == 11:
        player_idle_i = 0
        mask_count = 0
        astro_count = 0
    mask_idle_current_frame = mask_idle_frames[player_idle_i]
    mask_idle_left_current_frame = mask_idle_left_frames[player_idle_i]
    astro_idle_current_frame = astro_idle_frames[player_idle_i]
    astro_idle_left_current_frame = astro_idle_left_frames[player_idle_i]
    # ninja_idle_current_frame = ninja_idle_frames[player_idle_i]
    player_idle_i += 1


    # screen updates
    screen.blit(backGround.image, backGround.rect)
    # if start_game is True then show the choose character screen
    
    screen.fill([255, 255, 255])
    if start_game == True:
        screen.blit(backGround.image, backGround.rect)
        screen.blit(player_select1, (25,-100))
        screen.blit(player_select2, (425,-100))
        screen.blit(mask_idle, (20,100))
        screen.blit(astro_idle,(220,100))
        screen.blit(mask_idle2, (420,100))
        screen.blit(astro_idle2,(620,100))
    else:
        screen.blit(ground.image, ground.rect)
        screen.blit(floatingPlatform.image, floatingPlatform.rect)
        screen.blit(floatingPlatform2.image, floatingPlatform2.rect)
        screen.blit(mask_health_1,(200,200))
        screen.blit(mask_idle_current_frame, (mask_x, mask_y))
        # IF mask is looking to the left then show mask_idle_left
        if mask_direction == 'left':
            screen.blit(mask_idle_left_current_frame,(mask_x, mask_y))
        elif mask_direction == 'right':
            screen.blit(mask_idle_current_frame,(mask_x, mask_y))
        if astro_direction == 'left':
            screen.blit(astro_idle_left_current_frame,(astro_x, astro_y))
        elif astro_direction == 'right':
            screen.blit(astro_idle_current_frame,(astro_x, astro_y))

        for arrow in mask_arrows:
            if arrow['direction'] == "left":
                screen.blit(arrow_left_frame, (arrow["x"], arrow["y"]))
            else:
                screen.blit(arrow_right_frame, (arrow["x"], arrow["y"]))
        for laser in astro_lasers:
            screen.blit(laser_frame, (laser["x"], laser["y"]))
        # for attack in mask_attack:
        #     if attack['direction'] == "left":
        #         screen.blit(astro_left_attack, (attack["x"], attack["y"]))
        #     else:
        #         screen.blit(astro_attack, (attack["x"], attack["y"]))
        # for mask in mask_attacks_grouped.keys():
        #     for current_mask in mask:
        #         if attack['direction'] == "left":
        #             screen.blit(mask_left_attack, (attack["x"], attack["y"]))
        #         else:
        #             screen.blit(mask_attack, (attack["x"], attack["y"]))

        for attack in mask_attacks:
            if attack['direction'] == "left":
                screen.blit(mask_left_attack, (attack["x"], attack["y"]))
            else:
                screen.blit(mask_attack, (attack["x"], attack["y"]))

        for attack in astro_attacks:
            if attack['direction'] == "left":
                screen.blit(astro_left_attack, (attack["x"], attack["y"]))
            else:
                screen.blit(astro_attack, (attack["x"], attack["y"]))
    
    



    # screen.blit(ninja_idle_current_frame, (ninja_x, ninja_y))

    pygame.display.update()
