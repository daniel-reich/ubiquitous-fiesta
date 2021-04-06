
def f(A, c):
​
    import math
​
    c_sqr = pow(c, 2)
    A_COF = (4) * pow(A, 2)
​
    try:
        t_1 = (c_sqr - math.sqrt((pow(c_sqr, 2)) - (4 * A_COF))) / 2
        t_2 = (c_sqr + math.sqrt((pow(c_sqr, 2)) - (4 * A_COF))) / 2
​
        t_1 = round(math.sqrt(t_1), 3)
        t_2 = round(math.sqrt(t_2), 3)
    
    except ValueError:
        return "Does not exist"
​
    return [t_1, t_2]

