
def get_number_of_apples(n, p):
    applleft = int(n - (n * int(p.replace('%', ''))*.01))
    if applleft > 0:
        return applleft
    else:
        return 'The children didn\'t get any apples'

