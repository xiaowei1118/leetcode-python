# -*- coding: utf-8 -*-
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = None
    link = None
    carry = 0  #carry 表示进位
    while not l1 is None or not l2 is None:
        total = (l1.val if not l1 is None else 0) + (l2.val if not l2 is None else 0)+carry
        val = total % 10
        if link is None:
            link = ListNode(val)
            head = link
        else:
            link.next =ListNode(val)
            link = link.next
        carry = total / 10

        if not l1 is None:
            l1 = l1.next

        if not l2 is None:
            l2 = l2.next

    if carry > 0:
        link.next = ListNode(carry)

    return head

def buildList(list):
    current = None
    head = None
    for item in list:
        if current is None:
            current = ListNode(item)
            head = current
        else:
            current.next = ListNode(item)
            current = current.next

    return head

def printListNodes(node):
    '''
    :param node: ListNode
    :return:
    '''
    while not node is None:
        print node.val
        node = node.next

list1 = buildList([9,8])
list2 = buildList([1])
list = addTwoNumbers(list1,list2)
printListNodes(list)


