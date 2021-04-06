
def can_build(word1,word2):
  s=[]
  for i in ''.join(word1.split()):
    s.append(i in ''.join(word2.split()))
    print(s)
    word2=word2.replace(i,"",1)
  return min(s)!=False

