
def puzzle_pieces(a1, a2):
   x = len(a1)
   y = len(a2)
   if(x != y):
      return(False)
   val = a1[0] + a2[0]
   for i in range(len(a1)):
      print(str(a1[i]) + " " + str(a2[i]))
      if a1[i] + a2[i] != val:
         return(False)
   return(True)

