
def d(a, b):
    return pow((a[0]-b[0])**2 + (a[1]-b[1])**2, .5)
​
def perimeter(lst):
    return round(sum([d(lst[i], lst[(i+1)%3]) for i in range(3)]), 2)

