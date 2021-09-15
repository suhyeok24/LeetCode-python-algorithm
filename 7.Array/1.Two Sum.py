# 1. 브루트 포스(무지성 더하기) ㅋㅋ > ㅈ밥용
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):  # 연산줄이기: i+1번부터 돌리기
                if nums[i] + nums[j] == target:
                    return [i, j]


# 시간복잡도 O(n^2): 개쓰레기

# 2. in을 이용한 탐색
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i, num in enumerate(nums):
            diff = target - num

            if diff in nums[i + 1:]:
                return [i, nums[i + 1].index(diff) + (i + 1)]


# 시간복잡도는 O(n^2)로 마찬가지지만 in을 쓰는게 두값비교(==)보다 훨씬 효율적이다.

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

# 3번에서 for문 합치기
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [i, nums_dict[complement]]
            nums_dict[num] = i
#투 포인터 이용
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        left, right= 0, len(nums)-1
        nums = sorted(nums)
        while left!=right : #loop돌리기(left right 같지 않을때)
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return [left,right]

# 정렬이 안된 배열(리스트)이기 때문에 값을 구할수는 있지만 인덱스가 뒤섞여 풀이 불가능
