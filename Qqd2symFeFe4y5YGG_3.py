
def palindromic_date(date):
    res = ''.join([i for i in date if i.isdigit()])
    return res == res[::-1] and date[0:2] == date[3:5]

