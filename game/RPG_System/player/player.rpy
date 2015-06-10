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
                'hp',
                'maxHP',
                'belly',
                'maxBelly',
                'sleep',
                'maxSleep',
                'xp',
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
            self.dealDamage(move, target)

        def calculateDamage(self, move, target):
            critdice = renpy.random.randint(0, 100)
            critmod = 1

            if (critdice <= 9):
                critmod = 2
                "It was a critical hit!"
            if (move.typea == 'physical' or move.typea == 'projectile'):
                defense = target.resistance

            if (move.typea == 'physical'):
                attack = self.strength
            elif(move.typea == 'projectile'):
                attack = self.dexterity
            elif(move.typea == 'aural'):
                attack = self.intelligence
                defense = target.spirit

            sect1 = (self.level * 2 / 5) + 2
            sect2 = move.power
            sect3 = attack
            sect4 = defense
            sect5 = 1

            battledice = renpy.random.randint(85, 100)

            damage = ((((((sect1 * sect2 * sect3 / 50) / sect4)) + 2) * critmod * battledice / 100) * sect5)

            return damage

        def dealDamage(self, move, target):
            # Try to attack
            hitdice = renpy.random.randint(0, 100)

            # TODO: Subtract relevant move costs

            # Attack missed
            if (hitdice > (move.accuracy * 100)) and self.status is not 'stunned':
                renpy.say(None, "%s used %s, but the attack missed...{fast}" % (self.name, move.name))
            elif self.status is 'stunned':
                # Player is stunned
                renpy.say(None, "%s is stunned and cannot move!" % (self.name))
            else:
                renpy.say(None, "%s used %s!" % (self.name, move.name))
                renpy.say(None, "Damage dealt to %s!" % target.name)

                damage = self.calculateDamage(move, target)

                target.hp -= damage

                if target.hp < 0:
                    target.hp = 0

                renpy.say(None, "%s took %d HP from %s.  %s's HP is now %d!" % (self.name, damage, target.name, target.name, target.hp))

                if (move.parameter == 'stun'):
                    statdice = renpy.random.randint(0, 100)
                    if (statdice < move.parameterplus):
                        target.status = 'stunned'
                        renpy.say(None, '%s is stunned!' % target.name)
