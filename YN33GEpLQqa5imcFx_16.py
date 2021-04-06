
def pascals_triangle(row):
 def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
 return "".join([str(int((fact(row))/(fact(i)*fact(row-i)))) + " " for i in range(row+1)]).strip()

