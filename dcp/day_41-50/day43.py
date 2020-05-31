'''
This problem was asked by Amazon.

Implement a stack that has the following methods:

    push(val), which pushes an element onto the stack
    pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
    max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
'''

class Stack:
    def __init__(self):
        self.st = list()

    def push(self, val):
        return self.st.append(val)

    def pop(self):
        if len(self.st)==0:
            raise ValueError('Length error')
        else:
            return self.st.remove(self.st[0])

    def max(self):
        return max(self.st)


s = Stack()
s.push(1)
s.push(3)
s.push(7)
for i in s:
    print(i)
print(s.max())
s.pop()
for i in s:
    print(i)
