
def mood_today(*mood):
    if len(mood)!=0:
        return "Today, I am feeling {}".format(*mood)
    else:
        return "Today, I am feeling neutral"

