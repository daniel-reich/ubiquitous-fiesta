
def lottery(ticket, win):
    wins = 0
    for l in ticket:
        _ = []
        for char in l[0]:
            _.append(ord(char))
        if l[1] in _:
            wins += 1
    return 'Winner!' if wins >= win else 'Loser!'

