class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if not self.length:
            return None
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append_list(self, value):
        new_node = Node(value)

        if not self.length:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1

    def pop(self):
        if not self.length:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if not self.length:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)

        if not self.length:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def pop_first(self):
        if not self.length:
            return None

        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1

        if not self.length:
            self.head = None
            self.tail = None

        return temp

    def get_index(self, value):
        if not self.length:
            return None

        temp = self.head
        index = 0
        while temp:
            if temp.value == value:
                return index
            index += 1
            temp = temp.next

        return -1

    def get_value(self, index):
        if index < 0 and index >= self.length:
            return None

        temp = self.head
        while index:
            temp = temp.next
            index -= 1

        return temp

    def set_value(self, index, value):
        if index < 0 and index >= self.length:
            return None

        temp = self.get_value(index)

        if temp:
            temp.value = value
            return True

        return False

    def insert(self, index, value):
        if index < 0 and index >= self.length:
            return None
        if index == 0:
            return self.prepend(vaue)
        if index == self.length:
            return self.append_list(value)

        temp = self.get_value(index - 1)
        new_node = Node(value)
        new_node.next = temp.next
        temp.next = new_node

        self.length += 1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get_value(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head, self.tail = self.tail, self.head
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


my_linked_list = LinkedList(4)
my_linked_list.append_list(5)
my_linked_list.append_list(6)
my_linked_list.append_list(9)
my_linked_list.set_value(2, 3)
my_linked_list.print_list()

my_linked_list.reverse()
my_linked_list.print_list()
