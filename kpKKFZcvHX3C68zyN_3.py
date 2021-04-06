
def swap_cards(n1, n2):
    n1ten, n1one = str(n1)[0], str(n1)[1]
    n2ten, n2one = str(n2)[0], str(n2)[1]
    if n1ten <= n1one:
        n1ten, n2ten = n2ten, n1ten
    else:
        n1one, n2ten = n2ten, n1one
    return int(n1ten+n1one) > int(n2ten+n2one)

