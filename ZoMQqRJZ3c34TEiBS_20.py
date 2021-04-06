
import string
​
​
def playfair(txt, keyword):
  letters = ''.join(keyword.split()) + string.ascii_lowercase
  square_map = {}
  square = [['' for _ in range(5)] for _ in range(5)]
  row = column = 0
  for letter in letters:
    if letter in square_map:
      continue
    if letter == 'j':
      square_map[letter] = square_map['i']
      continue
    square_map[letter] = (row, column)
    square[row][column] = letter
    if column == 4:
      row += 1
    column = (column + 1) % 5
  text = [letter for word in txt.lower().split() for letter in word if letter.isalpha()]
  pairs = []
  cur_pair = []
  for letter in text:
    if not cur_pair or cur_pair[-1] != letter:
      cur_pair.append(letter)
    else:
      cur_pair.append('x')
      pairs.append(''.join(cur_pair))
      cur_pair = []
      cur_pair.append(letter)
    if len(cur_pair) == 2:
      pairs.append(''.join(cur_pair))
      cur_pair = []
  if cur_pair:
    pairs.append(cur_pair[0] + 'x')
  ciphered = []
  for pair in pairs:
    direction = -1 if txt.isupper() else 1
    letter1, letter2 = [square_map[letter] for letter in pair]
    if letter1[0] == letter2[0]:
      row = letter1[0]
      new_coords = [(coord + direction) % 5 for coord in (letter1[1], letter2[1])]
      new_pair = ''.join([
        square[row][column] for column in new_coords
      ])
    elif letter1[1] == letter2[1]:
      column = letter1[1]
      new_coords = [(coord + direction) % 5 for coord in (letter1[0], letter2[0])]
      new_pair = ''.join([
        square[row][column] for row in new_coords
      ])
    else:
      new_pair = square[letter1[0]][letter2[1]]
      new_pair += square[letter2[0]][letter1[1]]
    ciphered.append(new_pair)
  return ''.join(ciphered).upper()

