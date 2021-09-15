#연결 리스트. 그림을 이용해서 풀것. 처음에 이해 어려움

#1. 반복 풀이(책)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #ListNode는 포인터로 연결된 리스트 자체를 지칭

        node, prev = head, None #초기값 설정(head는 가장 첫 노드가 됨)

        while node:
            next, node.next = node.next, prev
            # next는 head의 원 방향대로 가는 다음 노드
            # node.next = prev는 포인터를 역방향으로 연결(노드하나씩,head부터)

            prev, node = node, next
            # prev와 node를 한칸씩 점프(head 정방향)

        #즉 이 while문의 의미는 node와 prev를 정방향으로 한칸씩 이동시키면서
        #    해당 노드의 포인터를 역방향으로 연결
        # node가 null이 됐을때 prev는 마지막 노드에 종착, 모든 노드가 역뱡항으로 연결됨
        # prev를 리턴하면 역방향 linked d리스트가 리턴됨


node, prev = head, None

node.next, next = prev, node.next
#이걸 한줄에 swap하는 이유, 뒤의 node.next는 정방향이므로 역뱡향 prev에 영향받으면 안됨

node, prev = next, node

