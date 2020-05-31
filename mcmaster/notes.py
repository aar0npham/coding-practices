import math
'''Useful algorithm for ICPC'''

'--------------------------------------------------------------------------------------------------------------------'

# Example array
arr1 = [10, 43, 1, 5, 32, 9, 4]
arr2 = [-1, 4, 3, 5, 1]

'--------------------------------------------------------------------------------------------------------------------'


class SortingAlgorithm:
    '''1. Sorting algorithm'''
    # Cheat way to sort array very fasty boi
    # sorted()

    def merge_sort(self, arr):
        '''Merge sort - O(nlog(n))'''
        if len(arr) < 2:
            return arr
        result = []
        mid = int(len(arr) / 2)
        l, r = self.merge_sort(arr[:mid]), self.merge_sort(arr[mid:])
        i, j = 0, 0
        while i < len(l) and j < len(r):
            if l[i] > r[j]:
                result.append(r[j])
                j += 1
            else:
                result.append(l[i])
                i += 1
        result += l[i:]
        result += r[j:]
        return result
    # print(merge_sort(arr1))

    def quick_sort(self, arr):
        '''Quick sort - O(n^2)'''
        lower = []
        equal = []
        upper = []

        if len(arr) > 1:
            p = arr[0]
            for x in arr:
                if x < p:
                    lower.append(x)
                elif x == p:
                    equal.append(x)
                elif x > p:
                    upper.append(x)
            return self.quick_sort(lower) + equal + self.quick_sort(upper)
        else:
            return arr
    # print(quick_sort(arr1))

    def insertion_sort(self, arr):
        '''Insertion sort - O(n^2)'''
        for i in range(1, len(arr)):
            tmp = arr[i]
            k = i
            while k > 0 and tmp < arr[k - 1]:
                arr[k] = arr[k - 1]
                k -= 1
            arr[k] = tmp
        return arr
    # print(insertion_sort(arr1))


'--------------------------------------------------------------------------------------------------------------------'


class SearchAlgorithm:
    '''2. Search algorithm'''
    def binary_search(self, arr, target):
        '''Binary search - O(log(n))'''
        lower = 0
        upper = len(arr)
        while lower < upper:
            mid = lower + (lower + upper) // 2
            if arr[mid] == target:
                return mid
            elif target < arr[mid]:
                lower = mid + 1
            else:
                upper = mid - 1
        return -1
    # print(binary_search(sorted(arr1),4))

'--------------------------------------------------------------------------------------------------------------------'


class Tree:
    '''3. Tree'''
    class TreeNode:
        def __init__(self, val, left, right):
            self.val = val
            self.left = left
            self.right = right



        '''deserialize, serialize tree to string refers to day3.py'''


'--------------------------------------------------------------------------------------------------------------------'

'''4. Array'''

'--------------------------------------------------------------------------------------------------------------------'

'''5. Stack, Queue, Deque'''

'--------------------------------------------------------------------------------------------------------------------'


