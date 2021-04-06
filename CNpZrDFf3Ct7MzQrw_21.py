
def trouble(num1, num2):
  nums1 = list(str(num1))
  nums2 = list(str(num2))
  for i in range(len(nums1)-2):
    if nums1[i] == nums1[i+1] and nums1[i] == nums1[i+2]:
      for j in range(len(nums2)-1):
        if nums2[j] == nums2[j+1] and nums2[j] == nums1[i]:
          return True   
  return False

