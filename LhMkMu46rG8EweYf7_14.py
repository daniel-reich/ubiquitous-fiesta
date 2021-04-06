
def sort_by_letter(lst):
    return sorted(lst, key=lambda word: list(filter(str.isalpha, word)))

