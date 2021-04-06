
def same_line(lst):
    try:
        num1 = (lst[1][1] - lst[0][1]) / (lst[1][0] - lst[0][0])
        num2 = (lst[2][1] - lst[1][1]) / (lst[2][0] - lst[1][0])
    except:
        num1 = lst[1][0] - lst[0][0]
        num2 = lst[2][0] - lst[1][0]
  # but there are some mistakes
    return num1 == num2

