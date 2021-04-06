
def count_d(sentence):
   sum=0
   for i in range(len(sentence)):
      if sentence[i]=='d':
         sum+=1
      if sentence[i]=='D':
         sum+=1
   return sum

