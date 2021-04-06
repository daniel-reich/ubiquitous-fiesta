
def microwave_buttons(time):
    minute, second = time.split(":")
    sec_button = (int(minute) + int(second)/60) / .5
    len_time = len(str(int(time[:2] + time[3:])))
    mn = min (sec_button, len_time)
    return mn + 1 if mn == mn//1 else len(second) + 1

