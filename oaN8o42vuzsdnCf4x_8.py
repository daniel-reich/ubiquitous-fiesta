
def best_words(lst):
  letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 2, 
  3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
​
  arr, brr = [], []
  for x in lst:
    score = 0
    for c in x:
      score += points[letters.index(c.upper())]
    arr.append([score, x])
  for w in arr:
    if w[0] == max(arr)[0]:
      brr.append(w[1])
  return brr

