# Equations (c) Baltasar 2019 MIT License <baltasarq@gmail.com>


from equations.Equation import Equation
from equations.Component import create


def parser(txt):
    toret = []

    for lin in txt.split('\n'):
        parts = lin.split(' ')

        if len(parts) > 2:
            eq = Equation()
            eq.result = create(parts[0].strip())

            for part in parts[1:]:
                if (part != '+'
                and part != '='):
                    eq += create(part)

            toret.append(eq)

    return toret
