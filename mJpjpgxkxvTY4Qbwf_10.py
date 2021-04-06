
def bingo_check(board):
​
    vert_scores=[0]*5
    diag_score1=0
    diag_score2=0
    diag_index1 = -1
    diag_index2 = 5
    for row in board:
        horiz_score=0
        diag_index1+=1
        diag_index2-= 1
​
        for index,item in enumerate(row):
            horiz_score+=((item=="x"))
​
            diag_score1 += (index == diag_index1)*((item=="x"))
            diag_score2 += (index == diag_index2)*((item == "x"))
​
            vert_scores[index]+=(item=="x")
​
            if vert_scores[index]==5 or horiz_score==5 or  diag_score1==5 or  diag_score2==5 :
                return True
​
    return False

