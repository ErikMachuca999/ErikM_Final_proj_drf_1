
# A Binary Search Tree Example to Program
#                 50
#              /	 \
#            30       70
#           /  \      / \
#          20  40   60   80

# for the binary search tree, 
# needs first a node to start inserting data in

class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A function to insert
# a new node with the given key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

# make a function to do in_order tree traversal

def in_order(root):
	if root:
		in_order(root.left)
		print(root.val)
		in_order(root.right)


r = Node(50)
r = insert(r, 30)    # written code to use the inputs desired
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print in_order FUNCTION traversal of the BST
in_order(r)

# expected output shall be:
# 20
# 30
# 40
# 50
# 60
# 70
# 80