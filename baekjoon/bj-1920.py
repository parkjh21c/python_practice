# 트리 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

def addNode(self , node):
    while (1):
        if (self.root == None):
            self.root = node
            break
        elif (node.data > self.root.data):
            self.root = self.root.right
        elif (node.data < self.root.data):
            self.root = self.root.left
        else:
            break

def findNode(self, data):
    while (1):
        if (self.root == None):
            print("0")
            break
        elif (data > self.root.data):
            self.root = self.root.right
        elif (data < self.root.data):
            self.root = self.root.left
        else:
            print("1")
            break
        
def postorder(self, n):
    if n != None:
        if n.left:
            self.postorder(n.left)
        if n.right:
            self.postorder(n.right)
        print(n.data, '', end='')

import sys

N = int(sys.stdin.readline())

tree = Tree()

n_list = list(map(int, sys.stdin.readline().split()))

for i in n_list:
    node = Node(i)
    addNode(tree ,node)

postorder(tree)

M = int(sys.stdin.readline())

m_list = list(map(int, sys.stdin.readline().split()))

for j in m_list:
    findNode(tree, j)


