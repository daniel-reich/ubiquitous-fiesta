
from datetime import datetime
​
def energy_bill(time1, time2, read1, read2, tariff, stand):
    days = (
        datetime(*map(int, time2.split(","))) -
        datetime(*map(int, time1.split(",")))
    ).days * stand
    if days < 0:
        return "Invalid date"
    meter = (read2 - read1) * tariff
    if meter < 0:
        return "Invalid meter readings"
    return "${}".format(round(1.05 * (days + meter), 2))

