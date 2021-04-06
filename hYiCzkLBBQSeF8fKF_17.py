
def count(deck):
    x = [2,3,4,5,6]
    z = [10, "J","Q","K","A"]
    return sum([1 for i in deck if i in x]) + sum([-1 for i in deck if i in z])

