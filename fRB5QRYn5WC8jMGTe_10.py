
import datetime as dt
def time_difference(city_a, timestamp, city_b):
  gmt = {"Los Angeles": {"h": -8,"m":0},
    "New York": {"h":-5,"m":0},
    "Caracas": {"h":-4,"m":-30},
    "Buenos Aires": {"h":-3,"m":0},
    "London": {"h":0,"m":0},
    "Rome": {"h":1,"m":0},
    "Moscow": {"h":3,"m":0},
    "Tehran": {"h":3,"m":30},
    "New Delhi": {"h":5,"m":30},
    "Beijing": {"h":8,"m":0},
    "Canberra": {"h":10,"m":0}
  }
  t = dt.datetime.strptime(timestamp, "%B %d, %Y %H:%M")
  ot = (t - dt.timedelta(hours=gmt[city_a]["h"], minutes=gmt[city_a]["m"]) +
    dt.timedelta(hours=gmt[city_b]["h"], minutes=gmt[city_b]["m"]))
  return "{}-{}-{} {:02d}:{:02d}".format(ot.year, ot.month, ot.day,
    ot.hour, ot.minute)

