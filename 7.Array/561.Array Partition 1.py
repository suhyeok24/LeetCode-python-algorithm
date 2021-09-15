# 1. 내 풀이(오름차순 정렬)
class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        sum=0
        for i in range(0,len(nums),2):
            sum+=min(nums[i],nums[i+1])
        return sum
# -----------------------------------------------------------------------------------
#2. 1번과 유사(책풀이) 내께 더 나음 ㅋㅋ
class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        sum=0
        pair=[]
        for n in nums:
            pair.append(n)
            if len(pair)==2:
                sum+=min(pair) #min(리스트):int
                pair=[]
        return sum
# ------------------------------------------------------------------------------------
#3. 짝수 번째 값 계산 (1번에서 발전)- 내 풀이

class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        sum=0
        for i in range(0,len(nums),2): # n개 전부 loop 돌려서 if문 거는 것보단 step=2주는게 남
            sum+=nums[i]
        return sum
# ------------------------------------------------------------------------------------
#4. 짝수 번째 값 계산 - 책 풀이
class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        sum=0

        for i,n in enumerate(nums):
            if i%2==0:
                sum+=n
        return sum
# ------------------------------------------------------------------------------------
#5. Real Phythonic Way :파이썬을 공부하는 이유
class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        return sum(sorted(nums)[::2])