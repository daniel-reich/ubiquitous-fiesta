
def abbreviate(sentence, n=4):
        k = ""
        s = sentence.split(" ")
        for i in s:
            if len(i) >= n:
                k += i[0]
        return k.upper()

