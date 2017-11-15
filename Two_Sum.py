class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        while i < len(nums):
            nums2 = nums[i+1:]
            num = target - nums[i]
            if num in nums2:
                return [i,nums.index(num,i+1)]
            i = i + 1
