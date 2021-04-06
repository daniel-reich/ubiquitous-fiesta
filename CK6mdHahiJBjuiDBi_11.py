
def can_fit(weights, bags):
    weights.sort(reverse=True)
    cart = []
    
    while weights:
        bag = [weights.pop(0)]
        items = []
        for w in weights:
            if sum(bag) + w <= 10:
                bag.append(w)
                items.append(w)
        for i in items:
            weights.remove(i)
        cart += [bag]
        
    return len(cart) <= bags

