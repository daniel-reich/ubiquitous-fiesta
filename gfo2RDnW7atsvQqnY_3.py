
def count_smileys(lst):
  from re import match
  return len([x for x in lst if match("[:;][-~]?[\)D]",x)])

