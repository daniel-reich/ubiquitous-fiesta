
def factory(n):
    
    def myFunc(x):
        for i in range(len(x)):
            x[i] = x[i] / n
        return x
        
    return myFunc

