
def split_and_delimit(txt, num, delimiter):
  new = ""
  for x in range(len(txt) // num):
    new += txt[x * num: x * num + num] + delimiter
  if len(txt) // num != len(txt) / num:
    new += txt[len(txt) // num * num:]
  if new[-1] == delimiter:
    new = new[:-1]
  return new

