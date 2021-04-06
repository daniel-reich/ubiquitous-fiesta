
def is_disarium(n):
    return sum([int(str(n)[x])**(x+1) for x in range(len(str(n)))]) == n

