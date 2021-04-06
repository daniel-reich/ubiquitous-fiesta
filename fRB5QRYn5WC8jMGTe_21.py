
from datetime import timedelta
from dateutil.parser import parse
​
GMT = {
  "Los Angeles": -480,
  "New York": -300,
  "Caracas": -270,
  "Buenos Aires": -180,
  "London": 0,
  "Rome": 60,
  "Moscow": 180,
  "Tehran": 210,
  "New Delhi": 330,
  "Beijing": 480,
  "Canberra": 600
}
​
def time_difference(city_a, timestamp, city_b):
  return (parse(timestamp) + timedelta(minutes=GMT[city_b]-GMT[city_a])).strftime("%Y-%-m-%-d %H:%M")

