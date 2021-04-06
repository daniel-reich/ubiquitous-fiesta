
def abbreviate(sentence, n=4):
  result = ""
  str_lst = sentence.split()
  for i in str_lst:
    if len(i) >= n:
      result += i[0]
  return result.upper()

