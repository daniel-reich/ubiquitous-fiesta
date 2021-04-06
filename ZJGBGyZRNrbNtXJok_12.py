
import string
def nearest_vowel(c):
    chars = string.ascii_lowercase
    indexc = chars.index(c)
    nearest = min([abs(chars.index(c) - chars.index(i)) for i in 'aeiou'])
    nearl = chars[indexc - nearest]
    try:
        nearr = chars[indexc + nearest]
    except:
        nearr = nearl
    return nearl if nearl in 'aeiou' else nearr

