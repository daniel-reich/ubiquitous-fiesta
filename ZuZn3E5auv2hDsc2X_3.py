
# Return the `Title` and `Pages` of books which **strictly** have
# a greater number of pages than the given argument.
​
def longer_than_n_pages(pages):
  c.execute("SELECT * From Book WHERE Pages > ?", (pages,))
  books = c.fetchall()
  return books

