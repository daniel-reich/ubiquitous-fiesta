
def reverse_words(words):
    a = words.split(" ")
    c = ""
    for i in range(len(a)-1, -1, -1):
        c += a[i] + " "
    return c[0:len(c)-1]

