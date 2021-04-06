
def is_ladder_safe(ldr):
    if any(' ' in ldr[i] and ' ' in ldr[i+1] and ' ' in ldr[i+2] for i in range(len(ldr)-2)):
        return False
    if ldr[:len(ldr)//2] != ldr[len(ldr)//2+1:][::-1]:
        return False
    if len([i for i in ldr[:len(ldr)//2] if ' ' in i ]) % 2 == 0:
        return False
    for i in ldr:
        if len(i) < 5:
            return False
    return True

