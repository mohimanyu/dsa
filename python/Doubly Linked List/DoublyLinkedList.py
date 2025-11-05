class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            if index <= self.length / 2:
                for _ in range(index):
                    temp = temp.next
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
            return temp

    def set_value(self, value, index):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next
        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.prev = None
        temp.after = None
        self.length -= 1
        return temp


# my_doubly_linked_list = DoublyLinkedList(7)
# my_doubly_linked_list.append(8)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop())
# my_doubly_linked_list.prepend(6)
# print(my_doubly_linked_list.pop_first().value)
# print(my_doubly_linked_list.get(2).value)
# my_doubly_linked_list.insert(0,1)

# my_doubly_linked_list.print_list()

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)


print("DLL before insert():")
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(1, 2)

print("\nDLL after insert(2) in middle:")
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(0, 0)

print("\nDLL after insert(0) at beginning:")
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(4, 4)

print("\nDLL after insert(4) at end:")
my_doubly_linked_list.print_list()
