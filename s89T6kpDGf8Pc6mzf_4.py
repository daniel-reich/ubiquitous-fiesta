
ref={"0":"abcdef", "1":"bc", "2":"abdeg", "3":"abcdg", "4":"bcfg",
 "5":"acdfg", "6":"acdefg", "7":"abc", "8":"abcdefg", "9":"abcfg"}
def order(i):
    return ord(i.lower())
def seven_segment(nums):
    res=[]
    for i in range(len(nums)-1):
        temp1=[j for j in ref[nums[i]] if j not in ref[nums[i+1]]]
        temp2=[j.upper() for j in ref[nums[i+1]] if j not in ref[nums[i]]]
        res.append(sorted((temp1 + temp2),key=order))
    return res

