
def chosen_wine(wines):
    if not wines:
        return None
    if len(wines) == 1:
        return wines[0]['name']
    cheap = sorted([wines[x]['price'] for x in range(len(wines))])[1]
    for x in wines:
        if cheap in x.values():
            return x['name']

