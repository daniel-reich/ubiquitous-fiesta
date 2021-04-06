
def game_of_life(board):
    ans=''
    v=len(board)
    h=len(board[0])
    d=((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1))
    for y in range(v):
        for x in range(h):
            k=0
            for p in range(8):
                xn=x+d[p][0];yn=y+d[p][1]
                if h>xn>-1 and v>yn>-1:
                    if board[yn][xn]==1:
                        k+=1
            if board[y][x]==1:
                if k<2 or k>3:
                    ans+='_'
                else:
                    ans+='I'
            else:
                if k==3:
                    ans+='I'
                else:
                    ans+='_'
        if y<v-1:
            ans+='\n'
    return ans

