
def find_bob(names):
  xd = "Bob"
  try:
    position = names.index("Bob")
    return position
    
  except ValueError as xd:
    return -1

