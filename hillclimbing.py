from solution import solution
import numpy as np
from time import time

class hillclimbing:
    def __init__(self, f, d: int, mi: int, bw: float, v : int, vTweak : int):
        self.best = solution(d, f)
        self.function = f
        self.maxiterations = mi
        self.bandwith = bw
        self.valor = v
        self.vT = vTweak

    def evolve(self):
        starttime = time()
        x = np.arange(0, self.maxiterations)
        y = np.zeros(self.maxiterations, float)
        self.best.randomInitialization(self.valor)
        for iteration in range(self.maxiterations):
            copyofbest = solution(self.best.size, self.best.function)
            copyofbest.from_solution(self.best)
            copyofbest.tweak(self.bandwith,self.vT)
            if copyofbest.fitness < self.best.fitness:
                self.best.from_solution(copyofbest)
            y[iteration] = self.best.fitness
        elapsedt = time() - starttime
        self.best.show(elapsedt)
        return [x, y]
