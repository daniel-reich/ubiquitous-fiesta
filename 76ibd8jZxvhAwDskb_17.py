
def tallest_skyscraper(lst):
    for row in lst:
        if 1 in row:
            return len(lst) - lst.index(row)

