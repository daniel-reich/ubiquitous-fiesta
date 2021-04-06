
def comments_correct(s):
  s1=list(s)
  s2=s1
  for i in range(len(s1)):
​
      for j in range(i+1,len(s2)):
          if(s1[i]== s2[j]):
​
              s2[i]=0
              s2[j]=0
              break
  if('/' in s2 or '*' in s2):
      return False
  else:
      return True

