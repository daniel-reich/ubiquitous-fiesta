
def total_points(guesses, word):
  point = 0
  for guess in guesses:
    word_list = list(word)
    c = 0
    for w in guess:
      if w in word_list:
        word_list.remove(w)
        c += 1
      else:
        c = 0
        break
    if c == 3: point += 1
    elif c == 4: point += 2
    elif c == 5: point += 3
    elif c == 6: point += 54
  return point

