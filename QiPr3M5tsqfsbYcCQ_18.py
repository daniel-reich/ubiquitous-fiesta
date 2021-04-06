
def square_digits(n):
    a=str(n)
    b=0
    for i in a:
      b =str(b)+str(int(i)**2)
    return(int(b[1:]))

