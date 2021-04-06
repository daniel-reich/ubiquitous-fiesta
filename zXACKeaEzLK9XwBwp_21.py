
def split_bunches(bunches):
    result = []
    for element in bunches:
        for i in range(element["quantity"]):
            result.append({"name":element["name"], "quantity": 1})
    return result

