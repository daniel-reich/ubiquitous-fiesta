
from datetime import datetime 
from datetime import timedelta 
​
def time_difference(city_a, timestring, city_b):
​
    offsets = {"Los Angeles": -8, "New York": -5, "Caracas": -4.5, "Buenos Aires": -3, "London": 0, "Rome": 1, 
            "Moscow": 3, "Tehran": 3.5, "New Delhi": 5.5, "Beijing": 8, "Canberra": 10}
​
    time1 = datetime.strptime(timestring, "%B %d, %Y %H:%M") 
​
    time_diff = offsets[city_b] - offsets[city_a]
​
    new_time = time1 + timedelta(hours=time_diff)
​
    return new_time.strftime("%Y-%-m-%-d %H:%M")

