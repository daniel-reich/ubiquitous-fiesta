
def find_triangles(lst):
  return sum(sum((a-c)**2+(b-d)**2==(a-e)**2+(b-f)**2 and (a-c)*(b-f)-(b-d)*(a-e)!=0 for (c,d) in lst for (e,f) in lst if (c,d)!= (e,f)) for (a,b) in lst)//2

