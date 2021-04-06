
def tallest_skyscraper(lst):
    count = len(lst)
    for i in lst:
        if sum(i) == 0:
            count -= 1
        else:
            return count

