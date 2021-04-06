
def filter_by_rating(d, rating):
    x={a:b for a, b in d.items() if b==rating}     
    if x=={}:
        return "No results found"
    else:
        return x

