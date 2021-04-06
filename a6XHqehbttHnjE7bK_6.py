
def is_repdigit(num):
    num = list(str(num))
    lis = []
    for i in range(len(num)):
        if i >= len(num)-1:
            break
        elif num[i] == num[i+1]:
            lis.append(True)
        else: lis.append(False)
    return False if False in lis else True

