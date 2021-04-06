
def sle(eq):
    # eq in form a*x + b*y = c
    eq1 = eq[0]
    eq2 = eq[1]
    
    # Make a1 and a2 the same but opposite values
    a1, a2 = eq1[0], eq2[0]
    
    # If both a1 and a2 are positive, make eq2 negative 
    if a1 > 0 and a2 > 0:
        eq2 = list(map(lambda a: a*(-1), eq2))
    
    eq1 = list(map(lambda a: a*a2, eq1))
    eq2 = list(map(lambda a: a*a1, eq2))
    
    # Add equations together, cancelling x out
    eq_sum = [n1 + n2 for n1,n2 in zip(eq1, eq2)]
    
    # Calculate x and y
    try:
        y = eq_sum[2]//eq_sum[1]
        x = (eq1[2] - eq1[1]*y)//eq1[0]
    except:
        return False
    return (x, y)

