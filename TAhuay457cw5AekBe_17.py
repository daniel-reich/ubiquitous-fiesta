
def monkey_talk(s):
    a = ["eek" if i[0].lower() in "aeiou" else "ook"for i in s.split()]
    return " ".join(a).capitalize() + "."

