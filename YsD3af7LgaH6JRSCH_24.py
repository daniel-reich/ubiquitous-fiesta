
def time_adjust(now, hrs, mins, sec):
    hours, minutes, seconds = map(int, now.split(':'))
    out = []
​
    out.append(str((seconds + sec) % 60).zfill(2))
    carry = (seconds + sec) // 60
    out.append(str((minutes + mins + carry)%60).zfill(2))
    carry = (minutes+mins+carry) // 60
    out.append(str((hrs + hours + carry) % 24).zfill(2))
    return ':'.join(out[::-1])

