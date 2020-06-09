class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
        return self.next

# node = Node(1)
# node.set_next(Node(2))
# node.get_next().set_next(Node(3))
# node.get_next().get_next().set_next(Node(4))

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        newNode = Node(value)
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.set_next(newNode)
            self.tail = newNode
    
    def remove_tail(self):
        if self.tail is None:
            return None
        value = self.tail.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
        return value

    def remove_head(self):
        if self.head is None:
            return None
        deleted_head = self.head.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.get_next()
        return deleted_head

    def get_max(self):
        if self.head is None:
            return None
        max_so_far = self.head.get_value()
        current = self.head.get_next()
        while current is not None:
            if current.get_value() > max_so_far:
                max_so_far = current.get_value()
            current = current.get_next()
        return max_so_far


    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current is not None:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False