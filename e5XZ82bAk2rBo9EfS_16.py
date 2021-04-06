
def bed_time(*times):
    result = []
    for item in times:
        time_of_alarm = int(item[0][:2]) * 60 + int(item[0][3:])
        sleep_duration = int(item[1][:2]) * 60 + int(item[1][3:])
        dif = time_of_alarm - sleep_duration
        mod = dif % 60
        div = dif // 60
        result.append(str("{:02d}".format(24 + div if div < 0 else div)) + ":" + str("{:02d}".format((mod) % 60)))
    return result

