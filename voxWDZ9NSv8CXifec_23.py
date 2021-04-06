
def lemonade(bills):
    counter = []
    for b in bills:
        change = b - 5
        if change > 0:
            idx = 0
            while change > 0 and idx < len(counter):
                if counter[idx] <= change:
                    change -= counter[idx]
                    counter = counter[:idx] + counter[idx + 1:]
                else:
                    idx += 1
            if change > 0:
                return False
        counter = sorted(counter + [b], reverse=True)
    return True

