# 3.첫번쨰 수를 뺸 결과 키 조회(딕셔너리만들기)
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            nums_dict[num] = i  # num을 key로 해야 첫번째 수를 뺀 값을 in을 활용해 조회가능
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums_dict and i != nums_dict[complement]:  # error가 발생하면 안됨
                return [i, nums_dict[complement]]  # key값이 조회가 되는 것만 return