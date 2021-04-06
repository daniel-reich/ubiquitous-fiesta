
def three_letter_collection(s):
    return sorted(s[idx:idx+3] for idx, letter in enumerate(s[:-2])) if len(s) > 2 else []

