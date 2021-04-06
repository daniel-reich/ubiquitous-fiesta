
def oddish_or_evenish(num):
    return "Oddish" if sum(int(i) for i in str(num))%2 else "Evenish"

