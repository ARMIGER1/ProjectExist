label battle(player, enemy):
    # To start battling, call this label with 2 Player objects as arguments.

    $ player = copy(test_player)
    $ enemy = copy(test_enemy)

    # Disable rollback
    $ _rollback = False

    show screen battle_ui

    "[enemy.name] appeared!"

    call _battle(player, enemy)

    if _return is "lose":
        "Game over"
        $ renpy.full_restart()
    elif _return is "win":
        "You won!"
    elif _return is "escape":
        "You escaped!"

    hide screen battle_ui

    $ _rollback = True

    return

label _battle(player, enemy):
    # Handle the actual battle
    while True:
        $ player.move = renpy.call_screen("move_menu")
        $ enemy.move = renpy.random.choice(enemy.moves)

        if player.move.typea == 'escape':
            return 'escape'
        $ enemy.status = None
        $ player.attack(player.move, enemy)
        if enemy.hp < 1:
            return 'win'
        $ player.status = None
        $ enemy.attack(enemy.move, player)
        if player.hp < 1:
            return 'lose'
