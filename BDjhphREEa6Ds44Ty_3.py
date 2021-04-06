
def bomb(l):
  
​
        def eq(x,y):
                eq1 = (x-l[0][0])**2 + (y-l[0][1])**2 == round((0.343*l[0][2])**2,0)
                eq2 = (x-l[1][0])**2 + (y-l[1][1])**2 == round((0.343*l[1][2])**2,0)
                eq3 = (x-l[2][0])**2 + (y-l[2][1])**2 == round((0.343*l[2][2])**2,0)
                return eq1 and eq2 and eq3
        x = 0
        while x<=50:
                y = 0
                while y<=50:
                        if eq(x, y):
                                return((x,y))
                                y+=1
                        else:
                                y+=1
                x+=1

