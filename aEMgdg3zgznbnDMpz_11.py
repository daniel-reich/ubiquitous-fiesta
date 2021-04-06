
def rotated_words(txt):
 arr = ["H", "I", "N", "O", "S", "X", "W", "Z"]
 string = list(set(txt.split(" ")))
 return 0 if txt=="" else len([x for x in string if all(y in arr for y in list(x))])

