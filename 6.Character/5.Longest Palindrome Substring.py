class Solution:
    def longestPalindrome(self, s: str) -> str:

        # 예외처리(값 바로 나와서 투 포인터 쓸 필요 없음)
        if len(s) < 2 or s == s[::-1]:
            return s

        # 펠린드롬 판별 및 포인터 확장
        def extend(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # while을 벗어난건 펠린드롬이 아닌거니까 이전의 껄로 return

        # 포인터 위치 이동(슬라이딩 윈도우)
        result = ''
        for i in range(len(s) - 1):
            result = max(result,  # 이전 result와 비교
                         extend(i, i + 1),
                         extend(i, i + 2),
                         key=len)
        return result
