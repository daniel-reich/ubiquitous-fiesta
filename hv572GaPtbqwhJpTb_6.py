
def elasticize(word):
    if len(word) < 3:
        return word
​
    elif len(word) % 2 == 0:
        left = word[:len (word) // 2]
        right = word[len (word) // 2:]
        left_ = ''.join([(left[i] * (i + 1)) for i in range(len(left))])
        right_ = ''.join([(right[i] * (len(right) - i)) for i in range(len(right))])
        return left_ + right_
​
    else:
        left = word[:len (word) // 2]
        right = word[1 + len (word) // 2:]
        center = word[len (word) // 2]
        left_ = ''.join([(left[i] * (i + 1)) for i in range(len(left))])
        center_ = (center *( 1 + len(word) // 2))
        right_ = ''.join([(right[i] * (len(right) - (i))) for i in range(len(right))])
        return left_ + center_ + right_

