
def is_exact(n, prod=1, k=1):
    return (is_exact(n, prod * k, k + 1) if prod < n
            else ([n, k - 1] if prod == n else 'Not exact!'))

