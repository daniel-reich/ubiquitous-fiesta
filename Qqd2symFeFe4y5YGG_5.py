
def palindromic_date(date):
    d, m, y = date.split('/')
    return d + m + y == y[::-1] + m[::-1] + d[::-1] and d + m + y == m + d + y

