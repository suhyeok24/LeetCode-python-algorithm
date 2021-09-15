class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] == nums[i - 1] and i >= 1:
                continue
            # 6~7 번째 라인도 중요 
            left, right = i + 1, len(nums) - 1

            while left < right:
                target = 0 - nums[i]
                if nums[left] + nums[right] > target:
                    right -= 1

                elif nums[left] + nums[right] < target:
                    left += 1

                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        #21~26번쨰 라인이 중요

        return answer
