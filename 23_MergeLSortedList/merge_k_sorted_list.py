# coding=utf-8
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        head = ListNode(None)
        p = head
        current = 0

        while(n > 0):
            for i in range(0, len(lists)):
                if not lists[i]:
                    continue

                if not lists[current]:
                    current = i

                if lists[i] and lists[i].val < lists[current].val:
                    current = i

            if p:
                p.next = lists[current]
                p = p.next


            if lists[current]:
                lists[current] = lists[current].next

            if not lists[current]:
                n = n - 1
                lists.pop(current)

            current = 0

        return head.next

def printList(node):
    while node:
        print node.val
        node = node.next

# item1 = ListNode(1)
# item1.next = ListNode(4)
# item1.next.next = ListNode(5)
#
# item2 = ListNode(1)
# item2.next = ListNode(3)
# item2.next.next = ListNode(4)
#
# item3 = ListNode(2)
# item3.next = ListNode(6)

item1 = None

# item2 = ListNode(-1)
# item2.next = ListNode(5)
# item2.next.next = ListNode(11)

item3 = ListNode(1)

# item4 = ListNode(6)
# item4.next = ListNode(10)

# item3 = ListNode(1)

printList(Solution().mergeKLists([item1, item3]))
