
def halve_count(a, b, d=0):
    if b==0:
        return None
    if a <= b:
        return d-1
    else:
        return halve_count(a/2,b,d+1)

