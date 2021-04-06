
def pig_latin(txt):
  result = []
  for word in txt[:-1].lower().split(' '):
    if word[0] in 'aeiou':
      result.append(word + 'way')
    else: 
      result.append(word[1:] + word[0] + 'ay')
  result = ' '.join(result)
  result = result.capitalize()
  result += txt[-1]
  return result

