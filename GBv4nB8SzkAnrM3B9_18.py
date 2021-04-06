
def letter_counter(lst, letter):
  ans = 0
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if letter == lst[i][j]:
        ans += 1
  return ans

