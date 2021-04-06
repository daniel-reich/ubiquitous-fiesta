
def best_start(lst, word):
  letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
   "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 
  3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
  letter_to_points = {key: value for key, value in zip(letters, points)}
  word_values = [letter_to_points[letter.upper()] for letter in word]
  move = {}
  for i in range(len(lst) - len(word) + 1):
    word_score = 0
    multiplier = 1
    for j in range(len(word)):
      if lst[i+j] == 'DL':
        word_score += word_values[j] * 2
      elif lst[i+j] == 'TL':
        word_score += word_values[j] * 3
      elif lst[i+j] == 'DW':
        multiplier = 2
      else:
        word_score += word_values[j]
    move[i] = word_score * multiplier
  return max(move, key=move.get)

