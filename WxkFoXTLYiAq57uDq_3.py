
def find_and_remove(dct):
    ans = {}
    for item in dct:
        ans[item] = {}
        for article, price in dct[item].items():
            try:
                price = int(price)
                ans[item][article] = price
            except:
                pass
    return ans

