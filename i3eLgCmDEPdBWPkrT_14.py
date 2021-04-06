
def limit_number(num, range_low, range_high):
    return num if range_low <= num <= range_high else range_low if num < range_low else range_high

