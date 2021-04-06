
def quad_sequence(lst):
    return [lst[-1] +
            sum(j*lst[-3] -(2*j+1)*lst[-2] +(j+1)*lst[-1]
            for j in range(1, i+1))
            for i in range(1, len(lst) +1)]

