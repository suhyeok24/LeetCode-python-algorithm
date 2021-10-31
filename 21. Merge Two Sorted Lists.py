class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 재귀구조를 이용
        #기본적으로 l1과 l2의 초기값은 연결리스트의 맨 처음 값
        if (not l1) or (l2 and l1.val > l2.val):   #작은 값이 왼쪽으로 오도록 함.(정렬된 연결리스트를 만들어야하니까)
            l1, l2 = l2, l1
        if l1:   # l1의 다음노드와 l2를 다시 함수에(재귀)
            l1.next = self.mergeTwoLists(l1.next, l2)
            #li.next가 null이되면(li의 마지막 노드) 재귀함수에서 l1.nnnnnn~,l2 = l2,null이 되고
            #두번째 if 문은 if null이 되어 자동 false, l1.nnnnn~이 드디어 재귀탈출, 리턴시작
            #리턴값들이 백트래킹하면서 올라감.
            #최종적으로 l1이 리턴.
        return l1
