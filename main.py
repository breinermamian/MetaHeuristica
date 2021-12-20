import numpy as np
from hillclimbing import hillclimbing
from sphere import sphere
from step import step
from rastrigin import rastrigin
from schwefel import schwefel
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # myStep = step (-5.0, 5.0)
    # input = np.arrange(1,4);
    # result = myStep.evaluate(input)
    # print (result)

    # np.random.seed(5)
    '''
    myStep = sphere(-5.0, 5.0)
    myHC = hillclimbing(myStep, 3, 1000, 2, 2)
    [x, y] = myHC.evolve()

    
    np.random.seed(2)
    rastrigin = Rastrigin(-5.0, 5.0)
    myHC = hillclimbing(rastrigin, 2, 100, 0.5, 1)  # 2 Dimensones #penultimo es bandwitch
    [x2, y2] = myHC.evolve()



    mySphere = sphere(-5.0, 5.0)
    myHC = hillclimbing(mySphere, 2, 100, 0.5, 1)  # 2 Dimensones #penultimo es bandwitch
    [x1, y1] = myHC.evolve()

    
    np.random.seed(2)
    Myschwefel = schwefel(-5.0, 5.0)
    myHC = hillclimbing(Myschwefel, 2, 100, 0.5, 1)  # 2 Dimensones #penultimo es bandwitch
    [x, y] = myHC.evolve()
    np.random.seed(2)
    myRastrigin = rastrigin(-5.12, 5.12)
    myHC = hillclimbing(myRastrigin, 2, 100, 0.5, 2)
    [x, y] = myHC.evolve()'''
    mySphere = sphere(-5.0, 5.0)
    # Nuestro
    np.random.seed(1)
    myHC = hillclimbing(mySphere, 5, 500, 1, 2, 2)
    [x2, y2] = myHC.evolve()
    #Profe
    #np.random.seed(2)
    myHC = hillclimbing(mySphere, 5, 500, 1, 1, 1)  # 2 Dimensones #penultimo es bandwitch
    [x, y] = myHC.evolve()



    # plotting
    plt.title("Convergence curve")
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    # plt.plot(x, y, color="red")
    # plt.plot(x2, y2, color="green")
    plt.plot(x, y, color="green")
    plt.plot(x2, y2, color="black")
    plt.show()
