
def three_letter_collection(s):
  list=[]
  word=''
  for x in range(0,len(s)-2):
    for y in range(0,3):
      word=word+s[x+y]
    list.append(word)
    word=''
  list.sort()
  return list

