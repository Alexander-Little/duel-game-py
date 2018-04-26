import sys
import pygame
#from pygame.locals import Color, KEYUP, K_ESCAPE, K_RETURN
from pygame.locals import *
#import spritesheet
from sprite_strip_anim import SpriteStripAnim
import random
from game_class_stripped import game as gg

##todo: use sprite groups, make unique left and right knight animation functions
fullscreen = False
surface = pygame.display.set_mode((800, 600))
FPS = 30
rulesSm = pygame.image.load('l_knight\\rules_simple.png')
rules = pygame.image.load('gui\\rules_extra.png')
load = pygame.image.load('gui\\load.png')
splash = pygame.image.load('gui\\splash.png')
##bground should change with level
bground = pygame.image.load('Backgrounds\\arena_01.png')
hp_plus = pygame.image.load('gui\\heart.png')
hp_minus = pygame.image.load('gui\\heart_brk.png')
bnr_vic = pygame.image.load('gui\\banner_victory.png')
bnr_def = pygame.image.load('gui\\banner_defeat.png')
surface.fill((100,100,100))
surface.blit(load, (0,0))
pygame.display.flip()
frames = FPS / 10
color_key = (255, 255, 255)
result = (0,0,(1,1))
n2 = 0
health = (1,1)
p_max_hp = 3
cpu_max_hp = 3
score = (0,0,1)
rnd = 1
level = 1
ruleBool = False
#animation key: 0 = idle, 1 = swing,      2 = block,      3 = stab,
#                         4 = swing fail, 5 = block fail, 6 = stab fail
#
#                         7 = swing clash 8 = block clash 9 = stab clash
#
#                         10= swing kill  11= block kill  12= stab kill
#                         13= swing death 14= block death 15= stab death
#knight_anims_r src should change with level
anim_width = 418
anim_height = 350
#other characters, not implemented fully
##knight_anims_r = [
##    SpriteStripAnim('r_knight\\sheet_Knight_right_Idle_1.png', (0, 0, 408, 327), 10, (255,255,255), False, frames),
##    SpriteStripAnim('r_knight\\sheet_Knight_right_swing_000.png', (0, 0, 408, 327), 10, (255,255,255), False, frames),
##    SpriteStripAnim('r_knight\\sheet_Knight_right_block.png', (0, 0, 408, 327), 10, (255,255,255), False, frames),
##    SpriteStripAnim('r_knight\\sheet_Knight_right_stab.png', (0, 0, 408, 327), 10, (255,255,255), False, frames),
##    SpriteStripAnim('r_knight\\sheet_Knight_right_swing_fail.png', (0, 0, 408, 327), 10, (255,255,255), False, frames),
##    SpriteStripAnim('r_knight\\sheet_Knight_right_block_fail.png', (0, 0, 408, 327), 10, (255,255,255), False, frames),
##    SpriteStripAnim('r_knight\\sheet_Knight_right_stab_fail_alt_000.png', (0, 0, 408, 327), 10, (255,255,255), False, frames),
##    SpriteStripAnim('r_knight\\sheet_Knight_right_clash_000.png', (0, 0, 408, 327), 10, (255,255,255), False, frames),
##]
char_src = 'gld'
knight_anims_l = [
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_Idle_1.png', (0, 0, anim_width, anim_height), 10, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_swing_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_block_001.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_stab_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_swing_fail_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_block_fail_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_stab_fail_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_swing_clash_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_block_clash_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_stab_clash_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),   
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_swing_kill_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_block_kill_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_stab_kill_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_swing_death_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_block_death_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('l_knight\\' + char_src + '_Knight_left_stab_death_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
]
char_src = 'ex'
knight_anims_r = [
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_Idle_1.png', (0, 0, anim_width, anim_height), 10, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_swing_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_block.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_stab_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_swing_fail_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_block_fail_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_stab_fail_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_swing_clash_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_block_clash_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_stab_clash_000.png', (0, 0, anim_width, anim_height), 12, (255,255,255), False, frames),    
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_swing_kill_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_block_kill_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_stab_kill_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_swing_death_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_block_death_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
    SpriteStripAnim('r_knight\\' + char_src + '_Knight_right_stab_death_000.png', (0, 0, anim_width, anim_height), 20, (255,255,255), False, frames),
]
    

    
grey = Color('grey')
clock = pygame.time.Clock()
surface.blit(splash, (0,0))
surface.blit(bground, (100,120))

