
def filter_by_rating(d, rating):
    filtered = dict(filter(lambda x: x[1] == rating, d.items()))
    return filtered if filtered else 'No results found'

