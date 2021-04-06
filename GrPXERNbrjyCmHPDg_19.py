
def duplicate_count(txt) :
   result=""
   for i in txt:
       if txt.count(i)>1:
           result+=i
   return(len(set(result)))

