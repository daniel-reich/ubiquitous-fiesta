
import re
def superheroes(heroes):
  return sorted(h for h in heroes if re.search(r"(?<!wo)man$", h.lower()))

