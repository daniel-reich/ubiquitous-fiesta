
def letters_only(s):
    return (all((c.isalpha() and c.islower()) or c == ' ' for c in s)
            if s else False)

