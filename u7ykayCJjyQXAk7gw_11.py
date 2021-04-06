
animals = ["dog", "cat", "bat", "cock", "cow", "pig", 
  "fox", "ant", "bird", "lion", "wolf", "deer", "bear", 
  "frog", "hen", "mole", "duck", "goat"]
​
def count_animals(txt):
    count = []
    possible = [animal for animal in animals if all(letter in txt for letter in animal)]
    for i in range(len(possible)):
        ct = 0
        new_txt = txt
        for animal in possible:
            while all(letter in new_txt for letter in animal):
                ct += 1
                for char in animal:
                    new_txt = new_txt.replace(char, '', 1)
        count.append(ct)
        possible.append(possible.pop(0))
    return max(count)

