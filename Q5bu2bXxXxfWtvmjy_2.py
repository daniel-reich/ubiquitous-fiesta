
def missing_letter(txt):
  res = {chr(i) for i in range(ord(txt[0]),ord(txt[-1])+1)} - set(txt)
  return res.pop() if res else 'No Missing Letter'

