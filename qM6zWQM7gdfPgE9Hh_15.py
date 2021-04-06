
def filter_by_rating(d, rating):
    d_res={}
    for key,value in d.items():
        if value==rating:
            d_res[key]=value
    if len(d_res)>0:
        return d_res  
    else:
        return "No results found"

