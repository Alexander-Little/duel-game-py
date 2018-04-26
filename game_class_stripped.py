#Alexander Little - alittle5@cnm.edu
#duelists 1 / Single Combat
#adds:
#       Class based to facilitate Graphical User Interface
########Needed to restructure duel function to operate based on button pressed
#       Blood letting in semi-random increments
#   X    Main Menu Structure
#       Points System
#       Draw is now considered a 'clash'
import random
#import knights_game_simple
#import wx
#import GUI_base



match = 1
rnd = 1
#score [0]=player score     [1]=CPU score    [2]= round
score = [0, 0, 1]
health = [1, 1]
wounds = [0, 0]
blood = [0.0, 0.0] #1.0 = 1 gallon
play = "y"
longest = [0]
attacks = ('Parry/Riposte', 'Swing', 'Lunge')
title = "          -=Welcome to The Arena=-"
rules = "==========================================================="
rules += "  \nRULES: 1)" + str(attacks[2]) + " Beats " + str(attacks[1]) #+ ", but " + attacks[2] + " is beaten by " + attacks[0]
rules += "  \n       2)" + str(attacks[0]) + " Beats " + str(attacks[2]) 
rules += "  \n       3)" + attacks[1] + " Beats " + str(attacks[0]) 
rules += "  \n       4) When you and your enemy strike with an"
rules += "  \n          identical attack, it is known as a clash!"
rules += "  \n          You will gain +1 health on each clash! (max 3)"
rules += "\nSee how many duels you can win before you fall. good luck!"
rules += "\n==========================================================="
cSt = 0
lSt = 0 #change to load in high score
#anim = knights_game_simple
class game():
    #clean up match repeats
    match = 0
    def __init__(self, match = 0, rnd = 1, score = [0, 0, 1],
                health = [1, 1],
                wounds = [0, 0],
                blood = [0.0, 0.0], 
                play = "y",
                longest = [0],
                attacks = ('Block', 'Swing', 'Stab'),
                title = "Welcome to The Arena.",
                rules = "RULES: " + attacks[2] + " BEATS " + attacks[1] + " BEATS " + attacks[0] + " BEATS " + attacks[2],
                 cSt = 0, lSt = 0
                 ):
        self.match = match
        self.rnd = rnd
        #score [0]=player score     [1]=CPU score    [2]=draws/round # 
        self.score = score
        self.health = health
        self.wounds = wounds
        self.blood = blood #1.0 = 1 gallon
        self.play = play
        self.longest = longest
        self.attacks = attacks
        self.title = title
        self.rules = rules
        self.cSt = cSt
        self.lSt = lSt
        match = 0
        rnd = 1
        #score[0] = player score [1] = CPU
        ######
        #score = [0, 0, 1]
        play = "y"
        attacks = ('swing', 'block', 'stab')
        ######
        

    #round, score, health, wounds, blood, longest round
    #round, score, health, wounds, blood, longest round, current winstreak, longest winstreak
    def duel_lite(rnd, score, uAtk):
        #match += 1
        #print "---------------------"
        #print "Round: " + str(rnd)
        #print "---------------------"
        #print "Attacks: 1 = Rock 2 = Paper 3 = Scissors"
        #uAtk = input("Choose your attack: ")
        uAtk += -1
        cAtk = random.choice(attacks)
##        if uAtk == -1:
##            cAtk = 0
##            return
        #print "your move:", attacks[uAtk], "enemy move:", cAtk

        #result returns which animations to play
        #result[0] = left animations
        #result[1] = right animations
        result = (0,0,health)
        
        
        if (attacks.index(cAtk) == 0 and uAtk == 1):
            #enemy swing hits
            health[0] -= 1
            lRslt = 5
            rRslt = 1
            #score[1] = (score[1] + 1)
            
        elif (attacks.index(cAtk) == 1 and uAtk == 0):
            #player swing hits
            health[1] -= 1
            lRslt = 1
            rRslt = 5
            #score[0] = (score[0] + 1)
            
        elif (attacks.index(cAtk) == 1 and uAtk == 2 ):
            #enemy block hits
            health[0] -= 1
            lRslt = 6
            rRslt = 2
            #score[1] = (score[1] + 1)
            
        elif (attacks.index(cAtk) == 2 and uAtk == 1):
            #player block hits
            health[1] -= 1

            lRslt = 2
            rRslt = 6
            #score[0] = (score[0] + 1)

        elif (attacks.index(cAtk) ==  2 and uAtk == 0):
            #enemy stab hits
            health[0] -= 1

            lRslt = 4
            rRslt = 3
            #score[1] = (score[1] + 1)
            
        elif (attacks.index(cAtk) ==  0 and uAtk == 2):
            #player stab hits
            health[1] = (health[1] -1)

            lRslt = 3
            rRslt = 4
            #score[0] = (score[0] + 1)
            #print (result[0], result[1])
