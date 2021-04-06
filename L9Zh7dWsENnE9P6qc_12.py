
def josephus(people):
 binary=bin(people)
 winner=binary[3:]+binary[2]
 return (int(winner,2))

