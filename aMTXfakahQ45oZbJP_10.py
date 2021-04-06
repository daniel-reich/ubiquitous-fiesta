
def complete_bracelet(lst):
 for n in range(len(lst)):
     if (lst[:n]==lst[-1:-(n+1):-1][::-1]) and n>1 and (lst[:n] * int(len(lst)/len(lst[:n])) == lst):
         return True
 return False

