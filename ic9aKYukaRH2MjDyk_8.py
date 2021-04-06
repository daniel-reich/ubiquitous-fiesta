
#from operator import itemgetter
def sort_by_last(txt):
  lst=[]
  for word in txt.split():
    lst.append(word)
  def last_letter(s):
    return s[-1]
  sortedList = sorted(lst, key=last_letter)
  return ' '.join(sortedList)

