
def duplicate_count(txt):
  txt_set = set(txt)
  return sum( 1 for c in txt_set if c.isalnum() and txt.count(c)>1 )

