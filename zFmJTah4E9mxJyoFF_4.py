
def find_index(lst, str):
  resp = 0
  for len in lst:
    if len == str:
      return resp
    resp = resp + 1

