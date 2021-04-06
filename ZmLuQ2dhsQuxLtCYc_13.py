
from datetime import date
def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):
    if end_read < start_read: return "Invalid meter readings"
    
    # Days 
    un_sort_days = start_date.replace(","," ") + " " + end_date.replace(","," ")
    sorted_days = un_sort_days.split(" ")
    sorted_days = list(map(int,sorted_days))
    
    days = (date(sorted_days[3], sorted_days[4], sorted_days[5]) - 
            date(sorted_days[0], sorted_days[1], sorted_days[2]))
    
    if str(days.days).startswith("-"): return "Invalid date"
    day_standing = days.days * stand
    
    # Units
    meter_read = (end_read - start_read) * tariff
    
    unit_cost = day_standing + meter_read
    unit_cost_tax = unit_cost * 0.05
    return "$" + str(round(unit_cost_tax + unit_cost,2))

