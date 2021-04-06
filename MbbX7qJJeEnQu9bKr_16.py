
def max_occur(text):
    freqs = {c: text.count(c) for c in text if text.count(c) > 1}
​
    if not freqs:
        return 'No Repetition'
​
    return sorted(c for c in freqs if freqs[c] == max(freqs.values()))

