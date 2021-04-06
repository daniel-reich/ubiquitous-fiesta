
def unique_styles(albums):
  return len(set(j for i in albums for j in i.split(',')))

