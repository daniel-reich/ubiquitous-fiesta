
def check(d1, d2, k):
 a = (list(d1.keys())+list(d2.keys())).count(k)
 #try:
 if a==1:
   return "One's empty"
 #except: pass
 #try:
 if d1[k]==d2[k]:
   return True
 #except : pass
 #try:
 if d1[k]!=d2[k]:
   return "Not the same"
 #except : pass

