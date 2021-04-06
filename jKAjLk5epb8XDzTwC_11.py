
def total_amount_adjectives(obj):
    count = 0
    for adj in obj.values():
        count += 1
    return count
​
​
print(total_amount_adjectives({"a": "moron"}))
print(total_amount_adjectives({"a": "idiot", "b": "idiot", "c": "idiot"}))
print(total_amount_adjectives({"a": "moron", "b": "scumbag", "c": "moron", 'd': "dirtbag"}))

