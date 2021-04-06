
def rotate_transform(lst, num):
    result = []
    for _ in range(len(lst)):
        result.append(["0" for _ in range(len(lst))])
    if num == 0:
        return lst
    if num == -1:
       for i in range(len(lst)):
          for j in range(len(lst)):
              result[i][j] = lst[j][len(lst) - i - 1]
       return result
    elif num < -1:
        return rotate_transform(rotate_transform(lst, -1), num+1)
    elif num == 1:
        for i in range(len(lst)):
            for j in range(len(lst)):
                result[j][len(lst)-i-1] = lst[i][j]
        return result
    elif num > 1:
        return rotate_transform(rotate_transform(lst, 1), num-1)

