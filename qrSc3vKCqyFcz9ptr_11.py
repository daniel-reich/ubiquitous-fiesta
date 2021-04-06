
def sum_round(num):
    return " ".join("{}{}".format(c, "0" * i)
                    for i, c in enumerate(str(num)[::-1]) if c != "0")

