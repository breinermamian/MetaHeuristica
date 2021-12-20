import numpy as np
import solution as solution
from sphere import sphere

class solution:
    def __init__(self, d: int, f):
        self.size = d
        self.cells = np.zeros(self.size, float)
        self.fitness = 0.0
        self.function = f

    def from_solution(self, origin:solution):
        self.size = origin.size
        self.cells = np.copy(origin.cells)
        self.fitness = origin.fitness
        self.function = origin.function

    def randomInitialization(self,valor : int):
        #5 puntos aleatorios y escojo el mejor
        if valor == 1:
            self.randomInitialization1()
        else :
            self.randomInitialization2()

    def randomInitialization1(self):
        self.cells = np.random.uniform(low=self.function.lowerbound, high=self.function.upperbound,
                                       size=(self.size,))
        self.fitness = self.function.evaluate(self.cells)

    def randomInitialization2(self):
        self.cells = np.random.uniform(low=self.function.lowerbound, high=self.function.upperbound,
                                       size=(self.size,))
        self.fitness = self.function.evaluate(self.cells)
        fitnesstemporal = 0.0
        i=0
        while i < 10:
            self.cells = np.random.uniform(low=self.function.lowerbound, high=self.function.upperbound,
                                           size=(self.size,))

            fitnesstemporal = self.function.evaluate(self.cells)
            #print("Valor Temporal:: ", fitnesstemporal);
            print("Fitness:: ", self.fitness)
            if(fitnesstemporal < self.fitness):
                self.fitness = fitnesstemporal
            i=i+1
        print("Fitness:: ", self.fitness)

        #Generamos 5soluciones- Escogemos la mejor y la regresamos.

    def tweak(self, bw: float):
        n = np.random.randint(1,self.size+1)#Aleatorio entre el número de dimensiones -> Mínimo 1
        bandwidths = np.random.uniform(low=-bw, high=bw, size=(n,))#Bandwihth para n dimensiones
        i=0 #Inicia el Vector desde pos 0
        while(i<n):
            self.cells[i] = self.cells[i] + bandwidths[i]#Sumamos cada dimensión hasta n
            i=i+1
        #Si es menor del rango se asigna el limite inferior, así mismo para el superior
        self.cells[self.cells < self.function.lowerbound] = self.function.lowerbound
        self.cells[self.cells > self.function.upperbound] = self.function.upperbound
        self.fitness = self.function.evaluate(self.cells)

    def tweak(self, bw: float):
        bandwidths = np.random.uniform(low=-bw, high=bw, size=(self.size,))
        self.cells = self.cells + bandwidths
        self.cells[self.cells < self.function.lowerbound] = self.function.lowerbound
        self.cells[self.cells > self.function.upperbound] = self.function.upperbound
        self.fitness = self.function.evaluate(self.cells)

    def show(self):
        print(self.cells)
        print(self.fitness)