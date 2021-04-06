
def describe_num(n):
  txt = "brilliant exciting fantastic virtuous heart-warming tear-jerking beautiful exhilarating emotional inspiring".split()
  num = [txt[x-1] for x in range(1,n+1) if n%x==0 and x <=10] 
  return "The most {} number is {}!".format(" ".join(num), n)

