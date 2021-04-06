
def clean_up(files, sort):
   pre=[]
   su=[]
   final=[]
   for i in files:
     a,b=i.split(".")
     pre.append(a)
     su.append(b)
   prefix=list(set(pre))
   suffix=sorted(list(set(su)),key=lambda x :len(x),reverse=True)
   if sort =="prefix":
       for i in  prefix :
          ajout=[]
          for j in  files:
            if i in j :
              ajout.append(j)
          final.append(ajout)
       return sorted(final)
   else:
     for i in suffix:
       ajout=[]
       for j in files:
         if i in j:
           ajout.append(j)
       final.append(ajout)  
     return final

