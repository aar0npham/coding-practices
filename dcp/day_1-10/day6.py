'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to 'get_pointer' and 'dereference_pointer'
functions that converts between nodes and memory addresses.
'''

class XOR_Node(object):
    def __init__(self, val, prev, next):
        self.val = val
        self.both = prev ^ next

    def next_node(self, prev_idx):
        return self.both ^ prev_idx

    def prev_node(self, next_idx):
        return self.both ^ next_idx

class XORLinkedList(object):
    def __init__(self):
        self.memory = [XOR_Node(None,-1,-1)]

    def head(self):
        return 0, -1, self.memory[0]  # head node idx, pre node idx, head node value

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
        self.memory.append(XOR_Node(val, current_node_idx, -1))

    def get(self, idx):
        current_idx, prev_idx, current_node = self.head()
        for current in range(idx+1):
            prev_idx, current_idx = current_idx, current_node.next_node(prev_idx)
            current_node = self.memory[current_idx]
        return current_node.val


# driver code
l = XORLinkedList()
for cnt in range(0,4):
    l.add(cnt)
l.get(2)==3
