
def skip_the_sugar(drinks):
​
    return [drink for drink in drinks if drink != "fanta" and drink != "cola"]
​
    # Alternative way
    # no_sugar_list = []
    # for drink in drinks:
    #     if drink != "fanta" and drink != "cola":
    #         no_sugar_list.append(drink)
    # return no_sugar_list
​
print(skip_the_sugar(["lemonade", "beer", "water"]))

