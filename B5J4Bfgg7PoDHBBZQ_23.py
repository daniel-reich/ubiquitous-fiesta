
def line_eq(p1, p2):
    #if x = cnt
    if p1[0] == p2[0]:
        return p1[0]
​
    def y(x):
        return x*(p1[1] - p2[1])/(p1[0] - p2[0]) + p1[1] - p1[0]*(p1[1] - p2[1])/(p1[0] - p2[0])
​
    return y
​
def same_side(p1, p2, line):
    #if x = cnt 
    if isinstance(line, int):
        return (p1[0] >= line and p2[0] >= line) or (p1[0] >= line and p2[0] >= line)
​
    if (p1[1] >= line(p1[0]) and p2[1] >= line(p2[0])) or (p1[1] <= line(p1[0]) and p2[1] <= line(p2[0])):
        return True
    return False
​
def within_triangle(p1, p2, p3, test):
    line1 = line_eq(p1, p2)
    line2 = line_eq(p1, p3)
    line3 = line_eq(p2, p3)
​
    if same_side(p1, test, line3) and same_side(p2, test, line2) and same_side(p3, test, line1):
        return True
    return False

