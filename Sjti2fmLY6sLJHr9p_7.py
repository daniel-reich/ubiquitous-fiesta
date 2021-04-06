
def look_and_say(start, n):
    terms, current_term = [start], str(start)
    for _ in range(n-1):
        tokens = [current_term[0]]
        for char in str(current_term)[1:]:
            if char == tokens[-1][0]: tokens[-1]+=char
            else: tokens.append(char)
        next_term = str()
        for tok in tokens: next_term += str(len(tok)) + tok[0]
        terms.append(int(next_term))
        current_term = next_term
    return terms

