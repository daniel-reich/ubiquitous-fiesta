
def skip_the_sugar(drinks):
    ans = []
    for drink in drinks:
        if drink == "cola" or drink == "fanta":
            ans = ans
        else:
            ans.append(drink)
    return ans

