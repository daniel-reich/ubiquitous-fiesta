
def edit_words(lst):
  return [fix(i) for i in lst]
​
def fix(s):
  return (s.upper()[:len(s)//2]+'-'+s.upper()[len(s)//2:])[::-1]

