
def sort_authors(lst):
  def last_name(full_name):
    return full_name.split()[-1].lower()
  return sorted(lst, key = last_name)

