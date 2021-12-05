# Quick Basic Examples to show the flow of Sets

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# simple addition to a set, which likewise work for Removing a value from a set

set1.add(6)
set2.add(9)

print(set1)
print(set2)

print("="*40)

set3 = set1 & set2          # The way to write an intersection using an "&"; the symbol for intersections 
print(set3)                 # It shows the values that BOTH sets have the same as a math operation             
print("="*40)               # of where the points of a line meet

set4 = set1 | set2        #  The way of writing a union using the "|" key, to combine the numbers 
print(set4)               # of BOTH previous sets, then to create a New set to say all numbers used!
print("="*40)

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)         # since sets don't allow duplicates, evene strings along            
print("="*40)         # with numbers follow that rule.


# Set Demo of operations on unique letters from two words like a ven diagram
# note: ORDER IS NOT IMPORTANT, only the PRESSENCE of EACH Value
a = set('abracadabra')
b = set('alacazam')

print(a)                         # detects all unique letters in a
# expected: {'a', 'b', 'c', 'd', 'r'}
print("="*40)

print(a - b)                          # detects all letters in set a but not in set b
# expected: {'b', 'd', 'r'}
print("="*40)

print(a | b)                             # finds letters in a or b or both
# expected: {'a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'}
print("="*40)

print(a & b)                          # letters in both a and b
# expected: {'a', 'c'}
print("="*40)