class LinkedList:
    '''6. Linked List'''
    # linear data structure consists of node and pointer to the reference node
    # pretty complex comparing to Array since runtime might be worse, however, constant space and time for modifying value

    '''6.1 Singly Linked List'''
    class _SLLNode:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    class SinglyLinkedStack(_SLLNode):
        '''LIFO Stack implementation'''

        def __init__(self):
            self._head = None
            self._size = 0

        def __len__(self):
            return self._size

        def is_empty(self):
            return self._size == 0

        def push(self, e):
            self._head = self._SLLNode(e, self._head)
            self._size += 1

        def top(self):
            # return first element of the stack
            if self.is_empty():
                raise Exception('Empty Stack')
            else:
                return self._head._element

        def pop(self):
            if self.is_empty():
                raise Exception('Empty Stack')
            val = self._head._element
            self._head = self._head._next
            self._size -= 1
            return val

    class SinglyLinkedQueue(_SLLNode):
        '''FIFO Queue implementation for Singly Linked List'''

        def __len__(self):
            return self._size

        def is_empty(self):
            return self._size == 0

        def first(self):
            # Return the first element in the queue
            if self.is_empty():
                raise Exception('Empty Queue')
            else:
                return self._head._element

        def dequeue(self):
            # remove and return the first element of the queue
            if self.is_empty():
                raise Exception('Empty Queue')
            val = self._head._element
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():
                self._tail = None
            return val

        def enqueue(self, e):
            # add element back to the queue
            val = self._SLLNode(e, None)
            if self.is_empty():
                self._head = val
            else:
                self._tail._next = val
            self._tail = val
            self._size += 1

        # Circular Linked List
        def rotate(self):
            if self._size > 0:
                self._tail = self._tail._next

    '''6.2 Doubly Linked List'''
    # added sentinel, essentially dummy header and trailer node with empty value
    # can reference back and forward ==> XOR liked list
    # Advantages: Dynamically add/delete value from linked list
    class _DLLNode:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    class _DoublyLinkedList(_DLLNode):
        def __init__(self):
            self._header = self._DLLNode(None, None, None)
            self._trailer = self._DLLNode(None, None, None)
            self._header._next = self._trailer
            self._trailer._prev = self._header
            self._size = 0

        def __len__(self):
            return self._size

        def is_empty(self):
            return self._size == 0

        def _insert(self, e, left, right):
            # insert value e between two existing node
            val = self._DLLNode(e, left, right)
            left._next = val
            right._prev = val
            self._size += 1
            return val

        def _delete_node(self, node):
            left = node._prev
            right = node._next
            left._next = right
            right._prev = left
            self._size -= 1
            e = node._element
            node._prev = node._next = node._element = None
            return e

    class DoublyLinkedDeque(_DoublyLinkedList):
        '''Double-ended queue implementation'''

        def first(self):
            if self.is_empty():
                raise Exception('Empty Deque')
            return self._header._next._element

        def last(self):
            if self.is_empty():
                raise Exception('Empty Deque')
            return self._trailer._prev._element

        def insert_first(self, e):
            self._insert(e, self._header, self._header._next)

        def insert_last(self, e):
            self._insert(e, self._trailer._prev, self._trailer)

        def delete_first(self):
            if self.is_empty():
                raise Exception('Empty Deque')
            return self._delete_node(self._header._next)

        def delete_last(self):
            if self.is_empty():
                raise Exception('Empty Deque')
            return self._delete_node(self._trailer._prev)

    '''6.3 Positional List'''
    # Dynamically access node, implements DoublyLinkedList
    # Using insertion sort for PositionalList
    def insertion_sort(self, L):
        if len(L) > 1:
            marker = L.first()
            while marker != L.last():
                p = L.after(marker)
                val = p.element()
                if val > marker.element():
                    marker = p
                else:
                    w = marker
                    while w != L.first() and L.before(w).element().val:
                        w = L.before(w)
                    L.delete(p)
                    L.add_before(w, val)

    class PositionalList(_DoublyLinkedList):
        class Position:
            def __init__(self, container, node):
                self._container = container
                self._node = node

            def element(self):
                return self._node._element

            def __eq__(self, other):
                return type(other) is type(self) and other._node is self._node

        def _validate(self, p):
            # Return positions' node
            if not isinstance(p, self.Position):
                raise TypeError('p must be Position type')
            if p._container is not self:
                raise ValueError('p doesn\'t belong to the container')
            if p._node._next is None:
                raise ValueError('p isn\'t valid')
            return p._node

        def _make_position(self, node):
            # Return position instance for given node (None if sentinel)
            if node is self._header or node is self._trailer:
                return None
            else:
                return self.Position(self, node)

        def first(self):
            return self._make_position(self._header._next)

        def last(self):
            return self._make_position(self._trailer._prev)

        def before(self, p):
            # Return position before p
            node = self._validate(p)
            return self._make_position(node._prev)

        def after(self, p):
            # return position after p
            node = self._validate(p)
            return self._make_position(node._next)

        def __iter__(self):
            # Generate forward iteration of the List
            cur = self.first()
            while cur is not None:
                yield cur.element()
                cur = self.after(cur)

        # Overriding inherrited method
        def _insert(self, e, left, right):
            node = super()._insert(e, left, right)
            return self._make_position(node)

        def add_first(self, e):
            # insert new element e to the front and return position
            return self._insert(e, self._header, self._header._next)

        def add_last(self, e):
            # insert new element e to the back and return position
            return self._insert(e, self._trailer._prev, self._trailer)

        def add_before(self, p, e):
            # insert element e before p and return position
            org = self._validate(p)
            return self._insert(e, org._prev, org)

        def add_after(self, p, e):
            # insert element e after p and return position
            org = self._validate(p)
            return self._insert(e, org, org._next)

        def delete(self, p):
            # remove and return element at p
            org = self._validate(p)
            return self._delete_node(org)

        def replace(self, p, e):
            # replace element at position p with e. return the element formely at position p
            org = self._validate(p)
            old = org._element
            org._element = e
            return old

    '''6. XOR Linked List'''
    # refer to day6.py
    class XORLinkedList(object):
        class XORNode(object):
            def __init__(self, val, prev, next):
                self.val = val
                self.both = prev ^ next

            def next_node(self, prev_idx):
                return self.both ^ prev_idx

            def prev_node(self, next_idx):
                return self.both ^ next_idx

        def __init__(self):
            self.memory = [self.XORNode(None, -1, -1)]

        def head(self):
            # head node idx, pre node idx, head node value
            return 0, -1, self.memory[0]

        def add(self, val):
            current_node_idx, prev_node_idx, current_node = self.head()
            while True:
                next_node_idx = current_node.next_node(prev_node_idx)
                if next_node_idx == -1:
                    break
                prev_node_idx, current_node_idx = current_node_idx, next_node_idx
                current_node = self.memory[next_node_idx]

            new_node_idx = len(self.memory)
            current_node.both = prev_node_idx ^ new_node_idx
            self.memory.append(self.XORNode(val, current_node_idx, -1))

        def get(self, idx):
            current_idx, prev_idx, current_node = self.head()
            for current in range(idx + 1):
                prev_idx, current_idx = current_idx, current_node.next_node(
                    prev_idx)
                current_node = self.memory[current_idx]
            return current_node.val


