
def is_palindrome_possible(txt):
  lst=[]
  cnt=0
  for i in txt:
      lst.append([i,txt.count(i)])
  for i in lst:
      if i[1]%2!=0:
          cnt+=1
          if cnt>1:
              return False
              break
  return True

