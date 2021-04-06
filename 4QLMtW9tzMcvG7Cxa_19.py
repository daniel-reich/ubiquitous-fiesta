
def resistance_calculator(resistors):
    prl, seq, prl0 = 0, 0, False
    for r in resistors:
        seq += r
        if not prl0:
            if not r:
                prl0 = True
                continue
            prl += 1 / r
    return [round(1 / prl if not prl0 else 0, 2), round(seq, 2)]

