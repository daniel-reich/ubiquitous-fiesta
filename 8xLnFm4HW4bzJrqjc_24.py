
def digit_distance(num1, num2):
    nums1 = [i for i in str(num1)]
    nums2 = [i for i in str(num2)]
    return sum([abs(eval(i+"-"+j)) for i,j in zip(nums1,nums2)])

