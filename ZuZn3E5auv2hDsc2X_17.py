
def longer_than_n_pages(pages):
  c.execute("SELECT Title, Pages From Book WHERE Pages > ?", (pages,))
  return c.fetchall()

