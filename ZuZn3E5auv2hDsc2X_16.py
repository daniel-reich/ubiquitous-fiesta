
def longer_than_n_pages(pages):
    salary = 30000
    c.execute("SELECT * From Book WHERE Pages > ?", (pages,))
    return c.fetchall()

