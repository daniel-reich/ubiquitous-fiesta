
def error(n):
    errs = {
        1: "Check the fan",
        2: "Emergency stop",
        3: "Pump Error",
        4: "c",
        5: "Temperature Sensor Error",
    }
    if n not in errs:
        return 101
    return errs[n]+': e'+str(n)

