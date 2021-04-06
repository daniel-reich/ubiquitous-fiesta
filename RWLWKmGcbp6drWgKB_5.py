
def chosen_wine(wines):
    wines = sorted(wines, key=lambda x: x['price'])
    if len(wines) == 0:
        return None
    elif len(wines) == 1:
        return wines[0]['name']
    else:
        return wines[1]['name']

