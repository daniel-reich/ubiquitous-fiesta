
def worded_math(word):
  mydict = {'zero': '0', 'one': '1', 'two': '2', 0: 'Zero', 1: 'One', 2: 'Two', 'plus': '+', 'minus': '-'}
  
  return mydict[eval(''.join([mydict[x] for x in word.lower().split()]))]

