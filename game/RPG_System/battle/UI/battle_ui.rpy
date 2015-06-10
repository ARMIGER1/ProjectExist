screen battle_ui():
    # Display battle stats
    use player_stats(player, position=(.05, .05)) id "player"
    use player_stats(enemy, position=(.95, .05)) id "enemy"

screen player_stats(player, position):
    # A screen with player stats
    frame xysize(330, None) align(position) style("game_box"):
        vbox yfill False:
            text "%s Lv. %d" % (player.name, player.level)
            hbox xfill False:
                vbox:
                    text "HP"
                    text "FP"
                    text "SP"
                    showif player.ai_type == None:
                        text "XP"
                vbox:
                    bar value player.hp range player.maxHP xsize 180
                    bar value player.belly range player.maxBelly xsize 180
                    bar value player.sleep range player.maxSleep xsize 180
                    showif player.ai_type == None:
                        bar value player.xp range player.maxXP xsize 180
                vbox xfill True:
                    text("%d/%d" % (player.hp, player.maxHP)) xalign 1.0
                    text("%d/%d" % (player.belly, player.maxBelly)) xalign 1.0
                    text("%d/%d" % (player.sleep, player.maxSleep)) xalign 1.0
                    showif player.ai_type == None:
                        text("%d/%d" % (player.xp, player.maxXP)) xalign 1.0

screen move_menu():
    # Screen used for selecting moves.
    vbox style_group "move" align(.5, .5):
        for i in player.moves:
            textbutton "[i.name]" xsize(100) action Return(value = i)
