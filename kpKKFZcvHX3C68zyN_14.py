
def swap_cards(n1, n2):
    ot = n2 // 10
    if n1 // 10 <= n1 % 10:
        # Paul's lowest digit is the ten's digit:
        paul = 10 * ot + n1 % 10
        opp = 10 * (n1 // 10) + n2 % 10
    else:
        # Paul's lowest digit is the one's digit:
        paul = 10 * (n1 // 10) + ot
        opp = 10 * (n1 % 10) + n2 % 10        
    return paul > opp

