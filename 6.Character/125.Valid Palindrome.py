class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        answer = 0
        count = 0
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        for i in range(len(strs)):
            if strs[i] != strs[len(strs) - (1 + i)]:
                answer = False
            else:
                count += 1
        if count == len(strs):
            answer = True
        return answer
# -----------------------------------------------------------------------------------------------------------------

# 제대로된 나의 첫 리트코드 풀이이다
 # 변수명.isalnum()은 영문자,숫자여부를 판별하는 함수이다.
 # 변수명.lower()을 쓰면 변수를 소문자로 바꿔준다.

# 파이썬알고리즘 1번풀이

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs)>1:        1개일때는 비교 필요 x
            if strs.pop(0)!=strs.pop():
                return False      값을 리턴하고 모든 함수의 동작 자동종료, 즉 while문 자동종료
        return True               while문을 다 돌렸을때만 true가 나오게
# ------------------------------------------------------------------------------
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            #import re
            s = s.lower()
            s = re.sub('[^a-z0-9]', '', s)  # 대문자가 들어가지 않으면 w로 표기하면 안됨.

            return s == s[::-1]  # s[::-1]은 s의 reverse다.
# 가장 깔끔한 풀이

# -------------------------------------------------------------------------------------------------------
# Deque를 이용한 풀이

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import collections

        D: Deque = collections.deque()

        s=s.lower()

        for chr in s:
            if chr is alnum:
                D.append(chr)

        while len(D)>1:
            if D.popleft()!=D.pop():
                return False

        return True



