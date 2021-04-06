
def get_items_at(arr, par):
    if arr == []:
        return []
    elif len(arr) == 1 and par == "odd":
            return [arr[0]]
    elif len(arr) == 1 and par == "even":
           return []
    elif len(arr) >= 2:
        if len(arr) % 2 != 0 and par == "odd":
           return [arr[0]] + get_items_at(arr[1:], "odd")
        elif len(arr) % 2 != 0 and par == "even":
           return [arr[1]] + get_items_at(arr[2:], "even")
        elif len(arr) % 2 == 0 and par == "even":
           return [arr[0]] + get_items_at(arr[1:], "even")
        elif len(arr) % 2 == 0 and par == "odd":
           return [arr[1]] + get_items_at(arr[2:], "odd")

