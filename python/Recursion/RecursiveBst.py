class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class RecursiveBST:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None:
            current_node = Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if not self.root:
            self.root = Node(value)
        return self.__r_insert(self.root, value)

    def __r_contains(self, current_node, value):
        if not current_node:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left

        return current_node.value

    def __r_delete(self, current_node, value):
        if not current_node:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value < current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if not current_node.left and not current_node.right:
                current_node = None
            elif not current_node.left:
                current_node = current_node.right
            elif not current_node.right:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)

        return current_node

    def r_delete(self, value):
        return self.__r_delete(self.root, value)


my_tree = RecursiveBST()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

my_tree.r_delete(2)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right)

print(my_tree.r_contains(2))
print(my_tree.min_value(my_tree.root))
