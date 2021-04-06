
def ABA(s):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if s == "A":
        return s
    return ABA(letters[letters.find(s)-1]) + s + ABA(letters[letters.find(s)-1])

