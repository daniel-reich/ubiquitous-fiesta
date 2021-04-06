
def tower_of_hanoi(disks, move):
    arr = [list(range(disks, 0, -1)), [], []]
    direction = -1 if disks%2 else 1
    a, i = 0, 0
​
    while True:
        new_pos = (a + direction)%3
        arr[new_pos].append(arr[a].pop())
        a = new_pos
        i += 1
        if i == move:
            return tuple(arr)
        b, c = (a + direction)%3, (a + (direction*2))%3
        if not arr[b] and not arr[c]:
            return tuple(arr)
        if not arr[b]:
            arr[b].append(arr[c].pop())
        elif not arr[c]:
            arr[c].append(arr[b].pop())
        elif arr[b][-1] < arr[c][-1]:
            arr[c].append(arr[b].pop())
        else:
            arr[b].append(arr[c].pop())
        i += 1
        if i == move:
            return tuple(arr)

