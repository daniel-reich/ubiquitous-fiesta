
def fact_of_fact(n):
    factorial = 1
    for i in range(n):
        for j in range((i+1)):
            factorial *= (j+1) 
    
    return factorial

