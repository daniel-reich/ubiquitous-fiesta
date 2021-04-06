
def within_triangle(p1, p2, p3, test):
    d = dict(zip('p1 p2 p3'.split(),(p1,p2,p3)))
​
    x = [[k] + [v] for k, v in d.items()]
    x.sort(key= lambda y: y[1])
    y = [[k] + [v] for k, v in d.items()]
    y.sort(key= lambda y: y[1][1])
    
    q1, q2, q3 = x[0][1], x[1][1], x[2][1]    
    f12 = lambda x: q1[1]+ (q2[1]-q1[1])/(q2[0]-q1[0])*(x-q1[0])
    f13 = lambda x: q1[1]+ (q3[1]-q1[1])/(q3[0]-q1[0])*(x-q1[0])
    f23 = lambda x: q2[1]+ (q3[1]-q2[1])/(q3[0]-q2[0])*(x-q2[0])
          
    if test[0] >= x[0][1][0] and test[0] <= x[1][1][0]:
        if test[1] >= f12(test[0]) and test[1] >= f13(test[0]):
            return False
        elif test[1] <= f12(test[0]) and test[1] <= f13(test[0]):
            return False
        else:
            return True
        
    elif test[0] >= x[1][1][0] and test[0] <= x[2][1][0]:
        if test[1] >= f23(test[0]) and test[1] >= f13(test[0]):
            return False
        elif test[1] <= f23(test[0]) and test[1] <= f13(test[0]):
            return False
        else:
            return True
    
    else: 
        return False

