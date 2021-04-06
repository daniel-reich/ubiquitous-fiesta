
def hidden_anagram(text, phrase):
    T = [ch for ch in text.lower() if ch.isalpha()]
    P = [ch for ch in phrase.lower() if ch.isalpha()]
    check = len(P)
    for i in range(len(text)-check):
        if sorted(T[i:i+check]) == sorted(P):
            return ''.join(T[i:i+check])
    return "noutfond"

