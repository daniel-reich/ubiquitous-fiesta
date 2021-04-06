
def lets_meet(distance, va, vb):
    x = distance/(va+vb)
    hours, minutes = divmod(x*60, 60)
    seconds = divmod(x*3600,60)
    return "{}h {}min {}s".format(int(hours), int(minutes), int(seconds[1]))

