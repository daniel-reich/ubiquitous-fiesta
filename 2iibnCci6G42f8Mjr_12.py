
def guess_score(code, guess):
        ans = {}
        guessLst = [x for x in guess]
        black = 0
        white = 0
        for i in range(len(code)):
                if code[i] == guess[i]:
                        black += 1
                elif code[i] in guessLst:
                        white += 1
                        guessLst.remove(code[i])
        ans['black'] = black
        ans['white'] = white
        return ans

