import math


class schwefel:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        #[2,5]
        #49
        #
        #print("cells: ",cells)
        #xCua= cells[0]*cells[0]
        #print("xCua: ",xCua)
        #variable = cells.sum()*cells.sum()
        #print("Var: ",variable)
        #summa = xCua + variable
        #print("Suma: ",summa)
        summa = 0
        for i in range(len(cells)):
            summa = summa + (math.pow(cells[0:i + 1].sum(), 2))
        return summa

