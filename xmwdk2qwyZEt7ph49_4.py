
def get_length(lst):
  new_lst = []
  def get_newlenght(lst):
    for n in lst:
      if type(n) != list:
        new_lst.append(n)
      else:
        get_newlenght(n)
  get_newlenght(lst)
  return len(new_lst)

