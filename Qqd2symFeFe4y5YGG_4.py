
def palindromic_date(date):
    dstring = ''.join(date.split('/'))
    return bool(dstring == dstring[::-1] and date[0:2] == date[3:5])

