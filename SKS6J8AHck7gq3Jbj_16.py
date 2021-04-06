
def tidy_books(lst):
  tidy_lst = []
  for info in lst:
    book_info = info[0].split('-');
    tidy_lst.append([book_info[0].strip(),book_info[1].strip()])
  return tidy_lst

