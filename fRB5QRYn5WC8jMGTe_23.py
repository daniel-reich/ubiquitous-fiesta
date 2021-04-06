
from datetime import datetime, timedelta
def time_difference(city_a, timestamp, city_b):
  zone = {"Los Angeles":-8, "New York":-5, "Caracas":-4.5, "Buenos Aires":-3, "London":0, "Rome":1, "Moscow":3, "Tehran":3.5, "New Delhi":5.5, "Beijing":8, "Canberra":10}
​
  mths = ["January","February","March","April","May","June","July","August","September","October","November","December"]
  mths_n = {mths[i]:i+1 for i in range(12)}
  n_mths = {v:k for k,v in mths_n.items()}
  
  d_info = timestamp.split(" ")
  
  dati_a = datetime(int(d_info[2]), mths_n[d_info[0]],int(d_info[1][:-1]),int(d_info[3][:2]),int(d_info[3][-2:]),0)
  dati_b = dati_a + timedelta(hours = zone[city_b]-zone[city_a])
​
  return dati_b.strftime("%Y-%-m-%-d %H:%M")

