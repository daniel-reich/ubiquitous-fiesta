
def ink_levels(inks):
  pages = -1
  for i in inks:
    if pages == -1 or inks[i] < pages:
      pages = inks[i]
  return pages

