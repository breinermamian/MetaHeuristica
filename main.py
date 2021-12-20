import numpy as np

from griewank import griewank
from hillclimbing import hillclimbing
from sphere import sphere
from step import step
from rastrigin import rastrigin
from schwefel import schwefel
import matplotlib.pyplot as plt


def menu():
    return int(input('''
        funciones a evaluar
        1. sphere
        2. step
        3. rastrigin
        4. schwefel
        5. griewank
        
        Ingrese una opcion:
    '''))


def funcionevaluar(funcion):
    myHC = hillclimbing(funcion, 10, 1000, 1, 2, 2)
    print("propuesta")
    [x, y] = myHC.evolve()
    myHC = hillclimbing(funcion, 10, 1000, 1, 1, 1)
    print("En clase")
    [x2, y2] = myHC.evolve()

    # plotting
    plt.title("Convergence curve")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    # plt.plot(x, y, color="red")
    # plt.plot(x2, y2, color="green")
    plt.plot(x, y, color="green")
    plt.plot(x2, y2, color="black")
    plt.show()


if __name__ == '__main__':

    opcion = menu()

    if opcion == 1:
        for i in range(1, 32):
            funcionevaluar(sphere(-5.0, 5.0))
    elif opcion == 2:
        for i in range(1, 32):
            funcionevaluar(step(-5.0, 5.0))
    elif opcion == 3:
        for i in range(1, 32):
            funcionevaluar(rastrigin(-5.0, 5.0))
    elif opcion == 4:
        for i in range(1, 32):
            funcionevaluar(schwefel(-5.0, 5.0))
    elif opcion == 5:
        for i in range(1, 32):
            funcionevaluar(griewank(-5.0, 5.0))
    else:
        print("Ingrese una opcion valida")
