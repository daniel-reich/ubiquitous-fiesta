
import math 
from decimal import Decimal, ROUND_HALF_UP
​
def over_time(input_time_list):
​
    # See if you want to put checks for timings
    
    # input_time_list = [start_time, end_time, rate_hr, overtime_mul]
    
    # function -> 
    start_time = float(input_time_list[0])
    end_time = float(input_time_list[1])
    rate_hr = float(input_time_list[2])
    overtime_mul = float(input_time_list[3])
    
    pay = 0 
    
    if end_time < 17.00:
        normal_pay_time = end_time - start_time
    else:
        normal_pay_time = 17.00 - start_time
    
    if start_time < 17.00:
        overtime_hours = end_time - 17.00
    else:
        normal_pay_time = 0.0
        overtime_hours = end_time - start_time
        
    if end_time > 17.00:
        normal_pay = normal_pay_time * rate_hr 
        over_time_pay =  overtime_hours * overtime_mul * rate_hr
        pay = normal_pay + over_time_pay
    else:
        pay = normal_pay_time * rate_hr
        
        
    pay = Decimal(pay)
    pay = Decimal(pay.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)) 
    
    pay = "$%.2f" % (pay)
    
    return pay

