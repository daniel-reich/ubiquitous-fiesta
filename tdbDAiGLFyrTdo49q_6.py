
def find_difference(a, b):
    a_val=(a[0]*a[1]*a[2])
    b_val=(b[0]*b[1]*b[2])
    if(a_val>b_val):
        diff=a_val-b_val
    else:
        diff=b_val-a_val
  
    return diff

