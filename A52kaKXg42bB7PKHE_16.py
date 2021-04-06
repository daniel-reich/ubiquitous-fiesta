
def num_then_char(lst):
  leng= []
  all =[]
​
  for i in lst:
      # print(i)
      leng+= [len(i)]
      all+= i
​
  num= []
  abc= []
​
  for i in all:
      if type(i)== str: abc+=[i]
      else: num+=[i]
​
  # print(num)
  # print(abc)
  # sort()+abc.sort()
  all= sorted(num)+sorted(abc)
  # print(all)
  ans=[]
​
  for i in leng:
      ans+=[all[:i]]
      del all[:i]
      
  return ans

