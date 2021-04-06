
def nearest_vowel(s):
    closest_vowel = [abs(ord(s) - ord('a')), 'a']
    for vowel in 'eiou':
        distance = abs(ord(s) - ord(vowel))
        if distance < closest_vowel[0]:
            closest_vowel[0] = distance
            closest_vowel[1] = vowel
    return closest_vowel[1]

