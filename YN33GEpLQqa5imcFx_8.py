
def pascals_triangle(row):
  if (row ==1):
    return "1 1"
  else:
    list2 = "1"
    for k in range (1,row):
      elem = fact(row)/(fact(k)*fact(row-k))
      list2 +=" " + str(int(elem))
      list3  = list2 + " 1"
    return(list3)
        
def fact (a):
    if ( a == 1 or a == 0):
        return 1
    else:
        temp = 0
        res = 1
        while ( a !=1):
            temp = a
            res *= temp * ( temp-1)
            if ( a-2 == 0):
                break
            else:
                a -=2
    return(res)

