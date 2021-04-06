
def currently_winning(scores):
  you = [scores[i] for i in range(len(scores)) if i%2==0]
  opp = [scores[i] for i in range(len(scores)) if i%2==1]
  return ["Y" if sum(you[:i+1]) > sum(opp[:i+1]) else "O" if sum(you[:i+1]) < sum(opp[:i+1]) else "T" for i in range(len(you))]

