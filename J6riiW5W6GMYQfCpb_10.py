
def expensive_orders(d, k):
     list = {}
     for i in d:
          if (d[i] > k):
               list.update({ i : d[i] })
     return list

