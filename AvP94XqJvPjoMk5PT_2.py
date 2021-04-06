
def unique_styles(albums):
  unique = set()
  for album in albums:
    for style in album.split(','):
      unique.add(style)
  return len(unique)

