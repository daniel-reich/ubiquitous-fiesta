
def unique_styles(albums):
  return len(set(sum([i.split(',') for i in albums], [])))

