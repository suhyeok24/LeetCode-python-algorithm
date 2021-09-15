

class Solution:
    def reverseString(self, s) -> None:
        s.reverse()
# s[::-1]은 내부 직접 조작은 맞지만 공간복잡도 O(1)에 맞지않음(Only in leetcode)
# trick인 s[:] = s[::-1]을 쓰면 ㄱㄴ

#추가 투포인터를 이용한 스왑

class Solution:
    def reverseString(self, s:[str]) -> None:  #리턴이 없어 None
        left, right = 0, len(s)-1  #다중 할당을 생활화하자.
        while right > left:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
