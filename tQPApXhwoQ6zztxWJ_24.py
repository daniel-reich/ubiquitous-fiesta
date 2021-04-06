
def get_prices(lst):
       a=[]
       for x in lst:
              b=''
              for y in x:
                     if y.isdigit()or y=='.':
                            b+=y
              a.append(float(b))
       return a

