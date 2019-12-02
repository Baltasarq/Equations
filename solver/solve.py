# Equations (c) Baltasar 2019 MIT License <baltasarq@gmail.com>


from solver.tds import TDS
from equations.Component import VbleComponent
from equations.Component import ValueComponent


def solve_equation(eq):
    toret = (None, 0)

    if isinstance(eq.result, VbleComponent):
        result = 0

        for i in range(len(eq)):
            component = eq[i]
            toret = (eq.result.value, result)

            if isinstance(component, ValueComponent):
                result += component.value
            else:
                result = 0
                toret = (None, 0)
                break

        toret = tuple([toret[0], result])
    else:
        vble = None

        # Locate vble
        for i in range(len(eq)):
            component = eq[i]

            if isinstance(component, VbleComponent):
                if not vble:
                    vble = component.value
                else:
                    break

        # Calculate
        if vble:
            value = 0

            for i in range(len(eq)):
                component = eq[i]

                if isinstance(component, ValueComponent):
                    value += component.value

            toret = (vble, (value - eq.result.value) * -1)

    return tuple(toret)


def solve(eq_system):
    def determine_vbles(eq_system):
        toret = []

        for eq in eq_system:
            if isinstance(eq.result, VbleComponent):
                toret.append(eq.result.value)

            for i in range(len(eq)):
                component = eq[i]

                if isinstance(component, VbleComponent):
                    toret.append(component.value)

        return set(toret)

    def try_to_solve_all(eq_system, tds):
        for eq in eq_system:
            result = solve_equation(eq)

            if result[0]:
                tds += result

        return

    num_vbles = len(determine_vbles(eq_system))
    tds = TDS()
    try_to_solve_all(eq_system, tds)

    while num_vbles > len(tds):
        if len(tds) == 0:
            break

        for i in range(len(tds)):
            vble_name = tds.get_vble_names()[i]
            pair_vble = tuple([vble_name, tds[vble_name]])

            for eq in eq_system:
                for j in range(len(eq)):
                    component = eq[j]

                    if (isinstance(component, VbleComponent)
                    and component.value == pair_vble[0]):
                        eq[j] = ValueComponent(pair_vble[1])

        try_to_solve_all(eq_system, tds)
    return tds
