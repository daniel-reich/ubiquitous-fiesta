
string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def next_letter(s):
  if s == "Z":
    return "A"
  else:
    index = string.index(s)
    return string[index+1]
​
def next_letters(s):
  string = "Z"
  if not s:
    return "A"
  elif s.count("Z") == len(s):
    s = s.replace("Z","A")
    return s + "A"
  elif len(s) == 1:
    return next_letter(s)
  elif s[-1] != "Z":
    return s[:-1] + next_letter(s[-1])
  else:
    while s.endswith(string):
      string += "Z"
    k = len(string)
    string = string.replace("Z","A")
    string = string[:-1]
    return s[:-k] + next_letter(s[-k]) + string

