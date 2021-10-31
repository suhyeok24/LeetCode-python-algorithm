# 1차시도 실패 - time limit
class Solution:
    def maxProfit(self, prices: [int]) -> int:

        # 예외상황(내림차순정렬)
        if prices == sorted(prices)[::-1]:
            return 0

        # 일반적 상황(max(profit)산출 ㄱㄴ)
        answer = 0
        for i in range(0, len(prices) - 1):
            m = max(prices[i + 1:]) - prices[i]
            if m > answer:
                answer = m
        return answer

#2. 책 풀이 - 카데인 알고리즘 이용 O(n)
class Solution:
    def maxProfit(self, prices: [int]) -> int:

     #최대, 최소 설정(시스템의 최댓값, 최솟값으로 설정)
    profit = 0 #이론상 -sys.maxsize(시스템의 최솟값)이 맞지만 [](빈 리스트가 들어올 걸 가정해) 0으로 설정
    min_price = sys.maxsize  #입력값이 어떤 값이 들어올지 모르므로 시스템의 최댓값으로 설정
                             # 이후 점점 바꿔나가면 됨(어떤 값이든 교체될 수 있음)

    #최솟값과 최댓값을 계속 갱신
    for price in prices:                 # 단, 현재상태까지의 고점을 갱신하지는 않음. 그냥 현재값에서 빼는것.
                                         # 사실상 판매하는 모든 경우를 고려한것.(모든시점에서 판매이므로)
        min_price = min(min_price,price) # 현재 상태까지의 저점을 계속 갱신
        profit = max(profit,price-min_price) # 현시점의 가격 price에서 현재까지의 저점을 뺌 = profit
                                             # 그 profit의 최댓값을 갱신.


    return profit

    #시계열 문제 느낌, 매 시점마다 판매를 계속하여 profit의 최댓값을 갱신.(그 판매는 저점 가격과 이루어짐)



