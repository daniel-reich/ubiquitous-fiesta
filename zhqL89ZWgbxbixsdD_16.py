
def is_exact(n, f=1, i=1):
    return is_exact(n, f*i, i+1) if f<n else [f,i-1] if f==n else "Not exact!"

