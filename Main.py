import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
       if self.top == -1 :
     return 1
    else :
     return 0

    def is_full(self):
         if self.top == (self.size - 1) :
     return 1
    else :
     return 0

    def push(self, data):
        if not self.is_full():
          print("The stack is full")
          return "Push is not allowed"
      else:
          self.top = self.top+1
          self.l[self.top]=y

    def pop(self):
        if not self.is_empty():
              return "the stack is empty"
      else:
          print(self.l[self.top])
          self.top = self.top-1
          return "Array removed"

    def status(self):
        # Write code here

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
