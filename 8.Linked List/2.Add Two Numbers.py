# 내 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        q1 = []
        q2 = []

        node1 = l1
        node2 = l2

        while node1 is not None:
            q1.append(node1.val)
            node1 = node1.next

        while node2 is not None:
            q2.append(node2.val)
            node2 = node2.next

        n1, n2 = 0, 0
        for i, num1 in enumerate(q1):
            n1 += num1 * (10 ** i)

        for j, num2 in enumerate(q2):
            n2 += num2 * (10 ** j)

        n = n1 + n2
        n = list(str(n))[::-1]

        #숫자형 리스트를 만들고, 그 안의 숫자들을 더하고싶다.(342 + 465) 이런식
        #나는 for문을 이용해 리스트 요소를 꺼낸다음 10의 거듭제곱을 하였다.

        #but 책에서는 join을 활용한다(먼저 문자형 리스트여야함)그런데 숫자형 리스트라
        #걍 숫자를 for문으로 추출하고 그것에 str을 씌운다.(List comprehension)
        #like str(e) for e in a
        #그것을 다시 int를 씌워 숫자로 바꿈.솔직히 내께 더 나은듯 ㅋㅋ

# 책 풀이

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:












        resultStr= int("".join(str(e) for e in a))+
                   int("".join(str(e) for e in b))