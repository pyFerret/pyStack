class Stack:
  def __init__(self):
    self.stack = []
    
  def push(self, _val):
    self.stack.append(_val)

  def pop(self):
    result = self.stack[-1]
    self.stack.pop()
    return result

  def read(self):
    return self.stack
