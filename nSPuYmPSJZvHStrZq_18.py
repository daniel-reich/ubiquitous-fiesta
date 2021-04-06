
def oddeven(lst):
    result = 0
    for x in lst:
      if (x%2==0):
        result-=1
      else:
        result+=1
    return result>0

