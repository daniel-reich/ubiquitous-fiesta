
def letter_at_position(n):
    if int(n) != n or n < 1 or n > 26:
        return "invalid"
    return chr(int(n) + 64).lower()

