
def bug_jump(height, time):
    t = time /1000
    
    # y = x**2 / 4 ,  https://www.futurelearn.com/courses/maths-linear-quadratic/0/steps/12114
    x = 2 * (height ** 0.5)
    
    if 0 < t < x/2:
        return [round((-t**2+t*x),2), "up"] 
    
    elif x/2 < t < x:
        return [round((-t**2+t*x),2), "down"]
​
    else:
        return [0, None]

