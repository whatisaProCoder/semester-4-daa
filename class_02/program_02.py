# Reverse a singly linked list

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
class LinkedList:
  def __init__(self, value=None):
    if value == None:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      new_node = Node(value)
      self.head = new_node
      self.tail = new_node
      self.length = 1
  
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()
    
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length +=  1
    return True
  
  def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp
    after = temp.next
    before = None
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after
      
linkedList = LinkedList(1)

linkedList.append(2)

linkedList.append(3)

linkedList.append(4)

print("LinkedList :-")

linkedList.print_list()

linkedList.reverse()

print("Reversed LinkedList :-")

linkedList.print_list()