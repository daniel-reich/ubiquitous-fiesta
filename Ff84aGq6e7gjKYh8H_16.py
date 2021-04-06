
def minutes_to_seconds(time):
    mins, secs = map(int, time.split(':'))
    return secs+mins*60 if secs<60 else False

