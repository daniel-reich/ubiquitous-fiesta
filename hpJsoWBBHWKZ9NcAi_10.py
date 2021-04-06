
def bird_code(lst):
​
    def code(lst):
        bird = lst.replace('-', ' ').upper().split()
        if len(bird) == 4:
            return ''.join(i[0] for i in bird)
        elif len(bird) == 3:
            return bird[0][0] + bird[1][0] + bird[2][:2]
        elif len(bird) == 2:
            return bird[0][:2] + bird[1][:2]
        else:
            return bird[0][:4]
​
    return [code(i) for i in lst]

