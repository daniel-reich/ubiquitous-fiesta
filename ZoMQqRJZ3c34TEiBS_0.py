
import numpy as np
​
def playfair(txt, keyword):
    val = 1 if txt[-1] == '.' else -1 # cypher or decypher mode set
    
    board = {chr(val) for val in range(65,91)} # A to Z
    txt = [char for char in txt.upper() if char in board] # Remove space and punctuation
    keyword_f = set(keyword.upper())
    board = np.array(sorted(board - keyword_f)) # (A to Z) - (chars in keyword_f)
    keyword_f = sorted(keyword_f, key = lambda elm: keyword.upper().index(elm)) # sort chars in txt_f in order of their apparition in txt
    board = np.reshape(np.concatenate((keyword_f, np.delete(board, np.where(board == 'J')))), (5,5)) # concatenate txt to board and reshape to a (5*5) array
    
    # insert x between every double letter
    for idx in range(0,len(txt),2):
        try:
            if txt[idx] == txt[idx+1]: txt.insert(idx+1, 'X')
        except: pass
    
    if len(txt)%2 != 0: txt.append('X') # insert x at the end of the message if it the number of chars is odd
    message = np.reshape(txt, (len(txt)//2, 2)) # reshape the message into arrays of 2 chars each
    
    # encrypting the message
    encrypted = ""
    for row in message:
        # get the row and cold of each char in the message
        letter_pos = np.array(list(map(np.concatenate, [np.where(board == row[val]) for val in range(2)])))
        
        # playfair encryption rules
        if letter_pos[0,0] - letter_pos[1,0] == 0: 
            letter_row = letter_pos[0,0]
            encrypted += board[letter_row, (letter_pos[0, 1] + val) % 5] + board[letter_row, (letter_pos[1, 1] + val) % 5]
        elif letter_pos[0,1] - letter_pos[1,1] == 0:
            letter_col = letter_pos[0,1]
            encrypted += board[(letter_pos[0, 0] + val) % 5, letter_col] + board[(letter_pos[1, 0] + val) % 5, letter_col]
        else:
            encrypted += board[letter_pos[0, 0], letter_pos[1,1]] + board[letter_pos[1,0], letter_pos[0,1]]
    
    return encrypted

