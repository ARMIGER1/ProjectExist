init -1 python:
    import renpy.store as store
    import renpy.exports as renpy
    from copy import copy

    class Player(store.object):
        """Player class"""
        def __init__(self, name, **args):
            super(Player, self).__init__()
            self.name = name
            self.args = args

            battle_attributes = [
                'level',
                'strength',
                'dexterity',
                'resistance',
                'speed',
                'intelligence',
                'spirit'
            ]

            player_attributes = [
                'HP',
                'maxHP',
                'belly',
                'maxBelly',
                'sleep',
                'maxSleep',
                'XP',
                'maxXP'
            ]

            # TODO: Add Weapon class in a separate file
            # TODO: Add Armor class in a separate file
            # TODO: Add Ability class in a separate file

            set_default_value(args, 'weapon', 'Fists')
            set_default_value(args, 'armor', 'Nothing')
            set_default_value(args, 'ai_type', None)
            set_default_value(args, 'status', None)

            empty_attributes = ['abilities', 'moves']

            for attribute in battle_attributes:
                set_default_value(args, attribute, 0)

            for attribute in player_attributes:
                set_default_value(args, attribute, 100)

            for attribute in empty_attributes:
                set_default_value(args, attribute, [])

            for key, value in self.args.items():
                if not (hasattr(self, key)):
                    setattr(self, key, value)

        def attack(self, move, target):
            pass

        def calculateDamage(self, move, target):
            pass

        def dealDamage(self, move, target):
            pass
