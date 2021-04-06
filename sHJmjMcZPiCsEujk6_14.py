
PI = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
​
def pilish_string(txt, i=0):
  return "" if txt == "" or i == 15 else (txt[:PI[i]].ljust(PI[i], txt[-1]) + " " + pilish_string(txt[PI[i]:], i + 1)).strip()

