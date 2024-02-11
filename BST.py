class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __insert__(self,data):
        if self.data is None:
            self.data = data
            return

        if data <= self.data:
            if self.left:
                self.left.__insert__(data)
            else:
                self.left = BST(data)

        if data > self.data:
            if self.right:
                self.right.__insert__(data)
            else:
                self.right = BST(data)

    def search(self,data):
        if self.data == data:
            print("\nData exist in the Tree!!")
            return

        if data <= self.data:
            if self.left:
                self.left.search(data)
            else:
                print("\nNode not present in tree!!")

        if data > self.data:
            if self.right:
                self.right.search(data)
            else:
                print("\nNode not present at the tree!!")

    

    def delete(self,data):
        if self.data is None:
            print("Tree is Empty!")
            return self
        if data <= self.data:
            if self.left:
                self.left = self.left.delete(data)
        if data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp

            elif self.right is None:
                temp = self.left
                self = None
                return temp

            temp = self.right
            while temp.left is not None:
                temp = temp.left
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self

    def preorder(self):
        print(self.data,end = " ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
            
        print(self.data,end = ' ')
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data,end = ' ')



bst = BST(None)
while True:
    print("Choices:\n 1.insert \n 2.delete \n 3.search \n 4.Traversal")

    op = input("Enter:")

    if op.lower() == 'insert':
        n = int(input("Enter the no. of nodes:"))
        for i in range(n):
            bst.__insert__(int(input("Enter the value:")))
        print("Done!")

    if op.lower() == 'delete':
        bst.delete(int(input("Enter the value:")))
        print("Done!")

    if op.lower() == 'search':
        bst.search(int(input("Enter the value: ")))

    if op.lower() == 'traversal':
        print("preorder traversal:")
        bst.preorder()
        print()
        print("Postorder Traversal:")
        bst.postorder()
        print()
        print("inorder TRaversal:")
        bst.inorder()
        print()