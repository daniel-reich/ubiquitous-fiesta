
def dif_ciph(inpt):
    if isinstance(inpt, str):
         lst=[ord(inpt[0])]
         for i in range(len(inpt[1:])):
             n=ord(inpt[i+1])-ord(inpt[i])
             lst.append(n)
         return lst
    elif isinstance(inpt, list):
         ultimate=[]
         res=[inpt[0]]
         for i in inpt[1:]:
             n=res[-1]+i
             res.append(n)
         for i in res:
             ultimate.append(chr(i))
         return "".join(ultimate)

