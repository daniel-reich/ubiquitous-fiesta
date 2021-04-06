
def longer_than_n_pages(pages):
  c.execute("SELECT * FROM Book WHERE Pages > ?", (pages,))
  result = c.fetchall()
  return result

