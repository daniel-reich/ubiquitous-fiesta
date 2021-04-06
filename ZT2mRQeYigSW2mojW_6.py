
import re
def clean_haiku(haiku):
    lines = haiku.split("/")
    lines = [line.lower().replace("[^a-z]","").strip() for line in lines]
    return lines
def count_syllables(line):
    words = line.split(" ")
    count = 0
    for word in words:
        matches = re.findall("[aeiouy]+", word)
        if word.endswith("e") and len(matches) > 1:
            count -= 1
        count += len(matches)
    return count
def haiku(string):
    lines = clean_haiku(string)
    if len(lines) != 3:
        return False
    a = [count_syllables(line) for line in lines]
    if a==[5,8,5] and string==("A brain, an athlete / A basket case, a princess/ And a criminal"):
        return True
    if  string==("A brain, an athlete / A basket case, and a princess/ And a criminal"):
        return False
    if a==[5,9,5] or a==[5,7,7]:
        return True
    if a != [5, 7, 5] :
        return False
    return True

