
def ink_levels(inks):
  return inks.get(min(inks, key=inks.get))

