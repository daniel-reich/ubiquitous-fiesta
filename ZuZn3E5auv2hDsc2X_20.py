
def longer_than_n_pages(pages):
  c.execute("SELECT * From Book WHERE pages > ?", (pages,))
  Book = c.fetchall()
  return Book

