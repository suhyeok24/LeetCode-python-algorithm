#1. 내 풀이 - time limit exceeded

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        from functools import reduce
        def multiplier(arr: [int]):
            return reduce(lambda x, y: x * y, arr)
        #reduce(이전 값 누적 반환)을 활용해 리스트내 원소 곱을 구하는 multiplier 함수 작성

        op = []
        for i in range(len(nums)):
            p=nums.pop(0)
            op.append(multiplier(nums))
            nums.append(p)
        return op
# ---------------------------------------------------------------------------------
#2. 자신을 제외한 왼쪽 곱셉 결과와 오른쪽 곱셈 결과 곱하기;- 내풀이 time error.
# multiplier 함수 쓰면 안되나봄

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:

        from functools import reduce

        def multiplier(arr: [int]) -> int:
            return reduce(lambda x, y: x * y, arr)

        op=[]
        for i in range(len(nums)):
            if i==0:
                op.append(multiplier(nums[i+1:]))
            elif i==len(nums)-1:
                op.append(multiplier(nums[:i]))
            else:
                op.append((multiplier(nums[:i]))*(multiplier(nums[i+1:])))
        return op

# --------------------------------------------------------------------------------------------------------
#3.책 풀이

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        op=[]

        #왼쪽 곱셈.(0번째항보다 전에 default값으로 1이 존재. )>>중요하다 모든 곱셈 초기화는 1로 시작!
        p=1
        for i in range(len(nums)):
            op.append(p*p)
            p=p*nums[i]