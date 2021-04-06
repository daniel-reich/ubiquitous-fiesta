
def upward_trend(lst):
    x=[0]
    for i in lst:
        if i==str(i):
            return "Strings not permitted!"
        elif i>x[-1]:
            x.append(i)
    return x[1:]==lst

