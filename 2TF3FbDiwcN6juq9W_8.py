
def days_in_month(m):
    if m in [4, 6, 9, 11]:
        return 30
    return 29 if m == 2 else 31
​
def days_until_2021(date):
    m, d, y = [int(_) for _ in date.split('/')]
    ans = days_in_month(m) - d + 1
    ans += sum([days_in_month(mo) for mo in range(m + 1, 13)])
    return "1 day" if ans == 1 else str(ans) + " days"

