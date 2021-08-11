class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None
    
    def add_to_front(self, val):
        # Only one case
        new_node = SLNode(val) # a new instance of a SLNode is created
        current_head = self.head # temporary variable for saving the current head of the SList instance
        new_node.next = current_head # the old head of the SLlist is the link to the next node from the new node
        self.head = new_node # the new head of the SLlist is the one from the new node added
        return self	# return SList
    
    def add_to_back(self, val):
        # Case 1: if the list is empty 
        if self.head == None:	
            self.add_to_front(val)	# add_to_front method is runned (in this case it is the same to add a node to the front or to the back)
            return self	# return SList

        # Case 2: if the list is NOT empty
        new_node = SLNode(val) # a new instance of a SLNode is created
        runner = self.head # set an iterator called runner to start at the front of the list. Runner is a variable of the class SLNode      
        while (runner.next != None): # while loop for looking the last SLNode instance
            runner = runner.next # Traversing the list when the while loop is true
        runner.next = new_node	# The next node in the last SLNode is updated from "None" to the new node created. (Note: the atribute next from a SLNode class is also a SLnode class) 
        return self # return SList

    def insert_at(self, val, n):
        # Case 1: if the list is empty 
        if self.head == None:
            self.add_to_front(val) # The n position doesn't matter in this case
            return self	# return SList for case 1
        
        # Case 2: if the list is NOT empty 
        runner = self.head # set an iterator called runner to start at the front of the list. Runner is a variable of the class SLNode      
        # Case 2.1: the new node is going to be in the first position (n=0)
        if n == 0:
            self.add_to_front(val)
            return self # return SList for case 2.1
        
        counter = 0 # auxiliar variable for measuring the length of the SList
        while counter<n-1: # while loop for looking the node before the nth node selected
            # Case 2.2: the node with the given nth position is between 0 and the length of the list
            if(runner.next.next != None):
                runner = runner.next # Traversing the list when the while loop is true.
            
            # Case 2.3: the node with the given nth position is after is equal to the length of the list
            else:
                self.add_to_back(val)
                return self # return SList for case 2.3
            counter +=1

        # Only if Case 2.2 is given
        new_node = SLNode(val) # a new instance of a SLNode is created
        current_node_at_nth = runner.next # temporary variable for saving the node at the current nth  position
        new_node.next = current_node_at_nth # the next node of the new node inserted at nth position is updated as the one that used to be at nth position
        runner.next = new_node # the new node is linked to the node that is before the nth position

        return self # return SList for case 2.2

    def remove_from_front(self):
        # Case 1: if the list is empty 
        if self.head == None: 
            # There is no node to eliminate. SList is returnend
            return self	# return SList
        
        # Case 2: if the list is NOT empty 
        
        # Case 2.1: there is only one node in the list
        if(self.head.next == None):
            self.head = None # the unique node is taken out of the list. Thus, the list head is updated to "None"
            return self	# return SList for case 2.1

        # Case 2.2: there are two nodes or more in the list
        self.head = self.head.next # the new head is the next node to the current head
        return self # return SList for case 2.2
    
    def remove_from_back(self):
        # Case 1: if the list is empty 
        if self.head == None: 
            # There is no node to eliminate. SList is returnend
            return self	# return SList
        
        # Case 2: if the list is NOT empty 
        runner = self.head # set an iterator called runner to start at the front of the list. Runner is a variable of the class SLNode      
        # Case 2.1: there is only one node
        if runner.next == None:
            self.remove_from_front()
            return self # return SList for case 2.1
        
        # Case 2.2: there are two nodes or more
        while (runner.next.next != None): # while loop for looking the second-to-last SLNode instance (Note: because runner and its atribute next are a variable from the class SLNode, then the link to last node from the second-to-last node can be obteined as runner.next.next)
            runner = runner.next #Traversing the list when the while loop is true. We stop at the second-to-last node
        runner.next = None # Second-to-last node is updated for being the last node. Thus the link to next node is changed to None. 
        return self # return SList for case 2.2

    def remove_val(self, val):
        # Case 1: if the list is empty 
        if self.head == None: 
            # There is no node to eliminate. SList is returnend
            return self	# return SList
        
        # Case 2: if the list is NOT empty 
        runner = self.head # set an iterator called runner to start at the front of the list. Runner is a variable of the class SLNode      
        # Case 2.1: the node with the given value is the first node
        if runner.value == val:
            self.remove_from_front()
            return self # return SList for case 2.1
        while runner.next.value != val: # while loop for looking the node before the first node containing the value "val"
            # Case 2.2: the node with the given value is in the middle of the SList
            if(runner.next.next != None):
                runner = runner.next # Traversing the list when the while loop is true.
            # Case 2.3: the node with the given value is the last node
            else:
                self.remove_from_back
                return self # return SList for case 2.3
        
        # Only if Case 2.2 is given
        runner.next = runner.next.next # We eliminate the link to the first node that contain the value "val" from its previous node. Thus, the new link to the next node is going to be the node after the first node containning the value "val". 
   
        return self # return SList for case 2.2

    def print_values(self):
        runner = self.head # a pointer to the list's first node
        while (runner != None): # iterating while runner is a node and not None
            print(runner.value)
            runner = runner.next # set the runner to its neighbor
        return self	# once the loop is done, return self to allow for chaining


# Tests
print ("\nTest 1 - Output should be B and C \n")
sll = SList()
sll.add_to_front("B").add_to_front("A").add_to_back("C").remove_from_front().print_values()
print ("\nTest 2 - Output should be nothing \n")
sll2 = SList()
sll2.add_to_back("Z").add_to_back("Y").remove_from_back().remove_from_back().remove_from_back().remove_from_back().print_values()
print ("\nTest 3 - Output should be B,C and D \n")
sll3 = SList()
sll3.add_to_back("A").add_to_back("B").add_to_back("C").add_to_back("D").remove_val("A").print_values()
print ("\nTest 4 - Output should be A,B,C and D \n")
sll3 = SList()
sll3.add_to_back("A").add_to_back("B").add_to_back("D").insert_at("C",2).print_values()
