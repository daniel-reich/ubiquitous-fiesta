
def straight_digital(number):
    if number<100:  return "Not Straight"
    number = str(number)
    if len(set(number))==1:  return "Trivial Straight"
    diff = int(number[1])-int(number[0])
    return "Not Straight" if any(int(y)-int(x)!=diff for x,y in zip(number, number[1:])) else diff

