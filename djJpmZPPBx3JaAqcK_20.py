
def twenty_power(n):
    i = 0
    result = []
    while i >= 0:
        if n / (20 ** i) >= 20:
            i += 1
        else:
            result= [(i, n // (20 ** i))]
            break
    if n == n // (20 ** i) * (20 ** i):
        return result
    else:
        return result + twenty_power(n - (n // (20 ** i)) * (20 ** i))
​
​
def maya_number(n):
    dict_maya = {0: "@", 1:"o", 2: "oo", 3: "ooo", 4: "oooo", 5: '-', 6: "o-", 7: "oo-",
                 8: "ooo-", 9: "oooo-", 10: "--", 11: "o--", 12: "oo--", 13: 'ooo--',
                 14: "oooo--", 15: "---", 16: 'o---', 17: "oo---", 18: "ooo---", 19: "oooo---"}
    final_result = []
    result = [twenty_power(n)[0]]
    for i in range(1, len(twenty_power(n))):
        if twenty_power(n)[i-1][0] - twenty_power(n)[i][0] == 1:
            result.append(twenty_power(n)[i])
        elif twenty_power(n)[i-1][0] - twenty_power(n)[i][0] > 1:
            for j in range(twenty_power(n)[i-1][0]-1, twenty_power(n)[i][0], -1):
                result.append((j, 0))
            result.append(twenty_power(n)[i])
    if twenty_power(n)[-1][0] == 1:
        result.append((0, 0))
    for j in range(len(result)):
            final_result.append(dict_maya[result[j][1]])
    return final_result

