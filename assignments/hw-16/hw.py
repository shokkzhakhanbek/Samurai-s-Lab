from typing import List, Any, Dict, Set, Generator, Optional

class StaticArray:
    def __init__(self, capacity: int):
        """
        Initialize a static array of a given capacity.
        """
        if capacity <= 0:
            raise ValueError("capacity  positive")
        self.capacity = capacity
        self._data: List[Optional[int]] = [None] * capacity

    def _check_index(self, index: int) -> None:
        if index < 0 or index >= self.capacity:
            raise IndexError("index out of range")

    def set(self, index: int, value: int) -> None:
        """
        Set the value at a particular index.
        """
        self._check_index(index)
        self._data[index] = value

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        self._check_index(index)
        val = self._data[index]
        if val is None:
            raise ValueError("no value set at this index")
        return val


class DynamicArray:
    def __init__(self):
        """
        Initialize an empty dynamic array.
        """
        self._capacity = 2
        self._size = 0
        self._data: List[Optional[int]] = [None] * self._capacity

    def __len__(self) -> int:
        return self._size

    def _resize(self, new_capacity: int) -> None:
        new_data: List[Optional[int]] = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def _check_index(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("index out of range")

    def append(self, value: int) -> None:
        """
        Add a value to the end of the dynamic array.
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def insert(self, index: int, value: int) -> None:
        """
        Insert a value at a particular index.
        """
        if index < 0 or index > self._size:
            raise IndexError("index out of range")

        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def delete(self, index: int) -> None:
        """
        Delete the value at a particular index.
        """
        self._check_index(index)
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        if self._size > 0 and self._size <= self._capacity // 4 and self._capacity > 2:
            self._resize(max(2, self._capacity // 2))

    def get(self, index: int) -> int:
        """
        Retrieve the value at a particular index.
        """
        self._check_index(index)
        val = self._data[index]
        if val is None:
            raise ValueError("unexpected empty value")
        return val


class Node:
    def __init__(self, value: int):
        """
        Initialize a node.
        """
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.head = None
        self.tail = None

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return

        current = self.head
        prev = None
        current_position = 0

        while current is not None and current_position < position:
            prev = current
            current = current.next
            current_position += 1

        new_node.next = current
        if prev is not None:
            prev.next = new_node

        if new_node.next is None:
            self.tail = new_node

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        current = self.head
        prev = None

        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                if current.next is None:
                    self.tail = prev
                return
            prev = current
            current = current.next

    def find(self, value: int) -> Node:
        """
        Find a node with a specific value.
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.head is None

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        prev = None
        current = self.head
        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def get_head(self) -> Node:
        """
        Returns the head node of the linked list.
        """
        return self.head

    def get_tail(self) -> Node:
        """
        Returns the tail node of the linked list.
        """
        return self.tail

class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        """
        Initialize a double node with value, next, and previous.
        """
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        """
        Initialize an empty doubly linked list.
        """
        self.head = None
        self.tail = None

    def append(self, value: int) -> None:
        """
        Add a node with a value to the end of the linked list.
        """
        new_node = DoubleNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, position: int, value: int) -> None:
        """
        Insert a node with a value at a particular position.
        """
        new_node = DoubleNode(value)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return

        current = self.head
        current_position = 0

        while current is not None and current_position < position:
            current = current.next
            current_position += 1

        if current is None:
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node

            if new_node.prev is None:
                self.head = new_node

    def delete(self, value: int) -> None:
        """
        Delete the first node with a specific value.
        """
        current = self.head

        while current is not None:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def find(self, value: int) -> DoubleNode:
        """
        Find a node with a specific value.
        """
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        """
        Returns the number of elements in the linked list.
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.
        """
        return self.head is None

    def print_list(self) -> None:
        """
        Prints all elements in the linked list.
        """
        current = self.head
        while current is not None:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.
        """
        current = self.head
        self.tail = self.head

        while current is not None:
            current.prev, current.next = current.next, current.prev
            if current.prev is None:
                self.head = current
            current = current.prev

    def get_head(self) -> DoubleNode:
        """
        Returns the head node of the linked list.
        """
        return self.head

    def get_tail(self) -> DoubleNode:
        """
        Returns the tail node of the linked list.
        """
        return self.tail

class Queue:
    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items: List[int] = []

    def enqueue(self, value: int) -> None:
        """
        Add a value to the end of the queue.
        """
        self.items.append(value)

    def dequeue(self) -> int:
        """
        Remove a value from the front of the queue and return it.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self) -> int:
        """
        Peek at the value at the front of the queue without removing it.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.
        """
        return len(self.items) == 0

