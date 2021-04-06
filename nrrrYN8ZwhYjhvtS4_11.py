
def extend_vowels(word, num):
  return 'invalid' if num%1 or num<0 else ''.join(i*(num+1) if i in 'aeiouAEIOU' else i for i in word )

