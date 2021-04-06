
def kaprekar(num, rounds = 1):
    if num == 6174:
        return 0
    ascending = sorted(list(str(num)))
    descending = sorted(list(str(num)), reverse=True)
    maxed = [int(''.join(ascending)),int(''.join(descending))]
    diff = max(maxed) - min(maxed)
​
    if diff  == 6174:
        return rounds
    elif diff < 1000:
        mod = list(str(diff))
        mod.append('0')
        return kaprekar(int(''.join(mod)), rounds=rounds+1)
    else:
        return kaprekar(diff, rounds=rounds+1)

