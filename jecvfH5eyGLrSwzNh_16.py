
animals = ["muggercrocodile", "one-hornedrhino", "python", "moth", "monitorlizard", "bengaltiger"]
​
def fauna_number(txt):
    parts = txt.replace('and', ',').replace('.', '').split(',')
    ans = []
    for part in parts:
        split = part.split()
        for animal in animals:
            if animal in split:
                idx = split.index(animal)
                ans.append((animal, split[idx-1]))
                break
    return ans

