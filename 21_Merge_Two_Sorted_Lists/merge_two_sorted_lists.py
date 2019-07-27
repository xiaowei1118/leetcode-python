# coding=utf-8

# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = None

        if not l1:
            head = l2
            return head

        if not l2:
            head = l1
            return head

        p = head
        while l1 and l2:
            if l1.val > l2.val:
                if not head:
                    head = l2
                    p = head
                else:
                    p.next = l2
                    p = p.next
                l2 = l2.next
            else:
                if not head:
                    head = l1
                    p = head
                else:
                    p.next = l1
                    p = p.next

                l1 = l1.next

        if l1:
            p.next = l1

        if l2:
            p.next = l2

        return head

# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

l1 = None
# l1.next = ListNode(2)
# l1.next.next = ListNode(4)

l2 = ListNode(1)
# l2.next = ListNode(3)
# l2.next.next = ListNode(4)

def printList(head):
    while head:
        print head.val
        head = head.next

printList(Solution().mergeTwoLists(l1,l2))