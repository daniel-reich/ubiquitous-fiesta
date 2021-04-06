
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def count_animals(txt):
    totals = []
    for i in range(len(animals)):
        totals.append(check(txt[i:]))
    return max(totals)
​
def check(txt):
    counter = 0
    txt2 = txt
    for i in animals:
        while True:
            for letter in i:
                if letter in txt2:
                    txt2 = txt2.replace(letter,'',1)
            if len(txt2) + len(i) == len(txt):
                txt = txt2
                counter += 1
            else:
                break
    return counter

