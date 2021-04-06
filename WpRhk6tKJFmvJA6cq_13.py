
import datetime
def manage_delays(train, dest, delay):
  if dest in train.destinations:
    a,b=map(int,train.expected_time.split(":"))
    a += delay//60; b += delay%60
    train.expected_time = "{}:{:0>2}".format(a+b//60,b%60)

