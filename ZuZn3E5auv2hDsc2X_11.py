
def longer_than_n_pages(pages):
  c.execute("SELECT * FROM Book WHERE Pages > %d" % pages)
  return c.fetchall()

