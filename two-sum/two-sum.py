class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [i, nums_dict[complement]]
            nums_dict[num] = i