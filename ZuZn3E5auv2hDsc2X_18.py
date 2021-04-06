
def longer_than_n_pages(pages):
  c.execute("SELECT Title, Pages FROM Book WHERE Pages > ?", (pages,))
  books = c.fetchall()
  return books

