# 트리 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self , data):
        if self.root is None:
            self.root = Node(data)
        else:
            p = self.root
            while (1):
                if data < p.data:
                    p = p.left
                elif (data > p.data):
                    p = p.right
                else:
                    break

    def findNode(self, data):
        while (1):
            if (self.root == None):
                print("0")
                return
            elif (data > self.root.data):
                self.root = self.root.right
            elif (data < self.root.data):
                self.root = self.root.left
            else:
                print("1")
                return
        
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
    tree.addNode(i)

tree.postorder(tree.root)

M = int(sys.stdin.readline())

m_list = list(map(int, sys.stdin.readline().split()))

for j in m_list:
    tree.findNode(j)


