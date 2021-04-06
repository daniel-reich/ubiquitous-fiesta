
def euclidean(a, b):
    if(b==0): 
        return a 
    else: 
        return euclidean(b,a%b)

