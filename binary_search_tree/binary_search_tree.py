from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        new_node = BinarySearchTree(value)
        while True:
            if value < node.value:

                if node.left is None:
                    node.left = new_node
                    break
                node = node.left

            else:
                if node.right is None:
                    node.right = new_node
                    break
                node = node.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            if self.right is None:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        while self.right is not None:
            self = self.right
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # second pass recursive solution
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        tmp = node
        q.enqueue(tmp)
        while q.len() > 0:
            tmp = q.dequeue()
            print(tmp.value)
            if tmp.left:
                q.enqueue(tmp.left)
            if tmp.right:
                q.enqueue(tmp.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stk = Stack()
        tmp = node
        stk.push(tmp)
        while stk.len() > 0:
            tmp = stk.pop()
            print(tmp.value)
            if tmp.left:
                stk.push(tmp.left)
            if tmp.right:
                stk.push(tmp.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
