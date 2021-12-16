class sphere:
    def __init__(self, lb:float, ub:float):
        self.lowerbound = lb
        self.upperbound = ub

    def evaluate(self, cells):
        #[1,2,3,4]
        # sphere = x[0]^2 + x[1]^2 + x[2]^2 + ... + x[n-1]^2
        #1*1 + 2*2 + 3*3 + 4*4
        summa = (cells * cells).sum()
        return summa
