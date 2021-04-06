
def total_points(guesses, word):
  d = {3: 1, 4: 2, 5: 3, 6: 54}
  ans = 0
  for i in guesses:
    boo = True
    w1 = list(word)[:]
    for j in i:
      if j not in w1:
        boo = False
        break
      w1.remove(j)
    if boo:
      ans = ans + d[len(i)]
  return ans

