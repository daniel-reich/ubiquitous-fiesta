
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n >= 2:
        return n*factorial(n-1)
​
def pascals_triangle(n):
    row_as_list = []
    for k in range(n+1):
        number = factorial(n) / (factorial(k)*factorial(n-k))
        row_as_list.append(str(int(number)))
    row_as_string = " ".join(row_as_list)
    return row_as_string

