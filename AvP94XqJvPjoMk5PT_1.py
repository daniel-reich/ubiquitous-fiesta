
def unique_styles(albums):
  return len({s for a in albums for s in a.split(',')})

