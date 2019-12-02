# Equations (c) Baltasar 2019 MIT License <baltasarq@gmail.com>


class TDS:
    def __init__(self):
        self._vbles = {}

    def __iadd__(self, other):
        self._vbles[other[0]] = other[1]
        return self

    def __getitem__(self, item):
        return self._vbles[item]

    def __setitem__(self, item, value):
        self._vbles[item] = value

    def get_vble_names(self):
        return list(self._vbles.keys())

    def __len__(self):
        return len(self._vbles)

    def get(self, vble):
        return self._vbles[vble]

    def __str__(self):
        toret = ""
        delim = ""

        for key in self._vbles.keys():
            toret += delim
            toret += str(key) + " = " + str(self._vbles[key])
            delim = ", "

        return toret
