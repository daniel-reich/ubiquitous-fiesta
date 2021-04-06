
def make_grlex(lst):
  def custom_key(string):
    return len(string), string.lower()
  return sorted(lst, key=custom_key)

