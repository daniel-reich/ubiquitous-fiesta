
def splitBunches(bunches):
    return [{"name": d["name"], "quantity": 1} for d in bunches
            for _ in range(1, d["quantity"] + 1)]

