
def title_to_number(s):
  n=len(s)
  return sum((ord(s[::-1][i])-ord('A')+1)*26**i for i in range(n))

