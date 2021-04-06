
def find_vertex(x):
    x,y,z= [int(str(i.replace('x',''))) for i in x.replace('+','').split()]
    return -y//(2*x)

