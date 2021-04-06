
def filter_by_rating(d, rating):
    lst = []
    for item,score in d.items():
        if score == rating:
            lst.append(item)
            
    if len(lst)>=1:
        return {item:rating for item in lst}
    else:
        return "No results found"

