
def bar_chart(results):
    return_string = ""
    for q, v in sorted(sorted(results.items()), key=lambda tup: tup[1], reverse=True):
        return_string = return_string + q + "|"
        if v > 0:
            return_string = return_string + ("#" * (int(v / 50))) + " {}\n".format(v)
        else:
            return_string = return_string + "0\n"
    return return_string[:-1]

