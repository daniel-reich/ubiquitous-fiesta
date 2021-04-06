
def gen_deck():
  suits = ["c", "d", "h", "s"]
  return [(x, z) for x in range(2, 15) for z in suits]

