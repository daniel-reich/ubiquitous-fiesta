
def upward_trend(lst):
  return ("Strings not permitted!" if [i for i in lst if type(i)==str]
          else all(lst[i] < lst[i+1] for i in range(len(lst)-1)))

