
def split_bunches(lst_dict):
    res = []
    for di in lst_dict:
        splitted = {"name": di['name'], "quantity": 1}
        for _ in range(di['quantity']):
            res.append(splitted)
    return res

