
def chosen_wine(wines):
    if len(wines)<1:
        return None
    return (sorted(wines,key=lambda x :x['price'],reverse=True)[-2]['name']) if len(wines)>1 else wines[0]['name']

