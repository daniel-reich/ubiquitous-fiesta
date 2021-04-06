
def spiral_matrix(side, string):
  chars = list(string + '+'*(side**2))[:side**2]
  ans = [[chars.pop(0)]]
  mode = 0
  while chars:
    if mode == 0:
      ans = [row + [chars.pop(0)] for row in ans]
    if mode == 1:
      k = len(ans[0])
      ans.append(chars[:k][::-1])
      chars = chars[k:]
    if mode == 2:
      k = len(ans)
      start = chars[:k][::-1]
      ans = [[start.pop(0)] + row for row in ans]
      chars = chars[k:]
    if mode == 3:
      k = len(ans[0])
      ans = [chars[:k]] + ans
      chars = chars[k:]
    mode = (mode+1)%4
  return ans

