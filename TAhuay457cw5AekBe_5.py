
from re import sub
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
def monkey_talk(txt):
    return "{}.".format(sub(r"^[eo]", lambda m: m.group().upper(),
                            sub(r"[A-Za-z]+",
                                lambda m: "eek" if m.group()[0] in vowels
                                else "ook", txt)))

