# Equation (c) Baltasar 2019 MIT License <baltasarq@gmail.com>

from equations.Component import ValueComponent


class Equation:
    def __init__(self):
        self._components = []
        self._result = ValueComponent(0)

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, component):
        self._result = component

    def add(self, other):
        self._components.append(other)

    def __iadd__(self, other):
        self.add(other)
        return self

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        return self._components[item]

    def __setitem__(self, item, value):
        self._components[item] = value

    def __str__(self):
        if len(self) == 0:
            return str(self.result)
        else:
            return str(self.result) + " = " + " + ".join([str(x) for x in self._components])
