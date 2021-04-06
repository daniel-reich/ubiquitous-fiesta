
def vertical_txt(txt):
  try:
    lst = txt.split(" ")
    size = max([len(word) for word in lst])
    array = [[" " for i in range(len(lst))] for j in range(size)]
​
    col = 0
    for word in lst:
      row = 0
      for letter in word:
        array[row][col] = letter
        row += 1
      col += 1
​
    return array
  except IndexError:
    return size

