
def help_bobby(n):  
    return [[int(i == j or i+j+1 == n) for j in range(n)] for i in range(n)]