'--------------------------------------------------------------------------------------------------------------------'


class Appendix_I:
    '''A. Appendix I'''
    def min_pos_int(self, arr):
        '''sfind lowest positive integer that doesn't exist in array, refers to day4.py'''
        m = max(arr)
        z_arr = ['-'] * m
        for i in arr:
            if i > 0:
                z_arr[i - 1] = 'x'
        # print(z_arr)
        try:
            return z_arr.index('-') + 1
        except:
            return m + 1
    # print(min_pos_int(arr2))
    '''Using ceil() and floor()'''
    math.floor(-12.00)  # return largest integer not greater than # XXX:
    math.ceil(12.00)  # return smallest integer not less than x

    def manachers(self, S):
        """
        O(n) algorithm to find longest palindrome substring
        :param S: string to process
        :return: longest palindrome
        """

        # Create a copy of array with sentinel chars in between and around
        # Also include space for starting and ending nodes
        T = [0] * (2 * (len(S)) + 3)

        # Fill odd indices with sentinel chars evens with real chars
        sen_char = "@"
        start_sen = "!"
        end_sen = "#"
        for i in range(len(T)):
            if i == 0:
                T[i] = start_sen
            elif i % 2 == 0 and i < len(T) - 1:
                s_index = (i - 1) // 2
                T[i] = S[s_index]
            elif i % 2 == 1 and i < len(T) - 1:
                T[i] = sen_char
            else:
                T[i] = end_sen

        # Also track the expand length around all indices
        P = [0] * len(T)

        # Track center of largest palin yet
        # and its right boundary
        center = right = 0

        # Track largest expansion length
        # and it index
        max_len = index = 0

        # Loop through word array to
        # update expand length around each index
        for i in range(1, len(T) - 1):

            # Check to see if new palin
            # around i lies within a bigger one
            # If so, copy expand length of its mirror
            mirror = 2 * center - i
            if i < right:
                P[i] = min(right - i, P[mirror])

            # Expand around new center
            # Update expand length at i as needed
            while T[i + P[i] + 1] == T[i - (P[i] + 1)]:
                P[i] += 1

            # If we breached previous right boundary
            # Make i the new center of the longest palin
            # and update right boundary
            if i + P[i] > right:
                right = i + P[i]
                center = i

            # Update max_len
            if P[i] > max_len:
                max_len = P[i]
                index = i

        t_arr = T[ index - max_len: index + max_len + 1 ]
        word_arr = [ c for c in t_arr if c != sen_char and c != start_sen and c != end_sen ]
        word = "".join(word_arr)

        return word

'--------------------------------------------------------------------------------------------------------------------'

value = 13
result = 'default'

if value == 7:
    result ='lucky'
elif value == 13:
    result = 'unlucky'
else:
    result='boring'