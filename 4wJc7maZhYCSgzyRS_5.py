
def two_product(arr, N):
    seen= set()
​
    for items in arr:
        comp= N/items
        seen.add(comp)
        if items in seen:
            if int(comp) in arr:
                return[ int(comp),items]

