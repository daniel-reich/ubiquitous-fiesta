
def translate(ran, num):
    if num > ran ** 2:
        return "{} is not in the range [0:{}]".format(num, ran ** 2)
    secrete_num = ran ** 2 - num
    if secrete_num == num:
        return "+0 ---> {}".format(secrete_num)
    elif secrete_num < num:
        move_forward = secrete_num + 1 + ran ** 2 - num
        move_backward = num - secrete_num
        if move_forward == move_backward:
            return "+{} or -{} ---> {}".format(move_forward, move_backward, secrete_num)
        elif move_forward > move_backward:
            return "-{} ---> {}".format(move_backward, secrete_num)
        elif move_forward < move_backward:
            return "+{} ---> {}".format(move_forward, secrete_num)
    elif secrete_num > num:
        move_forward = secrete_num - num
        move_backward = num + 1 + ran** 2 - secrete_num
        if move_forward == move_backward:
            return "+{} or -{} ---> {}".format(move_forward, move_backward, secrete_num)
        elif move_forward > move_backward:
            return "-{} ---> {}".format(move_backward, secrete_num)
        elif move_forward < move_backward:
            return "+{} ---> {}".format(move_forward, secrete_num)

