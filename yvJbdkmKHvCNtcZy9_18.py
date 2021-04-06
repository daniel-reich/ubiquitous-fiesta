
def is_disarium(n):
    var=str(n)
    return sum(int(var[i])**(i+1) for i in range(len(var)))== n

