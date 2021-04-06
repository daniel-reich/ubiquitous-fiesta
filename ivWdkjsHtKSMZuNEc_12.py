
def findShortestWords(txt):
  split_list = txt.replace(",", "").replace(".", "").replace("%", "").lower().split()
  min_length = len(min(split_list, key=len))
  return sorted([each for each in split_list if (len(each) == min_length and not each.isnumeric())])

