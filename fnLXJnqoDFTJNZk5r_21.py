
def sort_contacts(names, sort):
  if not names:
    return []
  if sort == "ASC":
    arrange = sorted(sorted(x.split(' ') for x in names), key=lambda x: x[1][0])
    return [' '.join(x for x in y) for y in arrange]
  else:
    arrange = sorted(sorted(x.split(' ') for x in names), key=lambda x: x[1][0], reverse=True)
    return [' '.join(x for x in y) for y in arrange]

