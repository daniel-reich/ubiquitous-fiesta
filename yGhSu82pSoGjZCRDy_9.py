
def seesaw(num):
    if num is None:
        return "balanced"
    num_arr = [int(d) for d in str(num)]
    if len(num_arr) == 1:
        return "balanced"
    final_arr = []
    if len(num_arr) % 2 == 0:
        final_arr = sum(num_arr[int(len(num_arr) / 2):]), sum(num_arr[:int(len(num_arr) / 2)])
    if len(num_arr) % 2 != 0:
        num_arr.pop(num_arr[round(len(num_arr) / 2) - 1])
        final_arr = sum(num_arr[int(len(num_arr) / 2):]), sum(num_arr[:int(len(num_arr) / 2)])
    if final_arr[0] > final_arr[1]:
        return "right"
    elif final_arr[0] < final_arr[1]:
        return "left"
    else:
        return "balanced"

