
def simplify_sqrt(n):
    for i in range(1,n+1):
        if ((n / i)**(0.5)).is_integer():
            return (int((n/i)**(0.5)), i)

