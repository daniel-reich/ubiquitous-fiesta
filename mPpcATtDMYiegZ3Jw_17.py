
def right_triangle(x,y,z):
    if x <= 0 or y <= 0 or z <= 0:
        return False
   
    ls = []
    ls.append(x)
    ls.append(y)
    ls.append(z)
    ls.sort()
    
    return (ls[0]**2)+(ls[1]**2) == ls[2]**2
​
​
​
print(right_triangle(3, 4, 5))

