
def split_bunches(bunches):
    ans = []
    for bunch in bunches:
        for _ in range(bunch["quantity"]):
            ans.append({"name": bunch["name"], "quantity": 1})
    return ans

