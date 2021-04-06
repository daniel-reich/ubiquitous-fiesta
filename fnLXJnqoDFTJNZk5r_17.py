
def sort_contacts(names, sort):
  return sorted(names, key=lambda x: x.split( )[1], reverse=sort=='DESC') if names else []

