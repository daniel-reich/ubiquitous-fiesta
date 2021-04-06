
def filter_by_rating(d, rating):
    x = {i:v for i,v in d.items() if v == rating}
    return 'No results found' if not x else x

