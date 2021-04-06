
def sort_authors(lst):
  import re
  def ln(name):
    return re.findall(r"\w+",name)[-1].lower()
  return sorted(lst,key=ln)