#        #result[2] = health
            #return result

            
        elif (attacks.index(cAtk) == uAtk):
            #clash         
            rnd += 1
            if health[0] < 3:
                health[0] += 1
            #Result +7 = clash animation
            lRslt = uAtk + 7
            rRslt = uAtk + 7
            #score[2] += 1 #add to round count (do it below, having both increments more than you want :P
            
            
    ##    print attacks.index(cAtk)
    ##    print uAtk
        #return score
        if (health[0] < 1):
            #resetting player's wins for now
            score[0] = 0
            #
            score[1] += 1
            lRslt += 9
            rRslt += 9
            score[2] = 0 #reset round count
            #match = 1 #reset level
            #add death result/change result[0] to death result
            #health[0] = 1
        elif (health[1] < 1):
            score[0] += 1
            lRslt += 9
            rRslt += 9
            score[2] = 0 #reset round count
            #match += 1 #go to next level
            #health[1] = 1
            #add death result/change result[0] to death result
        score[2] += 1
        result = (lRslt, rRslt, health)
        print (result[0], result[1])
        print ("your health: ", health[0])
#        #result[2] = health
        return result
#UPDATED animation/result key:
#animation key: 0 = idle, 1 = swing,      2 = block,      3 = stab,
#                         4 = swing fail, 5 = block fail, 6 = stab fail
#
#                         7 = swing clash 8 = block clash 9 = stab clash
#
#                         10= swing kill  11= block kill  12= stab kill
#                         13= swing death 14= block death 15= stab death
#knight_anims_r src should change with level


    def old_duel(self, rnd, score, health, wounds, blood, longest, cSt, lSt, uAtk = 0, cAtk = 0):

        bld_drp = (.01, .02, .03, .04, .05, .06, .07, .08, .09, .10)
        bld_gsh = (.6, .75, .8, .86, .9, .93, 1.0)
##        print("---------------------")
##        print ("Round: " + str(rnd))
##        print ("---------------------")
        if (longest[0] < rnd):
            longest[0] = rnd
##            print ("rounds: " + str(rnd))
##        print ("Attacks: 1 = " + attacks[0] + " 2 = " + attacks[1] + " 3 = " + attacks[2])
##        uAtk = int(input("Choose your attack: "))
##        uAtk += -1
        if (uAtk < 0 or uAtk > 2 or uAtk):
            print ("Agh! your hand must have slipped!")
            print ("luckily the sword flew towards the enemy!")
            uAtk = 2
        #cAtk = attacks[0]#random.choice(attacks)
            cAtk = random.choice(attacks)
##        print ("your move:", attacks[uAtk], "enemy move:", cAtk)
        if (attacks.index(cAtk) == 0 and uAtk == 2):
            
##            print ("|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|"
##             "\n     Enemy's", cAtk, "hits.."
##             "\n|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|")

            health[0] += -1
            wounds[0] += 1
            blood[0] += random.choice(bld_drp)
##            print ("your health:", health[0], "enemy health:", health[1])
            if (health[0] <= 0):  
                score[1] = (score[1] + 1)
                blood[0] += random.choice(bld_gsh)
##                print ("you've been slain.")
                #health[0] = 1 #reset player health
                #return
            else:
                rnd += 1
                self.duel(rnd, score, health, wounds, blood, longest, cSt, lSt)
        elif (attacks.index(cAtk) == 2 and uAtk == 0):

##            print ("|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|")
##            print ("     Your", attacks[uAtk], "hits!")
##            print ("|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|")
            health[1] += -1
            wounds[1] += 1
            blood[1] += random.choice(bld_drp)
##            print ("your health:", health[0], "enemy health:", health[1])
            if (health[1] <= 0):
##                print ("|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|")
##                print ("    Enemy slain! You are victorious!")
##                print ("|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|")
                blood[1] += random.choice(bld_gsh)
                score[0] = (score[0] + 1)
                self.cSt += 1
                health[1] = 1 #reset enemy health
            else:
                rnd += 1
                self.duel(rnd, score, health, wounds, blood, longest, cSt, lSt)
            
        elif (attacks.index(cAtk) > uAtk):
            
