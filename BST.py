
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

    def getting_path(self, value, path=None):
        if value == self.value:
            result_list = [path, value]
            return result_list
        elif self.left and value < self.value:
            return self.left.getting_path(value, self.left)
            
        elif self.right and value >= self.value:
            return self.right.getting_path(value, self.right)
        
        else:
            return None 

    def delete_path(self, cur_path=None, path=None):
        path_to_delete = path
        value = path_to_delete[-1]
        
        if not self.right == None and self.right.value == value:
            self.right = None 
            return
        elif not self.left == None and self.left.value == value:
            self.left = None 
            return
        else:
            if value == self.value:
                return 
            elif self.left and value < self.value:
                self.left.delete_path(self.left, path)
            elif self.right and value >= self.value:
                self.right.delete_path(self.right, path)

    
    def insert_balance(self, new_value):
        if new_value < self.value:
            if self.left == None:
                self.left = BST(new_value, self.depth + 1)
                if self.right == None:
                    
                    while True:
                        right_val = int(input('Please enter a value that is greater than {parent}: '.format(parent=self.value)))
                        if right_val < self.value:
                            print("That value is not valid")    
                        else:
                            break
                    self.right = BST(right_val, self.depth + 1)
            else:
                self.left.insert_balance(new_value)
        else:
            if self.right == None:
                self.right = BST(new_value, self.depth + 1)
                if self.left == None:
                    
                    while True:
                        left_val = int(input("Please enter a value that is less than {parent}: ".format(parent=self.value)))
                        if left_val > self.value:
                            print('That value is not valid')
                        else:
                            break 
                    self.left = BST(new_value, self.depth + 1)
            else:
                self.right.insert_balance(new_value)      


    
            
            
     
    
        
    

