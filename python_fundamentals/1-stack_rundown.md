# “Fax about Stax”- The rundown about Stacks

## First glance fast explanation

 A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert and delete operations are called push and pop.

## A Neat analogy for sweet tooths and others
If you were going to make pancakes to eat, a stack of the hot pancakes on as they finished cooking. Each time we put a pancake onto the stack, that is called a push. from the analogy, we say that each new pancake goes onto the top of the stack. 

However, since we are going to implement our stacks in Python, we will say that the pancake is actually added to the back. When we take a pancake off to eat, we call this a pop operation.  The push and pop start  from the back of the stack. in short, The bottom is considered *First*. the Top is *LAST*.

Removing from the middle of the stack is not allowed and jsut can't be done in both aspects of programming and reality without it being messy. 


## Multiple Commands to utilize stacks, and their concepts

* *push(value)* - Inserts the element of your ‘value’, (whatever implemented) to the back of the stack. 
 
    a.  Quotes are indication for this writing to know how to write the code: 
 " stack_name.append(value) ". The append() is utilze for pushing values in stacks.

* *pop()* - Removes and returns the item from the back of the stack.

    b. " value_name = stack_name.pop() ". uses the actual name. pop().

* *empty()* - Returns the condition of the stack when it is empty 

    c. The concept of this command NEEDS a boolean! also an if statement...
 
        " if len(stack_name) == 0: 
        
             return True"

* *size()* - returns the size of the stack.

    d. use the function len() to return lengths of lists. Stacks Can utlize lists. 
" length = len(stack_name) " 


## Example : a Stack in action
[=> a Stack in action <=](program_example1.py)



[Back to Welcome Page](0-welcome.md)



