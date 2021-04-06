
def no_yelling(phrase):
​
  phrase = phrase.split()
  word = ''
  for txt in phrase[-1]:
    if txt == '?':
      word+='?'
      break
    elif txt == '!':
      word+='!'
      break
    word+=txt
​
  remove = phrase.pop(-1)
  newphrase = ''
  for words in phrase:
    newphrase+=words+' '
  newphrase+=word
​
  return newphrase

