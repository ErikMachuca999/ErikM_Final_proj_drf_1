# Python program to
# demonstrate stack implementation
# using list
 
stack = []
 
# remember, the append() function is the ling 
# to push an element in the stack
stack.append('1')
stack.append('2')
stack.append('3')
 
print('The Stack')
print(stack)
 
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
