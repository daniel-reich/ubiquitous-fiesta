
def error(n):
    error_dict = {1: "Check the fan: e1", 2: "Emergency stop: e2",
                  3: "Pump Error: e3", 4: "c: e4", 5: "Temperature Sensor Error: e5"}
    if n in error_dict.keys():
        return error_dict[n]
    else:
        return 101

