
def average_index(letters):
  lst1 = [122-ord(character) for character in letters]
  lst2 = [26-i for i in lst1]
  return round(sum(lst2)/len(lst2),2)

