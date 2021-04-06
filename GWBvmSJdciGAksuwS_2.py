
def find_letters(word):
  a=[]
  for num in word:
    if num not in a and word.count(num)==1:
      a+=[num]
  return a

