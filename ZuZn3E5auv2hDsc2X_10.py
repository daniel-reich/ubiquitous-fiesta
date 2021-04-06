
def longer_than_n_pages(pages):
    c.execute('SELECT Title,Pages FROM Book WHERE pages>:pages',{'pages':pages})
    return c.fetchall()

