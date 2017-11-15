class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        while i < len(nums):
            nums2 = nums[i+1:]
            sec_num = target - nums[i]
            if sec_num in nums2:
                return [i,nums.index(sec_num,i+1)]
            i = i + 1
