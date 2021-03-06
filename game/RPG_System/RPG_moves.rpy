#######
# File name: RPG_moves.rpy
# 
# Description: Implements a class for hollding RPG moves.
# 
# Original author: Nolan/NintendoToad
# 
# Type: Library
# 
# Usage:
#     See cb_move() below.
#######

init -1 python:

    #####
    # Class name: cb_ability()
    # 
    # Description: Define innate abilities for combat. Also symbols.
    #
    # Parameters:
    # name - the name of the ability
    # level - the level of the ability
    #####
    class cb_ability():
        def __init__(self, name, level):
            self.name = name
            self.level = level

    #####
    # Class name: cb_status()
    # 
    # Description: Define innate abilities for combat, like stun
    #
    # Parameters:
    # name - the name of the status
    # turns - number of turns to be inflicted
    #####
    class cb_ability():
        def __init__(self, name, turns):
            self.name = name
            self.turns = turns

    #####
    # Class name: cb_move()
    # 
    # Description: Define moves for combat.
    # 
    # Parameters:
    # power - the base power of the move
    # accuracy - move's base chance to hit
    # prority - speed of the move
    # parameter - special parameter
    # parameterplus - special parameter
    # typea - physical or projectile?
    # typeb - element
    # typec - when I know what this does I'll tell you
    # cost - the cost to use
    # the really long text
    #
    # Returns: a move object of sorts
    #####
    class cb_move:
        def __init__(self, name, power, accuracy, priority, parameter, parameterplus, typea, typeb, typec, cost, desc = ""):
            self.name = name
            self.power = power
            self.accuracy = accuracy
            self.priority = priority
            self.parameter = parameter
            self.parameterplus = parameterplus
            self.typea = typea
            self.typeb = typeb
            self.typec = typec
            self.cost = cost
            self.desc = desc

        #####
        # Function name: asm_long_disp()
        # 
        # Description: Assemble a textual representation of the combat move. This is for .
        # 
        # Parameters:
        # move - the move object we are using.
        # 
        # Returns: the text
        #####
        def asm_long_disp(self):
            desc = self.desc + "\n"
            return desc
        
        #####
        # Function name: assign()
        # 
        # Description: Assign the move parameters to the character stats.
        # 
        # Parameters:
        # move - the move object we are using.
        # user - who is using the move
        # movename - the name of the move
        # 
        # Returns: None
        #####
        def assign(self, user, movename):
            if(user == "m1"):
                store.m1power = self.power
                store.m1accuracy = self.accuracy
                store.m1priority = self.priority
                store.m1move = movename
                store.m1parameter = self.parameter
                store.m1parameterplus = self.parameterplus
                store.m1typea = self.typea
                store.m1typeb = self.typeb
                store.m1typec = self.typec
                store.m1cost = self.cost[:]
            elif(user == "e1"):
                store.e1power = self.power
                store.e1accuracy = self.accuracy
                store.e1priority = self.priority
                store.e1move = movename
                store.e1parameter = self.parameter
                store.e1parameterplus = self.parameterplus
                store.e1typea = self.typea
                store.e1typeb = self.typeb
                store.e1typec = self.typec
                store.e1cost = self.cost[:]
            return
            
            
        #####
        # Function name: asm_disp()
        # 
        # Description: Assemble a textual representation of the combat move. This is mostly for debugging.
        # 
        # Parameters:
        # move - the move object we are using.
        # 
        # Returns: the text
        #####
        def asm_disp(move):#text version of assembling the text description
            #power block
            powertxt = "[Power: "
            if(move.power != None):
                powertxt += str(move.power)
            else:
                powertxt += "N/A"
            #accuracy block
            accuracytxt = " || Accuracy: "
            if(move.accuracy != None):
                accuracytxt += str(move.accuracy)
            else:
                accuracytxt += "N/A"
            #priority block
            prioritytxt = " || Priority: "
            if(move.priority != None):
                prioritytxt += str(move.priority)
            else:
                prioritytxt += "N/A"
            typetxt = " || " + str(move.typea).title() + " || " + str(move.typeb).title()
            #cost
            if(move.cost == ["", ""]):
                costtxt = "]\n"
            else:
                costtxt = " || Cost: " + str(move.cost[0]) + " " + move.cost[1] + "]\n"
            return (powertxt + accuracytxt + prioritytxt + typetxt + costtxt + move.desc)
        
                
screen move_details(move):
    for dkey, dmove in cbm.iteritems():
        if move is dmove:
            $ md_move = dkey
    if(move.parameter == None):
        $ effect = "None"
    else:
        $ effect = (move.parameter).title()
    if(move.parameterplus == None):
        $ coeffect = "N/A"
    else:
        $ coeffect = str(move.parameterplus).title() + "%"
    
    modal True
    zorder 10
    window:
        xminimum 1000
        xmaximum 1000
        yminimum 700
        ymaximum 700
        xalign .5
        yalign .5
        vbox:
            frame:
                xminimum 200
                text md_move
            hbox:
                frame:
                    xminimum 90
                    style "game_box"
                    text "Power:\n  " + str(move.power)
                frame:
                    xminimum 115
                    style "game_box"
                    text "Accuracy:\n  " + str(move.accuracy)
                frame:
                    xminimum 100
                    style "game_box"
                    text "Priority:\n  " + str(move.priority)
                frame:
                    xminimum 115
                    style "game_box"
                    text "Impact:\n  " + (move.typea).title()
                frame:
                    xminimum 135
                    style "game_box"
                    text "Alignment:\n  " + (move.typeb).title()
                frame:
                    xminimum 115
                    style "game_box"
                    text "Effect:\n  " + effect
                frame:
                    xminimum 165
                    style "game_box"
                    text "Rate of Effect:\n  " + coeffect
            vbox:
                frame:
                    xminimum 988
                    yminimum 590
                    text move.asm_long_disp()
        textbutton _("Return") action Return() align (.97, 1.0)

