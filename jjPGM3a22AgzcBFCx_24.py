
def decrypt(lst):
  x=lst
  a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  for i in range(len(x)):
    if i+1 not in x:
      return(a[i].upper())

