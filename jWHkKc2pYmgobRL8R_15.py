
def distance_to_nearest_vowel(txt):
    parsed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
​
    indexs = [i for i , word in enumerate(txt) if word in vowels]
​
    for idx , letter in enumerate(txt):
      closest = min([abs(x - idx) for x in indexs])
      parsed.append(closest)
​
    return parsed

