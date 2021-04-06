
def same_vowel_group(w):
    vowels = 'aeiou'
    used = []
    for x in w:
        used_v = []
        for y in x:
            for z in vowels:
                if y == z and z not in used_v:
                    used_v.append(z)
        used.append([x, sorted(used_v)])
    return [used[i][0] for i in range(len(used)) if used[i][1] == used[0][1]]

