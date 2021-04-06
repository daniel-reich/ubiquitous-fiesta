
def can_play(hand, face):    
    hand = [i.split(' ') for i in hand]
    face = [face.split(' ') for f in range(1)]
    new_list = []
    same = 0
    for i in hand:
        for j in i:
            if j not in new_list:
                new_list.append(j)
          
      
    for f in face:
        for g in f:
            if g in new_list:
                same +=1
            else:
                same += 0
    
    if same >= 1:
        return True
    else :
        return False

