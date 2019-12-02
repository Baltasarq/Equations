# Equation (c) Baltasar 2019 MIT License <baltasarq@gmail.com>

from equations.Equation import Equation
from equations.Component import create
from solver.solve import solve
from parser import parser

if __name__ == "__main__":
    eqs = parser("x = 5 + 3\n2 = y + 3\nz = x + y")
    print("\n".join([str(eq) for eq in eqs]))
    print(solve(eqs))
