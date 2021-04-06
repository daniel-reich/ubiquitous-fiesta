
def tidy_books(lst):
  output = []
  for i in lst:
    cleaned = i[0].strip()
    book = []
    dash = cleaned.find('-')
    book.append(cleaned[:dash-1])
    book.append(cleaned[dash + 2:])
    output.append(book)
  return output

