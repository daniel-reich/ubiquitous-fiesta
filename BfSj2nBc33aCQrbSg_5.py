
def truncatable(n):
    rightstring = str(n)
    leftstring = str(n)
    right = []
    left = []
    if '0' in rightstring:
        return False
    for x in str(n):
        right.append(all(int(rightstring) % j for j in range(2, int(int(rightstring)**0.5)+1)) and int(rightstring) > 1)
        left.append(all(int(leftstring) % j for j in range(2, int(int(leftstring)**0.5)+1)) and int(leftstring) > 1)
        rightstring = rightstring[:-1]
        leftstring = leftstring[1:]
    if left.count(True) == len(left) and right.count(True) == len(right):
        return 'both'
    if right.count(True) == len(right):
        return 'right'
    if left.count(True) == len(left):
        return 'left'
    else:
        return False

