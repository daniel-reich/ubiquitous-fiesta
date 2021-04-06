
def face_interval(nums):
    return (":/" if type(nums) != list else
            ":)" if nums[-1] - nums[0] in nums else ":(")

