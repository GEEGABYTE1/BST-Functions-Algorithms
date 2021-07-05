 BST Functions/Algorithms 
 
Extra Functions and Algorithms for Binary Search Tree 🔍🌳

# Delete Function 

The delete function is called `.delete_path()` , which will delete a certain path with a certain value in it .

It takes a path that will be outputted by another function called `.getting_path()` that returns the path of certain value. 

`.delete_path()` will check a node further instead of the current node. Essentially, it will check if the value prompted is in the child's node children, if it is, it will make that current path be set to `None`. 

Time Complexity: `O(N)` (Includes `.getting_path()`) 




