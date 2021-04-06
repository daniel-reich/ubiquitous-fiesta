
def common_last_vowel(txt):
  d = {'a':0,'e':0,'i':0,'o':0,'u':0}
  lst = [findVowels(i[::-1]) for i in txt.split()]
  for i in lst:
    d[i[0]]+=1
  return [i for i in d if d[i]==max(d.values())][0]
  
def findVowels(s):
  return ''.join([i.lower() for i in s if i.lower() in 'aeiou'])

