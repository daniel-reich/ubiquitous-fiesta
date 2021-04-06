
def grid_pos(lst):
    def factorial(x):
        if x<=1:
            return 1
        return x*factorial(x-1)
    return factorial(sum(lst))/factorial(lst[0])/factorial(lst[1])