##            print ("|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|")
##            print ("     Enemy's", cAtk, "hits..")
##            print ("|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|-|=|")
            
            health[0] += -1
            wounds[0] += 1
            blood[0] += random.choice(bld_drp)
##            print ("your health:", health[0], "enemy health:", health[1])
            if (health[0] <= 0):  
                score[1] = (score[1] + 1)
                blood[0] += random.choice(bld_gsh)
##                print ("you've been slain.")
                #health[0] = 1 #reset player health
                #return
            else:
                rnd += 1
                self.duel(rnd, score, health, wounds, blood, longest, cSt, lSt)
            
        elif (attacks.index(cAtk) < uAtk):
##            print ("|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|")
##            print ("     Your", attacks[uAtk], "hits!")
##            print ("|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|")
            health[1] += -1
            wounds[1] += 1
            blood[1] += random.choice(bld_drp)
##            print ("your health:", health[0], "enemy health:", health[1])
            if (health[1] <= 0):
##                print ("|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|")
##                print ("    Enemy slain! You are victorious!")
##                print ("|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|+|=|")
                score[0] = (score[0] + 1)
                blood[1] += random.choice(bld_gsh)
                self.cSt += 1
                health[1] = 1 #reset enemy health
            else:
                rnd += 1
                self.duel(rnd, score, health, wounds, blood, longest, cSt, lSt)
            
        elif (attacks.index(cAtk) == uAtk and uAtk != 0):
##            print ("|=|-|=|+++|=|-|=|")
##            print ("|=|+-CLASH!!-+|=|")
##            print ("|=|-|=|+++|=|-|=|")
            if (health[0] < 3):    
##                print ("YOU GAIN 1 HEALTH")
                health[0] += 1
##            else:
##                print ("Already at max health")
##            print ("your health:", health[0])
            score[2] += 1
            rnd += 1
            self.duel(rnd, score, health, wounds, blood, longest, cSt, lSt)
            

        #could return a list of info if necessary

    def play_game(self):
        play = self.play
        match = self.match
        health = self.health
        #note: cSt and lSt below are called slightly differently because their info goes both ways post-duel
        cSt = self.cSt
        lSt = self.lSt
        print (title)
        print (rules)
        
        while (play != "n"):
            #starting health levels will change when game levels/characters are implemented
            #health = [1,1]
            
            ##reset health levels for player if they died
            if (health[0] <= 0):
                health[0] = 1
##            print ("your health:", health[0], "enemy health:", health[1])
            
            #print "Your remaining health: ", health[0]
            while (health[0] > 0):
##                print ("------------")
                match += 1
##                print ("Duel #" + str(match))
##                anim.k_ctrl()
                self.duel(rnd, score, health, wounds, blood, longest, cSt, lSt)

                #reset win streak if player dies
                if (health[0] < 1):
                    self.cSt = 0
                    
                if (self.cSt >= self.lSt):
                    self.lSt = self.cSt

##            play = input("Continue duels? (y/n)")


    def score_string(self):
        "returns a score string"
        sscore = "\n=============SCORE BREAKDOWN==================="
        sscore += "\nAllied blood split... " + str(blood[0]) + " gallons"
        sscore += "\nEnemy blood spilt.... " + str(blood[1]) + " gallons"
        sscore += "\nAllied wounds........ " + str(wounds[0])
        sscore += "\nEnemy wounds......... " + str(wounds[1])
        sscore += "\nLongest Duel......... " + str(longest[0]) + " rounds"
        sscore += "\nLongest win streak... " + str(g.lSt)
        sscore += "\n==============================================="
        sscore += "\nDuels won: " + str(score[0]) + " |-| Duels Lost: " + str(score[1]) + " |-| Clashes: " + str(score[2])
        sscore += "\n==============================================="
        return sscore
    
    def mini_score(self):
        mini = "==============================================="
        mini += "\nDuels won: " + str(score[0]) + " |-| Duels Lost: " + str(score[1]) + " |-| Clashes: " + str(score[2])
        mini += "\n==============================================="
        return mini
    def get_score():
        return score
    def set_level(level):
        global match
        match = level
    def get_level():
        return match



#g = game()
#anim.k_ctrl()
#g.play_game()
#print (g.score_string())


