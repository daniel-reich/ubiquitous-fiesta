
def overlap(w1,w2):
 if w1==w2:
     return w1
 else:
     for i in range(len(w1)):
         for j in range(len(w2)):
            if w1[i:]==w2[:j]:
               return (w1[:i]+w2)
     return w1+w2

