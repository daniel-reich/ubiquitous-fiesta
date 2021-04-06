
def bishop(start, end, n):
    field_ids = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ], [1, 2, 3, 4, 5, 6, 7, 8]))
​
    # case 1 - zero ruchow
    if n == 0:
        if start == end:
            return True
        return False
​
    start_id_add = field_ids[list(start)[0]] + int(list(start)[1])
    end_id_add = field_ids[list(end)[0]] + int(list(end)[1])
    start_id_sub = field_ids[list(start)[0]] - int(list(start)[1])
    end_id_sub = field_ids[list(end)[0]] - int(list(end)[1])
​
    # case 2 - inny kolor pol start i end
    if start_id_add % 2 != end_id_add % 2:
        return False
​
    # case 3 - 1 ruch, ten sam kolor, przekatna \
    if n == 1 and start_id_add == end_id_add:
        return True
​
    # case 4 - 1 ruch, ten sam kolor, przekatna /
    if n == 1 and start_id_sub == end_id_sub:
        return True
    
    if n == 1:
        return False
    
    # case 5 - wicej niz 1 ruch i ten sam kolor
    return True

