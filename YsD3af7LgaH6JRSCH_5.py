
def time_adjust(now, hr, min, sec):
    hr_now,min_now,sec_now = now.split(':')
    hr_later = int(hr_now) + hr
    min_later = int(min_now) + min
    sec_later = int(sec_now) + sec
​
    n_sec = sec_later // 60
    sec_final = sec_later % 60
    n_min = (min_later + n_sec) // 60
    min_final = (min_later + n_sec) % 60
    hr_final = (hr_later + n_min) % 24
​
    return str(hr_final).rjust(2, '0')+':' + str(min_final).rjust(2,'0') + ':' + str(sec_final).rjust(2, '0')

