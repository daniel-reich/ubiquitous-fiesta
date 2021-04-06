
def longer_than_n_pages(pages):
  return c.execute("SELECT * FROM Book WHERE Pages > ?",(pages,)).fetchall()

