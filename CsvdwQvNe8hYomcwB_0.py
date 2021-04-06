
def remap(val, l1, h1, l2, h2):
 if h1==l1:
   return 0
 return (h2-l2)* ((val-l1)/(h1-l1)) + l2

