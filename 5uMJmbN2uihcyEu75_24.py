
def weekly_salary(hours):
    return (sum(h * 10 + ((h - 8) * 5 if h > 8 else 0) for h in hours[:5]) +
            2 * sum(h * 10 + ((h - 8) * 5 if h > 8 else 0) for h in hours[5:]))

