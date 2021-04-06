
def longer_than_n_pages(pages):
  c.execute("SELECT * From Book WHERE Pages > ?", (pages,))
  books = c.fetchall()
  print (books)
  return books

