
def after_n_months(year, months):
    if not year:
        return 'year missing'
    if not months:
        return 'month missing'
    return year + months//12

