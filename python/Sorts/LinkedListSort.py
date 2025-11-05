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
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        if not self.head or not self.head.next:
            return

        for i in range(self.length - 1, 0, -1):
            current = self.head
            swapped = False

            for _ in range(i):
                after = current.next
                if current.value > after.value:
                    current.value, after.value = after.value, current.value
                    swapped = True
                current = after

            if not swapped:
                break

    def selection_sort(self):
        if not self.head or not self.head.next:
            return

        temp = self.head
        while temp and temp.next:
            min_node = temp
            current = temp.next
            while current:
                if current.value < min_node.value:
                    min_node = current
                current = current.next
            if temp.value != min_node.value:
                temp.value, min_node.value = min_node.value, temp.value
            temp = temp.next

    def sorted_insert(self, sorted_head, new_node):
        if not sorted_head or new_node.value < sorted_head.value:
            new_node.next = sorted_head
            return sorted_head

        current = sorted_head
        while current.next and current.next.value < new_node.value:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head

    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

# my_linked_list.bubble_sort()

# print("\nBubble Sorted Linked List:")
# my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

# my_linked_list.selection_sort()

# print("\nSelection Sorted Linked List:")
# my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

my_linked_list.insertion_sort()

print("\Insertion Sorted Linked List:")
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""
