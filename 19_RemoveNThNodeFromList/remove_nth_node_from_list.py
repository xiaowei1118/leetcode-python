# coding=utf-8
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = head

        for i in range(0, n+1):
            if p:
                p = p.next
            else:
                if i == n:  # 刚好要删的是头节点
                    head = head.next

                # 倒数超出链表节点数
                return head

        q = head
        while p:
            p = p.next
            q = q.next

        q.next = q.next.next

        return head

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

def printList(head):
    while head:
        print head.val
        head = head.next

#printList(head)

p = Solution().removeNthFromEnd(head, 3)
printList(p)