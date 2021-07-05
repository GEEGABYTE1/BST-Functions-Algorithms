class BST:
    def __init__(self, value, depth=1):
        self.value = value 
        self.depth = depth 
        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left == None:
                self.left = BST(new_value, self.depth + 1)
                print("Node {value} has been added to the left of {parent} at depth {depth}".format(value=new_value, parent=self.value, depth=self.depth + 1))
            else:
                self.left.insert(new_value)
        else:
            if self.right == None:
                self.right = BST(new_value, self.depth  + 1)
                print("Node {value} has been added to the right of {parent} at depth {depth}".format(value=new_value, parent=self.value, depth=self.depth + 1))
            else:
                self.right.insert(new_value)
        
    def get_node_by_value(self, value, level=0):
        level += 1
        if value == self.value:
            return self.value, level
        elif self.left and value < self.value:
            return self.left.get_node_by_value(value, level)
        elif self.right and value >= self.value:
            return self.right.get_node_by_value(value, level)
        else:
            return None 
    
    def depth_first_traversal(self):
        if self.left:
            self.left.depth_first_traversal()
        print('Depth: {depth}, Value: {value}'.format(depth=self.depth, value=self.value))
        if self.right:
            self.right.depth_first_traversal()
    

## Test ##

test = BST(1)
test.insert(2)
test.insert(3)
test.insert(4)
test.insert(5)

print(test.get_node_by_value(4))
test.depth_first_traversal()