class TreeNode:
    def __init__(self, value: int):
        """
        Initialize a tree node with value.
        """
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

class BinarySearchTree:
    def __init__(self):
        """
        Initialize an empty binary search tree.
        """
        self.root: Optional[TreeNode] = None

    def _min_value_node(self, node: TreeNode) -> TreeNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def insert(self, value: int) -> None:
        """
        Insert a node with a specific value into the binary search tree.
        """
        if self.root is None:
            self.root = TreeNode(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return
                current = current.right

    def delete(self, value: int) -> None:
        """
        Remove a node with a specific value from the binary search tree.
        """
        def _delete_node(node: Optional[TreeNode], value: int) -> Optional[TreeNode]:
            if node is None:
                return None
            if value < node.value:
                node.left = _delete_node(node.left, value)
            elif value > node.value:
                node.right = _delete_node(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                temp = self._min_value_node(node.right)
                node.value = temp.value
                node.right = _delete_node(node.right, temp.value)
            return node

        self.root = _delete_node(self.root, value)

    def search(self, value: int) -> TreeNode:
        """
        Search for a node with a specific value in the binary search tree.
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return None

    def inorder_traversal(self) -> List[int]:
        """
        Perform an in-order traversal of the binary search tree.
        """
        result: List[int] = []

        def _inorder(node: Optional[TreeNode]) -> None:
            if node is not None:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return result

    def size(self) -> int:
        """
        Returns the number of nodes in the tree.
        """
        def _size(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self.root)

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty.
        """
        return self.root is None

    def height(self) -> int:
        """
        Returns the height of the tree.
        """
        def _height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def preorder_traversal(self) -> List[int]:
        """
        Perform a pre-order traversal of the tree.
        """
        result: List[int] = []

        def _preorder(node: Optional[TreeNode]) -> None:
            if node is not None:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
        return result

    def postorder_traversal(self) -> List[int]:
        """
        Perform a post-order traversal of the tree.
        """
        result: List[int] = []

        def _postorder(node: Optional[TreeNode]) -> None:
            if node is not None:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)

        _postorder(self.root)
        return result

    def level_order_traversal(self) -> List[int]:
        """
        Perform a level order (breadth-first) traversal of the tree.
        """
        result: List[int] = []
        if self.root is None:
            return result

        queue: List[TreeNode] = [self.root]

        while queue:
            current = queue.pop(0)
            result.append(current.value)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

        return result

    def minimum(self) -> TreeNode:
        """
        Returns the node with the minimum value in the tree.
        """
        if self.root is None:
            raise ValueError("Tree is empty")
        return self._min_value_node(self.root)

    def maximum(self) -> TreeNode:
        """
        Returns the node with the maximum value in the tree.
        """
        def _max_value_node(node: TreeNode) -> TreeNode:
            current = node
            while current.right is not None:
                current = current.right
            return current

        if self.root is None:
            raise ValueError("Tree is empty")
        return _max_value_node(self.root)

    def is_valid_bst(self) -> bool:
        """
        Check if the tree is a valid binary search tree.
        """
        def _is_valid_bst(node: Optional[TreeNode], low: Optional[int], high: Optional[int]) -> bool:
            if node is None:
                return True
            if (low is not None and node.value <= low) or (high is not None and node.value >= high):
                return False
            return _is_valid_bst(node.left, low, node.value) and _is_valid_bst(node.right, node.value, high)

        return _is_valid_bst(self.root, None, None)


def insertion_sort(lst: List[int]) -> List[int]:
    arr = lst[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(lst: List[int]) -> List[int]:
    arr = lst[:]
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(lst: List[int]) -> List[int]:
    arr = lst[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def shell_sort(lst: List[int]) -> List[int]:
    arr = lst[:]
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst[:]
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(lst: List[int]) -> List[int]:
    arr = lst[:]
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_helper(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_idx = i + 1
        _quick_sort_helper(arr, low, pivot_idx - 1)
        _quick_sort_helper(arr, pivot_idx + 1, high)