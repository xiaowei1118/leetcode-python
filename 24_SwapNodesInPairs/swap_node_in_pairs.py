# coding=utf-8
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        pre_node = head
        next_node = head.next

        new_head = ListNode(None)
        last_next = new_head

        while pre_node:
            if not next_node:
                last_next.next = pre_node
                break

            temp = next_node.next
            last_next.next = next_node
            next_node.next = pre_node
            last_next = pre_node

            if not temp:
                last_next.next = None
                break

            pre_node = temp
            next_node = temp.next

        return new_head.next


a = None
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

# a.next = b
# b.next = c
# c.next = d
# d.next = e

def printList(node):
    while node:
        print node.val
        node = node.next

printList(Solution().swapPairs(a))


