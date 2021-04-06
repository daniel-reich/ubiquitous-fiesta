
def edabit_in_string(txt):
    word = "edabit"
    it = iter(txt)
    return "YES" if all(x in it for x in word) else "NO"

