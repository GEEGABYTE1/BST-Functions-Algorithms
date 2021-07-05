# BST Functions/Algorithms 
 
Extra Functions and Algorithms for Binary Search Tree 🔍🌳

# Delete Function 🗑

The delete function is called `.delete_path()` , which will delete a certain path with a certain value in it .

It takes a path that will be outputted by another function called `.getting_path()` that returns the path of certain value. 

`.delete_path()` will check a node further instead of the current node. Essentially, it will check if the value prompted is in the child's node children, if it is, it will make that current path be set to `None`. 

Time Complexity: `O(N)` (Includes `.getting_path()`) 


# Self-Balancing Algorithm ⚖️

You can probably figure out what this algorithm does by just reading it's name. It essentially makes the tree balanced by having each parent node with two 2 child nodes. In other words, at each depth, there will be an even number of nodes. This algorithm will make sure that the max-depth of the BST will be for sure `O(log n)`

This algorithm is a little mash-up of the original `.insert()` function. Instead of having a conditional that checks if either the left path or a right path is empty for each parent node, and then adds a new BST object to that very path; this algorithm will do the same thing, but will also add a new BST object of a certain value (smaller than parent if it is going to the left path, or greater if it is going to the right path) to the other path as well if that is also empty (which is the case in most cases).

In my algorithm, I have set user-inputs where users can choose their valid inputs. Since the inputs are at random (check `test.py`), it does not really matter what the inputs are as long as there are int type. 

Time Complexity: `O(log n)`

# More Information 

`test.py` has all the test inputs. You can add your own test inputs if you would like.

The other functions (functions that have not been mentioned in this file) are base functions, and are not recommended to mess with unless you know what you are doing. 

Made in Python 🐍



