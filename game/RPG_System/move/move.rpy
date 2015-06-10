init -1 python:
    import renpy.store as store
    import renpy.exports as renpy

    class Move(store.object):
        """Class for holding all RPG moves"""
        def __init__(self, name, **args):
            super(Move, self).__init__()
            self.name = name
            self.args = args

            set_default_value(args, 'description', 'No description')

            attributes = [
                'power',
                'accuracy',
                'priority',
                'parameter',
                'parameterplus',
                'typea',
                'typeb',
                'typec',
                'cost'
            ]

            for attribute in attributes:
                if attribute is 'cost':
                    set_default_value(args, attribute, {})
                else:
                    set_default_value(args, attribute, 0)

            # Transform all attributes into class attributes
            for key, value in self.args.items():
                if not (hasattr(self, key)):
                    setattr(self, key, value)
