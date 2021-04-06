
def get_primiera_score(deck):
    colors = {'d':[], 'h':[], 'c':[], 's':[]}
    for card in deck:
        card = Card(card)
        colors[card.color].append(card.score)
    if all(colors.values()):
        return sum(max(score) for score in colors.values())
    return 0
​
class Card:
    def __init__(self,card):
        self.value, self.color = list(card)
        self.score = self._score()
​
    def _score(self):
        if self.value == '7': return 21
        if self.value == '6': return 18
        if self.value == 'A': return 16 
        if '2' <= self.value <= '5': return 10 + int(self.value)
        return 10

