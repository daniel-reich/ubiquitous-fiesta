
def get_primiera_score(l):
    if set([l[i][1] for i in range(len(l))]) != {'d','h','s','c'}:
        return False
    else:
        count = 0
        selected_suits = []
        while len(selected_suits) != 4:
            for card in l:
                if card[0] == '7' and card[1] not in selected_suits:
                    selected_suits.append(card[1])
                    count += 21
            for card in l:
                if card[0] == '6' and card[1] not in selected_suits:
                    selected_suits.append(card[1])
                    count += 18
            for card in l:
                if card[0] == 'A' and card[1] not in selected_suits:
                    selected_suits.append(card[1])
                    count += 16
            for card in l:
                if card[0] in '5432' and card[1] not in selected_suits:
                    selected_suits.append(card[1])
                    count += 10 + int(card[0])
            for card in l:
                if card[0] in 'JQK' and card[1] not in selected_suits:
                    selected_suits.append(card[1])
                    count += 10
        return count

