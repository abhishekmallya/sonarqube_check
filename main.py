class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        runner = self.head
        while runner is not None:
            print(f'{runner.value} -> ', end ='')
            runner = runner.next
        print('None')

    def append_node(self,  value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop_node(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = self.tail = None
        return temp.value
    
    def prepend_node(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head 
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value
            
            
    
my_linked_list = LinkedList(4)
my_linked_list.append_node(5)
my_linked_list.append_node(6)
my_linked_list.prepend_node(0)
my_linked_list.print_list()
print(my_linked_list.get(1))
print(my_linked_list.head.value, my_linked_list.tail.value)
