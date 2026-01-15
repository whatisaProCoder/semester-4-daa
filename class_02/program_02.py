# Reverse a singly linked list

class Node:
  def __init__(self, value):  
    self.value = value  # 1
    self.next = None  # 1
    
class LinkedList:
  def __init__(self, value=None):  
    if value == None:  # 1
      self.head = None  # 0 or 1
      self.tail = None  # 0 or 1
      self.length = 0  # 0 or 1
    else:
      new_node = Node(value)  # 0 or 1
      self.head = new_node  # 0 or 1
      self.tail = new_node  # 0 or 1
      self.length = 1  # 0 or 1
  
  def print_list(self):  
    temp = self.head  # 1
    while temp is not None:  # (n+1)
      print(temp.value, end=" ")  # n
      temp = temp.next  # n
    print()  # 1
    
  def append(self, value):  
    new_node = Node(value)  # 1
    if self.head is None:  # 1
      self.head = new_node  # 0 or 1
      self.tail = new_node  # 0 or 1
    else:
      self.tail.next = new_node  # 0 or 1
      self.tail = new_node  # 0 or 1
    self.length +=  1  # 1
    return True  # 1
  
  def reverse(self):  
    temp = self.head  # 1
    self.head = self.tail  # 1
    self.tail = temp  # 1
    after = temp.next  # 1
    before = None  # 1
    for _ in range(self.length):  # (n+1)
      after = temp.next  # n
      temp.next = before  # n
      before = temp  # n
      temp = after  # n
      
linkedList = LinkedList(1)  # 1

linkedList.append(2)  # 1

linkedList.append(3)  # 1

linkedList.append(4)  # 1

print("LinkedList :-")  # 1

linkedList.print_list()  # 1

linkedList.reverse()  # 1

print("Reversed LinkedList :-")  # 1

linkedList.print_list()  # 1