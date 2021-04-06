
from collections import OrderedDict
​
def chosen_wine(wines):
    if wines == []:
        return None
    if len(wines) == 1:
        return wines[0]['name']
    d = {x['name']:x['price'] for x in wines}
    od = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
    return list(od.keys())[1]

