class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if data == self.data:
            return
        
        # FOr LEFT SUB TREE
        if data < self.data:
            # if its not a leaf node
            if self.left:
                self.left.add_child(data)
            # if its a leaf node 
            else:
                self.left = BinarySearchTree(data)
        # FOr RIGHT SUB TREE
        elif data > self.data:
            # if its not a leaf node
            if self.right:
                self.right.add_child(data)
            # if its a leaf node 
            else:
                self.right = BinarySearchTree(data)