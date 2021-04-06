
def hours_passed(time1, time2):
    start = int(time1.split(':')[0])
    end = int(time2.split(':')[0])
    not_start = time1.split()[-1]
    not_end = time2.split()[-1]
    if time1 == '12:00 AM':
        start = 0
    if not_start == not_end and start == end:
        return 'no time passed'
    elif not_start == not_end and start != end:
        return str(abs(end - start)) + ' hours'
    elif not_start != not_end:
        if not_end == 'PM':
            return str(abs(end + 12 - start)) + ' hours'

