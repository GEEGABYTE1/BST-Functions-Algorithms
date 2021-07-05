from BST import BST
import random

## Test ##

'''test = BST(1)
test.insert(2)
test.insert(3)
test.insert(4)
test.insert(5)'''

#print(test.get_node_by_value(4))

## Delete Function Test ##
''' first_part = test.getting_path(5)
print(first_part)
test.delete_path(path=first_part)
'''
## ##

## Self-Balance Function ##
test = BST(random.randint(1, 20))
for number in range(4):
    test.insert_balance(random.randint(1, 20))


## ##

test.depth_first_traversal()



## ##