
def count_datatypes(*args):
  dic = {
    int : 0, str : 0, bool : 0, list : 0, tuple : 0, dict : 0
  }
  for x in args:
    dic[type(x)] += 1
  return [dic[int], dic[str], dic[bool], dic[list], dic[tuple], dic[dict]]

