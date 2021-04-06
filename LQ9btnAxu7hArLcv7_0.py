
def diagonalize(n, d):
  fcts = {\
            "ul": lambda x,y: x+y,\
            "ur": lambda x,y: n-x+y-1,\
            "ll": lambda x,y: n+x-y-1,\
            "lr": lambda x,y: 2*n-x-y-2\
          }
  return [[fcts[d](x, y) for x in range(n)] for y in range(n)]

