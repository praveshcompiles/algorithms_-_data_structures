# Tree Traversals

# Python program to print level order traversal using Queue 
  
# A node structure 
class Node: 
    # A utility function to create a new node 
    def __init__(self ,key): 
        self.data = key 
        self.left = None
        self.right = None
  
# Iterative Method to print the height of binary tree 
def printLevelOrder(root): 
    # Base Case 
    if root is None: 
        return
      
    # Create an empty queue for level order traversal 
    queue = [] 
  
    # Enqueue Root and initialize height 
    queue.append(root) 
  
    while(len(queue) > 0): 
        # Print front of queue and remove it from queue 
        print queue[0].data, 
        node = queue.pop(0) 
  
        #Enqueue left child 
        if node.left is not None: 
            queue.append(node.left) 
  
        # Enqueue right child 
        if node.right is not None: 
            queue.append(node.right) 


# A function to do inorder tree traversal 
def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.val), 
  
        # now recur on right child 
        printInorder(root.right) 
  
  
  
# A function to do postorder tree traversal 
def printPostorder(root): 
  
    if root: 
  
        # First recur on left child 
        printPostorder(root.left) 
  
        # the recur on right child 
        printPostorder(root.right) 
  
        # now print the data of node 
        print(root.val), 
  
  
# A function to do preorder tree traversal 
def printPreorder(root): 
  
    if root: 
  
        # First print the data of node 
        print(root.val), 
  
        # Then recur on left child 
        printPreorder(root.left) 
  
        # Finally recur on right child 
        printPreorder(root.right) 



# A recursive python program to find LCA of two nodes 
# n1 and n2 
  
# A Binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
# Function to find LCA of n1 and n2. The function assumes 
# that both n1 and n2 are present in BST 
def lca(root, n1, n2): 
      
    # Base Case 
    if root is None: 
        return None
  
    # If both n1 and n2 are smaller than root, then LCA 
    # lies in left 
    if(root.data > n1 and root.data > n2): 
        return lca(root.left, n1, n2) 
  
    # If both n1 and n2 are greater than root, then LCA 
    # lies in right  
    if(root.data < n1 and root.data < n2): 
        return lca(root.right, n1, n2) 
  
    return root 


# Check if two trees are identical
def areIdentical(root1, root2): 
      
    # Base Case 
    if root1 is None and root2 is None: 
        return True
    if root1 is None or root2 is None: 
        return False
  
    # Check if the data of both roots is same and data of 
    # left and right subtrees are also same 
    return (root1.data == root2.data and 
            areIdentical(root1.left , root2.left)and
            areIdentical(root1.right, root2.right) 
            )  



# function to check if tree is height-balanced or not 

def isBalanced(root): 
      
    # Base condition 
    if root is None: 
        return True
  
    # for left and right subtree height 
    lh = height(root.left) 
    rh = height(root.right) 
  
    # allowed values for (lh - rh) are 1, -1, 0 
    if (abs(lh - rh) <= 1) and isBalanced( 
    root.left) is True and isBalanced( root.right) is True: 
        return True
  
    # if we reach here means tree is not  
    # height-balanced tree 
    return False

# function to find height of binary tree 
def height(root): 
      
    # base condition when binary tree is empty 
    if root is None: 
        return 0
    return max(height(root.left), height(root.right)) + 1



# Creating a BST from a sorted Array
def sortedArrayToBST(arr): 
      
    if not arr: 
        return None
  
    # find middle 
    mid = (len(arr)) / 2
      
    # make the middle element the root 
    root = Node(arr[mid]) 
      
    # left subtree of root has all 
    # values <arr[mid] 
    root.left = sortedArrayToBST(arr[:mid]) 
      
    # right subtree of root has all  
    # values >arr[mid] 
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 