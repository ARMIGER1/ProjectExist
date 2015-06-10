label load_moves:
    $ struggle = Move('Struggle',
        power=50,
        accuracy=0.80,
        priority=0,
        parameter='struggle',
        parameterplus=None,
        typea='physical',
        typeb='normal',
        typec='close',
        cost=['', '']
    )

    $ pound = Move('Pound',
        description="""A basic attack in which the user, with any blunt object
        (including fists), strikes the opponent.""",
        power=50,
        accuracy=.95,
        priority=0,
        parameter=None,
        parameterplus=None,
        typea='physical',
        typeb='normal',
        typec='close',
        cost=['', '']
    )

    $ check = Move('Check',
        description="""A somewhat advanced technique in which the user tries to
        get in a light but surprising hit before the opponent has time to react.
        This has a 30 percent chance of causing flinching.""",
        power=10,
        accuracy=.70,
        priority=1,
        parameter='stun',
        parameterplus=30,
        typea='physical',
        typeb='normal',
        typec='close',
        cost=['', '']
    )

    $ warlocks_fist = Move("Warlock's Fist",
        description="""A somewhat advanced technique that requires use of
        tactics learned in the Dream Worlds.  The user locks onto his opponent's
        mind, and launches a strong punch backed with Dream Energy.""",
        power=85,
        accuracy=1.00,
        priority=-1,
        parameter='homing',
        parameterplus=None,
        typea='physical',
        typeb='dream',
        typec='close',
        cost=[-4, 'SP']
    )

    $ escape = Move('Escape', typea='escape')

    return
