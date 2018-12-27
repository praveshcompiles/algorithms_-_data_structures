# A complete working Python program to demonstrate all 
# insertion methods and delete method of linked list 
  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
    # Functio to insert a new node at the beginning 
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #        Put in the data 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node 
  
  
    # This function is in LinkedList class. Inserts a 
    # new node after the given prev_node. This method is 
    # defined inside LinkedList class shown above */ 
    def insertAfter(self, prev_node, new_data): 
  
        # 1. check if the given prev_node exists 
        if prev_node is None: 
            print "The given previous node must inLinkedList."
            return
  
        #  2. create new node & 
        #      Put in the data 
        new_node = Node(new_data) 
  
        # 4. Make next of new Node as next of prev_node 
        new_node.next = prev_node.next
  
        # 5. make next of prev_node as new_node 
        prev_node.next = new_node 
  
  
    # This function is defined in Linked List class 
    # Appends a new node at the end.  This method is 
    # defined inside LinkedList class shown above */ 
    def append(self, new_data): 
  
        # 1. Create a new node 
        # 2. Put in the data 
        # 3. Set next as None 
        new_node = Node(new_data) 
  
        # 4. If the Linked List is empty, then make the 
        #    new node as head 
        if self.head is None: 
            self.head = new_node 
            return
  
        # 5. Else traverse till the last node 
        last = self.head 
        while (last.next): 
            last = last.next
  
        # 6. Change the next of last node 
        last.next =  new_node 

    # Given a reference to the head of a list and a key, 
    # delete the first occurence of key in linked list 
    def deleteNode(self, key): 
          
        # Store head node 
        temp = self.head 
  
        # If head node itself holds the key to be deleted 
        if (temp is not None): 
            if (temp.data == key): 
                self.head = temp.next
                temp = None
                return
  
        # Search for the key to be deleted, keep track of the 
        # previous node as we need to change 'prev.next' 
        while(temp is not None): 
            if temp.data == key: 
                break 
            prev = temp 
            temp = temp.next 
  
        # if key was not present in linked list 
        if(temp == None): 
            return 
  
        # Unlink the node from linked list 
        prev.next = temp.next 
  
        temp = None 
  
    # Utility function to print the linked list 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print temp.data, 
            temp = temp.next


# Python program to find n'th node from end using slow 
# and fast pointer


def printNthFromLast(self, n): 
        main_ptr = self.head 
        ref_ptr = self.head  
      
        count  = 0 
        if(self.head is not None): 
            while(count < n ): 
                if(ref_ptr is None): 
                    print "%d is greater than the no. pf nodes in list" %(n) 
                    return
   
                ref_ptr = ref_ptr.next
                count += 1
  
        while(ref_ptr is not None): 
            main_ptr = main_ptr.next 
            ref_ptr = ref_ptr.next
  
        print "Node no. %d from last is %d " %(n, main_ptr.data) 