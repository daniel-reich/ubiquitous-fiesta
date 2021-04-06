
def negative_sum(chars):
    result = []
    for i in range(len(chars)):
        if chars[i] == "-":
            j = 1
            while chars[i + j].isdigit():
                   if i + j == len(chars) - 1:
                       j += 1
                       break
                   else:
                       j += 1
            result.append(chars[i + 1: i + j])
    return sum(int(num) for num in result) * -1

