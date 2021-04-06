
def time_to_finish(str_finish, str_unfinish):
    x = str_finish.replace(" ", "")
    y = str_unfinish.replace(" ", "")
    return float((len(x) - len(y) ) * 0.5)
​
​
print(time_to_finish(
"As a result, my point is still valid.",
  "As a result, my"
))

