# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List=[]

        if not head: #비어있어도 펠린드롬
           return True

        node=head
        #리스트 변환
        while node is not None:
            q.append(node.val)
            node=node.next

        #펠린드롬 판별
        while len(q)>1:
            if q.pop(o)!=q.pop():
                return False
        return True
        # 문자열 슬라이싱 써도 됨 q==q[::-1] 이게 더 빠르다.
# ---------------------------------------------------------------------------------
#2. Deque 이용

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        import collections
        D: Deque = collections.deque()

        if not head: #비어있어도 펠린드롬
           return True

        node=head
        #리스트 변환
        while node is not None:
            D.append(node.val)
            node=node.next

        #펠린드롬 판별
        while len(D)>1:
            if D.popleft()!=D.pop():
                return False
        return True
        # 문자열 슬라이싱 써도 됨 q==q[::-1] 이게 더 빠르다.