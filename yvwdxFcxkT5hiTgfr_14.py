
def get_xp(d):
​
    scores = []
    for k, v in d.items():
        if k == "Very Easy":
            newscore = 5*v
            scores.append(newscore)
        if k == "Easy":
            newscore = 10*v
            scores.append(newscore)
        if k == "Medium":
            newscore = 20*v
            scores.append(newscore)
        if k == "Hard":
            newscore = 40*v
            scores.append(newscore)
        if k == "Very Hard":
            newscore = 80*v
            scores.append(newscore)
            
    
    total = sum(scores)
        
    return str(total) + 'XP'

