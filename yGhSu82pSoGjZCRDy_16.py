
def seesaw(num):
    if not isinstance(num, int):  return "balanced"
    num = str(num)
    left,right = num[:len(num)//2], num[len(num)//2+(len(num)%2):]
    return "balanced" if left==right else "right" if left<right else "left"

