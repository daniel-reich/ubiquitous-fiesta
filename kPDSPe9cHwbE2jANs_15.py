
def cards_needed(n):
    if n < 0:
        return "invalid"
    else:
        return (n*(3 * n +1) // 2)

