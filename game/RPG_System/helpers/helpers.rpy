init -3 python:
    def set_default_value(dictionary, attribute, default_value):
        if not attribute in dictionary:
            dictionary[attribute] = default_value
