
def longest_nonrepeating_substring(txt):
  temp = ''
  ans = ''
  for i in range(len(txt)):
    for x in range(i, len(txt)):
      if txt[x] not in temp:
        temp += txt[x]
      else:
        break
    if len(temp) > len(ans):
      ans = temp
    temp = ''
  return ans

