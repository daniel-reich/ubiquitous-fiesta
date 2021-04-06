
def replace_the(txt):
    final = ""
    string = txt.split()
    for i in range(len(string) - 1):
        if string[i] == "the":
            if string[i + 1][0] in ["a", "e", "i", "o", "u"]:
                string.pop(i)
                string.insert(i, "an")
            else:
                string.pop(i)
                string.insert(i, "a")
​
    for x in string:
        final += x + " "
​
    return final.rstrip(" ")

