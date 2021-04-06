
def oddish_or_evenish(num):
    return "Oddish" if sum([int(digit) for digit in str(num)]) % 2 else "Evenish"

