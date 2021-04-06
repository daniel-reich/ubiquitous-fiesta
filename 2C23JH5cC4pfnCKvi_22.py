
def check_flush(table, hand):
    abbrevative = ['S','H','D','C']
    table_lst = []
    for s in table:
        s_split = s.split('_')
        table_lst.append(s_split)
        
    table_lst = [item for sublist in table_lst for item in sublist]
    
    hand_lst = []
    for s in hand:
        s_split = s.split('_')
        hand_lst.append(s_split)
        
    hand_lst = [item for sublist in hand_lst for item in sublist]
    
    for letter in hand_lst:
        if letter in abbrevative:
            if table_lst.count(letter) >= 3:
                return True
            else:
                return False

