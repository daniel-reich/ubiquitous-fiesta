
def sexagenary(year):
​
    ELEMENTS = ['wood', 'fire', 'earth', 'metal', 'water'] #change every second year
    ANIMALS = ['rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep', 'monkey', 'rooster', 'dog', 'pig'] #change yearly
​
    def _create_elements_order(elements):
        elements_order = []
        for el in elements:
            elements_order.extend([el, el])
​
        return elements_order
​
    def _find_items():
        items = []
        
        calc_index = lambda type_: abs(difference) % len(type_) 
        
        for type_ in [elements, ANIMALS]:
            index = calc_index(type_)
            index = index * -1 if difference < 0 else index
​
            items.append(type_[index])
        return items
    
    YEAR_0 = 1984
​
    
    elements = _create_elements_order(ELEMENTS) #DUPLICATE EACH VALUE
    difference = year - YEAR_0
    items = _find_items()
    
    return ' '.join(items).title()