#beginning round value
pygame.font.init()
font_regal = pygame.font.SysFont('Vivaldi', 30, True, False, None)
font_regal_sm = pygame.font.SysFont('BlackAdderITC', 22, True, False, None)
font_duel = pygame.font.SysFont('Times New Roman', 25, True, False, None)
rnd_txt = font_regal.render("Round " + str(score[2]), True, (0,0,0))
win_txt = font_regal_sm.render("Wins:" + str(score[0]), True, (220,20,20))
loss_txt = font_regal.render("Losses:" + str(score[1]), True, (150,20,20))
duel_txt = font_duel.render(str(level), True, (255,255,255))
hint_txt = font_duel.render("Press r to view rules/controls", True, (20, 220, 220))
def load_char():
    print("char loaded")
def load_lvl(lvl):
    level = lvl
    global bground
    if (level <= 3):
        bground = pygame.image.load('Backgrounds\\arena_0' + str(level) + '.png')
    
    else:    
        bground = pygame.image.load('Backgrounds\\arena_0' + str(random.randint(1,3)) + '.png')
    
    
def k_ctrl(left = 0, right = 0, health = (1,1)):
    #print ("round: ", score[2])
    surface.blit(bground, (100,120))
    lHp = health[0]
    rHp = health[1]
    
    pygame.event.clear(KEYDOWN)
    n1 = right #right
    n2 = left #left
            
    #surface.set_alpha(True)
    knight_anims_r[n1].iter()
    knight_anims_l[n2].iter()
    r_knight = knight_anims_r[n1].next()
    l_knight = knight_anims_l[n2].next()
    
    while (StopIteration != True):
        surface.blit(bground, (100,120))
#Need to review sprites for smoother gameplay        #rKgrp = pygame.sprite.RenderPlain(knight_anims_l[0])
        if n2 == 12 or n2 == 11:
            surface.blit(l_knight, (170, 90))
            surface.blit(r_knight, (270, 90))

        else:           
            surface.blit(r_knight, (270, 90))
            surface.blit(l_knight, (170, 90))
        surface.blit(splash, (0,0))
        
        surface.blit(rnd_txt, (340,518))
        surface.blit(win_txt, (97,122))
        surface.blit(duel_txt, (397, 107))
        surface.blit(hint_txt, (0, 570))
          ##draw health bars
        i = 0
        #xplc = health[0]
        #left side  
        while i != lHp and lHp > 0:
            surface.blit(hp_plus, (100 + (i * 25), 90))
            i += 1
        while i != p_max_hp:
            surface.blit(hp_minus, (100 + (i * 25), 90))
            i += 1
        i = 0
        #right side
        while i != rHp and rHp > 0:
            surface.blit(hp_plus, (625 + (i * 25), 90))
            i += 1
        while i != cpu_max_hp:
            surface.blit(hp_minus, (625 + (i * 25), 90))
            i += 1
        if (ruleBool):    
            surface.blit(rules, (210, 150))
        pygame.display.flip()
        
