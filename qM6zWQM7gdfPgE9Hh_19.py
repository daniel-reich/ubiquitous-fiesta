
def filter_by_rating(d, rating):
    result = {i:d[i] for i in d if d[i] == rating }
    return "No results found" if len(result) == 0 else result

