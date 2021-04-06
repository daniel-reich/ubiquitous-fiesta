
def empty_sq(step):
    if step == 1:
        return 0
    else:
        diag = 2*step
        dot = 4*step
        space = diag**2
        return space - dot
       # total = 0
       # for i in range(diag):
        #    total = total + diag
       # print(total)
        ##space = diag+ 2*total
        return space - dot
print(empty_sq(3))

