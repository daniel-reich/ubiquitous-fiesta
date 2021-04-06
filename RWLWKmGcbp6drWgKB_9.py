
def chosen_wine(wines: list):
    if len(wines) == 0:
        return None
    elif len(wines) == 1:
        return wines[0]['name']
    else:
        wines.sort(key=lambda x: x['price'])
        return wines[1]['name']

