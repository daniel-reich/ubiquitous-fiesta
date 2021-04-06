
def filter_by_rating(d, rating):
    answer = {x:d[x] for x in d if d[x] == rating}
    return answer if answer else 'No results found'

