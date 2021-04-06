
def tap_code(text):
  table = [
    ["A","B","C","D","E"],
    ["F","G","H","I","J"],
    ["L","M","N","O","P"],
    ["Q","R","S","T","U"],
    ["V","W","X","Y","Z"],
  ]   
  text = text.upper().replace("K","C")
  print(text)
  x = 0
  y = 0
  taps = ""
  word = ""
  if "." in text:
    split = text.split()
    print(split)
    for i in range(len(split)):
      if i % 2 == 0:
        x = len(split[i])
      else:
        y = len(split[i])
        word = word + table[x-1][y-1]
    return word.lower()
  else:
    for c in text:
      for row in table:
        y = y + 1
        for letter in row:
          x = x + 1
          if c == letter:
            print(str(y) + ", " + str(x))
            for i in range(y):
              taps = taps + "."
            taps = taps + " "
            for i in range(x):
              taps = taps + "."
            taps = taps + " "
        x = 0
      y = 0
    return taps[:-1]

