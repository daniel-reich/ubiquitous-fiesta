
def return_end_of_number(num):
    ky = {"1": "ST", "2": "ND", "3": "RD"}
    if str(num)[-2:] in ["11", "12", "13"]:
        return "{}-{}".format(str(num), "TH")
    else:
        return "{}-{}".format(str(num), ky.get(str(num)[-1], "TH"))

