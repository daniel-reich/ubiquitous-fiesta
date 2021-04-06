
import ast
​
def recurSol(net):
    if type(net) == list:
        temp = []
        for i in range(len(net)):
            if type(net[i]) == int:
                temp.append(net[i])
            else:
                temp.append(recurSol(net[i]))
        a = 0
        for i in range(len(temp)):
            a += 1/temp[i]
        return round(1/a,1)
    else:
        temp = []
        for i in range(len(net)):
            if type(net[i]) == int:
                temp.append(net[i])
            else:
                temp.append(recurSol(net[i]))   
        return sum(temp)
    
def resist(net):
    net = ast.literal_eval(net)
    
    return recurSol(net)

