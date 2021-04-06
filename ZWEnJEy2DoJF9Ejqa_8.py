
def edabit_in_string(txt):
  string="edabit"
  j=0
  for i in range(len(txt)-1):
    if (string[j]==txt[i]):
      j+=1
    if (j==len(string)):
      return "YES"
  return "NO"

