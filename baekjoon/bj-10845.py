class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedListQueue:
  def __init__(self):
    self.front = None
    self.rear = None

  def isEmpty(self):
    if self.front is None:
      return 1
    else:
      return 0
    
  def size(self):
    count = 0
    if self.isEmpty():
      return count
    
    p = self.rear

    while p != self.front:
      count += 1
      p = p.next
    
    return count + 1
  
  def enqueue(self, data):
    new_node = Node(data)

    if self.isEmpty():
      self.front = self.rear = new_node
    else:
      new_node.next = self.rear
      self.rear = new_node

  def dequeue(self):

    if self.isEmpty():
      return -1
    elif self.rear == self.front:
      return_data = self.front.data
      self.rear = self.front = None
      return return_data
    else:
      p = self.rear
      while p.next != self.front:
        p = p.next

      return_data = self.front.data
      self.front = p
      self.front.next = None

      return return_data
    
  def print_front(self):
    if self.isEmpty():
      return -1
    else:
      return self.front.data
    
  def print_rear(self):
    if self.isEmpty():
      return -1
    else:
      return self.rear.data

import sys

N = int(sys.stdin.readline())

Que = LinkedListQueue()

for i in range(N):
  word = sys.stdin.readline()

  if word == "pop\n":
    print(Que.dequeue())
  elif word == "size\n":
    print(Que.size())
  elif word == "empty\n":
    print(Que.isEmpty())
  elif word == "front\n":
    print(Que.print_front())
  elif word == "back\n":
    print(Que.print_rear())
  else:
    [word, data] = word.split()
    data = int(data)
    Que.enqueue(data)