
def sle(m):
        a,b,c,d,e,f = m[0][0],m[0][1],m[0][2],m[1][0],m[1][1],m[1][2]
        try:
                y = ((a*f) - (d*c)) / ((a*e) - (d*b))
                x = (c - (b*y)) / a
                return (x,y)
        except:
                return False

