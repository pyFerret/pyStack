# pyStack

#### This module is a dumbed down stack manager for python.

To use it, download the `stack.py` file, make sure it is in the same folder as the project you are working on and write `import stack`

---

#### Functions

`stack.Stack()` no arguments taken; Creates a new stack; use: `stack_name = stack.Stack()`

`stack_name.push()` takes any type of value; Pushes value given anto the top of the stack

`stack_name.pop()` no arguments taken; Returns and deletes the last value from the stack

`stack_name.read()` no arguments taken; Returns but does not delete the last value from the stack

NOTE: `pop` and `read` need to be printed if this is desired, they will not print themselves. This is done with the following code: `print(stack_name.read()` / `print(stack_name.read)`

---

##### For Future Releases
 - [ ] `read()` function should be able to read certain values/ranges of values
