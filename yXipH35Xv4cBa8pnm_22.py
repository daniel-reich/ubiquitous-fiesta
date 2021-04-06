
def microwave_buttons(t):
    m, sec = list(map(int, t.split(":")))
    total_sec = m * 60 + sec
    press_30, press_digits = float("inf"), float("inf")
    if not total_sec % 30:
        press_30 = total_sec // 30
    if m > 9:
        press_digits = 4
    elif m > 0:
        press_digits = 3
    elif sec > 9:
        press_digits = 2
    elif sec > 0:
        press_digits = 1
    else:
        press_digits = 0
    return min(press_30, press_digits) + 1