#animation key: 0 = idle, 1 = swing,      2 = block,      3 = stab,
#                         4 = swing fail, 5 = block fail, 6 = stab fail
#
#                         7 = swing clash 8 = block clash 9 = stab clash
#
#                         10= swing kill  11= block kill  12= stab kill
#                         13= swing death 14= block death 15= stab death
#knight_anims_r src should change with level
#control key: left = stab, down = block, right = swing, *up = idle
#                                                       *(not used)
###########
        transition = True
        try:
            r_knight = knight_anims_r[n1].next()
            l_knight = knight_anims_l[n2].next()
            #break
            
        except:
            
            #print("stop iteration detected")

            ##end level banners/transition
            if (lHp < 1 or rHp < 1):
                global level
                if (lHp < 1):
                    i = 0
                    while i < 180:
                        surface.blit(bnr_def, (273,-300 + i))
                        pygame.display.flip()
                        i += 1
    

                elif (rHp < 1):
                    i = 0
                    while i < 180:
                        surface.blit(bnr_vic, (273,-300 + i))
                        pygame.display.flip()
                        i += 1


                pygame.event.clear()                
                while transition != False:
                    event = pygame.event.wait()
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYUP:
                        if event.key == K_RETURN:
                            #print ("enter pressed")
                            if (health[0] < 1):
                                health[0] = 1
                                level = 1
                                lHp = health[0]
                            elif (health[1] < 1):
                                health[1] = 1
                                level += 1
                                rHp = health[1]
                            load_lvl(level)
                            transition = False
                            
                        #else:
                            #print("splurt")
                        
            else:
                n2 = 0
                break
        clock.tick(FPS)
        


#PLAY LOOP#################################################
while 1:
#animation key: 0 = idle, 1 = swing,      2 = block,      3 = stab,
#                         4 = swing fail, 5 = block fail, 6 = stab fail 7 = Clash
#control key: left = stab, down = block, right = swing, *up = idle
#                                                       *(not used)
#result[0] = left
#result[1] = rigt
#result[2] = health list (health[0]=left, [1]=right)
        ##USER INPUT/RESPONSIVE RENDERING
    for e in pygame.event.get():
        
        n2 = 0
        if e.type == KEYDOWN:
            #if n2 != 0: pygame.event.clear(KEYDOWN)
            if e.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif e.key == K_DOWN:
                n2 = 2
                #print("down")
##                result = gg.duel_lite(0,([0,0]),n2)
##                k_ctrl(result[1], result[0], result[2]) 

            elif e.key == K_LEFT:
                #n1 = 4
                n2 = 3
                #print("left")
##                result = gg.duel_lite(0,([0,0]),n2)
##                k_ctrl(result[1], result[0], result[2])

            elif e.key == K_RIGHT:
                #n1 = 5
                n2 = 1
                #print("right")
##                result = gg.duel_lite(0,([0,0]),n2)
##                k_ctrl(result[1], result[0], result[2])
            elif e.key == K_r:
                #^ toggles bool
                ruleBool^=True
            elif e.key == K_f:
                if fullscreen == True:
                    surface = pygame.display.set_mode((800, 600))
                    fullscreen = False
                    surface.blit(load, (0,0))
                    pygame.display.flip()
                else:
                    surface = pygame.display.set_mode((800, 600), FULLSCREEN)
                    fullscreen = True
                    surface.blit(splash, (0,0))
                    pygame.display.flip()
            pygame.event.clear(KEYDOWN)
            if n2 != 0:               
                result = gg.duel_lite(rnd,score,n2)
                health = result[2]
                k_ctrl(result[0], result[1], health)
            #print ("your wins: ", score[0], " enemy wins: ", score[1])
            #print ("round: ", score[2])
            rnd_txt = font_regal.render("Round " + str(score[2]), True, (0,0,0))
            win_txt = font_regal_sm.render("Wins:" + str(score[0]), True, (220,20,20))
            loss_txt = font_regal.render("Losses: " + str(score[1]), True, (150,20,20))
            gg.set_level(level)
            level = gg.get_level()
            #print ("level: ", str(level))
            duel_txt = font_duel.render(str(level), True, (255,255,255))
            ######
        if e.type == QUIT:
                pygame.quit()
                sys.exit()
        
           
        score = gg.get_score()
        
        #print ("your wins: ", score[0], " enemy wins: ", score[1], " round: ", score[2])
                
    pygame.event.clear(KEYDOWN)
    k_ctrl(0,0, health)#without this line the game "pauses" after 4 rotations
            
        ##RENDERING operated by k_ctrl()

