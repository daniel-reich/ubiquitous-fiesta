
def currently_winning(scores):
​
    currently_winner = []
    my_score, opponent_score = 0, 0
​
    for i in range(0, len(scores), 2):
​
        my_score += scores[i]
        opponent_score += scores[i+1]
​
        if my_score > opponent_score:
            winner = 'Y'
        elif my_score < opponent_score:
            winner = 'O'
        else:
            winner = 'T'
​
        currently_winner.append(winner)
​
    return currently_winner

