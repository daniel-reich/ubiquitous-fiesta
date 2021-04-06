
animals = ["dog", "cat", "bat", "cock", "cow", "pig",
           "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
           "frog", "hen", "mole", "duck", "goat"]
​
from collections import Counter
from itertools import permutations
def count_animals(txt):
    cnt = Counter(txt)
    potential = [a for a in animals if all(c in cnt for c in a)]
    n_max = 0
    for p in permutations(potential):
        n_animals = 0
        tmp_cnt = cnt.copy()
        someone_found = True
        while someone_found:
            someone_found = False
            for animal in p:
                animal_in = True
                for c in animal:
                    if tmp_cnt[c] > 0:
                        tmp_cnt[c] -= 1
                    else:
                        animal_in = False
                        break
                if animal_in:
                    n_animals += 1
                    someone_found = True
        n_max = max(n_max, n_animals)
    return n_max

