
def generate_rug(n):
    if n == 1: return [[0]] 
    return [[n//2]*n] + [[n//2]+row+[n//2]
           for row in generate_rug(n-2)] + [[n//2]*n]

