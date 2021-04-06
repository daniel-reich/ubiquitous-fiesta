
def add_letters(a):
    s = sum(ord(ch)-96 for ch in a) % 26
    return 'z' if not s else chr(s + 96)

