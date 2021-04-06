
def polybius(text):
  letters = {1: {1: 'a', 2:'b', 3:'c', 4:'d', 5:'e'}, \
    2: {1:'f', 2:'g', 3:'h', 4:'i,j', 5:'k'}, \
    3: {1:'l', 2:'m', 3:'n', 4:'o', 5:'p'}, \
    4: {1:'q', 2:'r', 3:'s', 4:'t', 5:'u'}, \
    5: {1:'v', 2:'w', 3:'x', 4:'y', 5:'z'}}
  codes = text.split(' ')
  sent = ''
  if codes[0].isdigit():
    for word in codes:
      w = ''
      i = 0
      while i < len(word):
        letter = word[i:i+2]
        num1 = int(letter[0])
        num2 = int(letter[1])
        if letters[num1][num2] != 'i,j':
          sent += letters[num1][num2]
        else:
          sent += 'i'
        i += 2
      if len(codes) > 1 and word != codes[-1]:
        sent += ' '
  else:
    for word in codes:
      c = ''
      for l in word:
        if l.lower() != 'i' and l.lower() != 'j':
          for num1 in letters:
            for num2 in letters[num1]:
              if letters[num1][num2] == l.lower():
                sent += str(num1) + str(num2)
        else:
          sent += '24'
      if len(codes) > 1 and word != codes[-1]:
        sent += " "
        
  return(sent)

