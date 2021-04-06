
import re
def sort_by_letter(lst):
  return sorted(lst, key=lambda x: re.search(r"[a-zA-Z]", x).group(0))

