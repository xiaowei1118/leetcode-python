# coding: utf-8
class TreeNode(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# 前序遍历
def forwardOrderIterator(node):
    if node:
        print node.value,
        forwardOrderIterator(node.left)
        forwardOrderIterator(node.right)

#后序遍历
def backwardOrderIterator(node):
    if node:
        backwardOrderIterator(node.left)
        backwardOrderIterator(node.right)
        print node.value,

#中序遍历
def middleOrderIterator(node):
    if node:
        middleOrderIterator(node.left)
        print node.value,
        middleOrderIterator(node.right)


def initBuildTree():
    a = TreeNode("a")
    b = TreeNode("b")
    c = TreeNode("c")
    a.left = b
    a.right = c
    d = TreeNode("d")
    e = TreeNode("e")
    f = TreeNode("f")
    g = TreeNode("g")
    h = TreeNode("h")
    i = TreeNode("i")
    j = TreeNode("j")
    b.left = d
    b.right = e
    d.left = h
    e.left = i
    c.left = f
    c.right = g
    g.right = j
    return a

forwardOrderIterator(initBuildTree())
print ""
middleOrderIterator(initBuildTree())
print ""
backwardOrderIterator(initBuildTree())
print ""

