
def extend_vowels(word, num):
 if type(num) is int and num>0:
  listt=[letter for letter in word]
  return ''.join(list(map(lambda x:x*(num+1) if x in 'aeiuoAEIOU' else x, listt)))
 elif num==0:
   return word
 else:
   return 'invalid'

