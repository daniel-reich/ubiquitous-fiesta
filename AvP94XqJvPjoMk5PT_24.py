
def unique_styles(albums):
  return len({style for album in albums for style in album.split(',')})

