
def get_total_price(lst):
    import numpy as np
    return np.around(sum(map(lambda x:x['quantity']*x['price'],lst)),decimals=2)

