
def club_entry(word):
    set_letters = set()
    for c in word:
        if c not in set_letters:
            set_letters.add(c)
        else:
            return (ord(c) - 96) * 4
    return "no double letter:)"

