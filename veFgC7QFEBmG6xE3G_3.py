
def is_smooth(sentence):
  book = {
    k: v
    for k, v in enumerate(sentence.lower())
  }
  spaces = [
    index
    for index, space in book.items()
    if space == ' '
  ]
  endings = [
    book.get(i - 1)
    for i in spaces
  ]
  beginnings = [
    book.get(i + 1)
    for i in spaces
  ]
  return beginnings == endings

