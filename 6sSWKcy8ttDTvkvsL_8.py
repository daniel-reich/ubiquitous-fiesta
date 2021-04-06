
def after_n_days(days, n):
    d = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    return [d[(d.index(x) + n)%7] for x in days]

