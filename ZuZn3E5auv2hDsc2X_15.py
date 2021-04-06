
def longer_than_n_pages(pages):
  num_pages = pages
  c.execute("select title, pages from book where pages > {}".format(num_pages))
  matches = c.fetchall()
  return matches

