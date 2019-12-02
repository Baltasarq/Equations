# Equation (c) Baltasar 2019 MIT License <baltasarq@gmail.com>


class Component:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return str(self._value)


class ValueComponent(Component):
    def __init__(self, value):
        super().__init__(value)


class VbleComponent(Component):
    def __init__(self, value):
        super().__init__(value)


def create(value):
    if (isinstance(value, str)
    and value.isalpha()):
        return VbleComponent(value)
    else:
        return ValueComponent(int(value))
