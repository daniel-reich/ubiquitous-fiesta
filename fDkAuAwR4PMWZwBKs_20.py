
def find_bob(names):
  return [i for i,ii in enumerate(names) if ii == "Bob"][0] if "Bob" in names else - 1

