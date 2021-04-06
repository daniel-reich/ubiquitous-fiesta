
def split(txt):
    balance = 0
    split_parentheses, curr = [], []
    opening, closing, balanced = "(", ")", 0
    for parenthesis in txt:
        curr.append(parenthesis)
        if parenthesis == opening:
            balance += 1
        else:
            balance -= 1
        if balance == balanced:
            split_parentheses.append("".join(curr))
            curr = []
    return split_parentheses

