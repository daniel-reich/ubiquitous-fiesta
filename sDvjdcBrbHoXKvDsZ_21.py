
def anagram(name, words):
    count = 0
    name = name.lower().replace(" ", "")
    for i in range(len(words)):
        for x in words[i]:
            if words[i].count(x) <= name.count(x):
                count += 1
​
    if count == len(name) and len(set(name)) == len(set("".join(words))):
        return True
    return False

