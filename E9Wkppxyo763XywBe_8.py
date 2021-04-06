
def binary_clock(time):
    template = [
        "  00",
        "0000",
        " 000",
        "0000",
        " 000",
        "0000"]
    time = time.replace(":", "")
    for i in range(6):
        str_bin = str(bin(int(time[i])))[2:]
        template[i] = template[i][: -len(str_bin)] + str_bin
    result = []
    for col in range(4):
      result.append(''.join(e[col] for e in template))
    return result

