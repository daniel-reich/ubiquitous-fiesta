
def make_sandwich(ingredients, flavour):
    sandwich = []
    for i in ingredients:
        sandwich += ['bread', i, 'bread'] if i == flavour else [i]
    return sandwich

