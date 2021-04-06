
def longer_than_n_pages(pages):
    c.execute("SELECT * From Book WHERE Pages > ?", (pages,))
    return c.fetchall()

