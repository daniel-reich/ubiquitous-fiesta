
def sig_figs(num):
    result = 0
    trail_nums = False
    zeros = 0
    for dig in num:
        if not dig == "." and not dig == "-":
            if not dig == "0":
                if zeros:
                    result += zeros + 1
                    zeros = 0
                else:
                    result += 1
                trail_nums = True
            elif trail_nums and "." in str(num):
                result += 1
            elif dig == "0" and not "." in str(num) and trail_nums:
                zeros += 1
    return result

