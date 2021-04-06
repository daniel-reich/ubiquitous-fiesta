
def x_pronounce(sentence):
  lst=sentence.split(" ")
  res2=""
​
  for i in lst:
      res=""
      if i=='x':
          res+="ecks"+" "
          res2+=res
      elif i[0]=="x":
          res+="z"+i[1:]+ " "
          res2+=res
      elif 'x' in i:
          k=i.index('x')
          res+=i[0:k]+'cks'+i[k+1:]+" "
          res2+=res
      else:
          res2+=i+" "
  return res2.strip()

