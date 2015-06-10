label combat_test:
    scene bg blackdrop
    # Combat test
    call load_moves

    $ test_player = Player('Kazuki',
        level=5,
        belly=65,
        sleep=75,
        xp=0,
        maxXP=50,
        strength=11,
        dexterity=11,
        resistance=20,
        speed=14,
        intelligence=14,
        spirit=20,
        moves=[struggle, pound, check, warlocks_fist, escape]
    )

    $ test_enemy = Player('Shadow',
        ai_type='enemy',
        level=4,
        hp=60,
        maxHP=60,
        xp=0,
        maxXP=35,
        strength=24,
        dexterity=7,
        resistance=6,
        speed=2,
        intelligence=9,
        spirit=24,
        moves=[pound]
    )

    "Begin combat test!"

    call battle(test_player, test_enemy)
    return
