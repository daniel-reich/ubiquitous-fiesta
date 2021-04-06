
def nearest_vowel(s):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    distances = [abs(alpha.index(s) - alpha.index(i)) for i in 'aeiou']
    return 'aeiou'[distances.index(min(distances))]

