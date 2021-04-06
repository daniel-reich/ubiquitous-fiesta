
def keys_and_values(d):
  key_lst = sorted( x for x in d.keys())
  val_lst = [ d[y] for y in key_lst ]
  return [ key_lst, val_lst ]

