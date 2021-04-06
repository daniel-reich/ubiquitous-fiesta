
def rps(p1, p2):
        d = ["PaperRock","RockScissors","ScissorsPaper"]
        if p1+p2 in d:
            return "The winner is p1"
        elif p1==p2:
            return "It's a draw"
        else:
            return "The winner is p2"

