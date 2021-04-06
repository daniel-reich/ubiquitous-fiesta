
def longer_than_n_pages(pages):
  c.execute("SELECT * from Book where Pages > ?", (pages,))
  return c.fetchall()

