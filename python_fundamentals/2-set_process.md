# “Be Set with Sets” – The basic layout and process of Sets
Some data structures would not necessarily worry about the order of the data. The data structure called "set" is an example of one for which order is not important. Sets do not allow duplicates. Most set implementations (including Python) will not give us an error when you try to add a duplicate value. This is done so that we can easily convert from a list, which may have duplicates, to a set that contains just the unique values.

The set does not keep values in order. a technique called hashing; in O(1) time, the Big O notation, the set is able to add, remove, and test for membership, See if the value one programs, is there or not. 
an index(n) hashing function  demonstartes that  the value added is not based on the order programmed.

To put in a visual perspective, The sets can be described as a ven diagram. Put a circle group of A and a circle
group of B and push them together, Sets can read out and output the items in the ven diagrams individually and 
what they have in common. even to *Combining* them.

# Commands to implement sets, and their meaning

Sets can be utilized in curly braces "{}" (my_set = {1, 2, 3}) an empty set (not like empty lists that we all know) writes out like this: "empty_set = set()". 

## Concepts of Set Operation commands

Quotes are indication for this writing to know how to write the code:

* *add(value)* - Adds "value" to the set	
    
    a. "my_set.add(value)"

* *remove(value)* - Removes the "value" from the set	
    
    b. "my_set.remove(value)"

* *member(value)* - Determines if "value" is in the set	
    
    c. "if value in my_set:"

* *size()* - Returns the number of items in the set	
    
    d. "length = len(my_set)"



## Example : a Demo of Sets
[=> examples of Sets at work <=](program_example2.py)



[Back to Welcome Page](0-welcome.md)