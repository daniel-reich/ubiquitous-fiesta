
def best_start(lst, word):
    
    points = {'A': 1, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5,
              'J': 8,'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1,
              'T': 1, 'W': 4,'V': 4, 'Y': 4, 'X': 8, 'Z': 10}
    
    word = word.upper()
    scores = []
    
    for i in range (len(lst) - len(word)) : # i is the start for the word to be entered
        score = sum([points[a] for a in word])
        for j in range (len(word)) :
            if lst[i+j] == 'DL' :
                score += points[word[j]]
            if lst[i+j] == 'TL' :
                score += 2*points[word[j]]
        if 'DW' in lst[i:i+len(word)] :
            score *= 2
        scores.append (score)
        
    return scores.index(max(scores))

