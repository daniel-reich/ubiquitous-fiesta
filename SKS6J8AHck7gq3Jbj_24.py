
import re
def tidy_books(lst):
  return [re.split(r" - ", re.sub(r"\s{2,}", "", lst[i][0])) for i in range(len(lst))]

