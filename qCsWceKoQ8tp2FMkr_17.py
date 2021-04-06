
def is_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False
print(is_triangle(2, 3, 4))
print(is_triangle(3, 4, 5))
print(is_triangle(4, 3, 8))

