
import math
def tower_of_hanoi(disks, move):
    assert move <= 2**disks-1
    disk_locs = [0 for i in range(disks)]
    for i in range(move):
        x = int(math.log2((i^(i+1))+1))-1
        disk_locs[x] = (disk_locs[x] + 1 - 2*(x%2!=disks%2))%3
    return (
        [i+1 for i in range(disks-1,-1,-1) if disk_locs[i]==0],
        [i+1 for i in range(disks-1,-1,-1) if disk_locs[i]==1],
        [i+1 for i in range(disks-1,-1,-1) if disk_locs[i]==2]
        )

