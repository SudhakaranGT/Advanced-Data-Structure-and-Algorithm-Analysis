class node():
    def __init__(self,value=None,left=None,right=None,parent=None):
        self.value=value
        self.left=left
        self.right=right
        self.parent=parent
    
class splay:
    def __init__(self):
        self.root=None
    def leftrotate(self,root):
        y=root.right
        z=y.left
        root.right=z
        if z is not None:
            z.parent=root
        y.parent=root.parent
        if root.parent==None:
            self.root=y
        elif root.parent.left==root:
            root.parent.left=y
        elif root.parent.right==root:
            root.parent.right=y
        y.left=root
        root.parent=y
    def rightrotate(self,root):
        y=root.left
        z=y.right
        root.left=z
        if z is not None:
            z.parent=root
        y.parent=root.parent
        if root.parent==None:
            self.root=y
        elif root.parent.left==root:
            root.parent.left=y
        elif root.parent.right==root:
            root.parent.right=y
        y.right=root
        root.parent=y
    def insert(self,value,p=None):
        if p is None:
            p=self.root
        if self.root is None:
            n=node(value)
            self.root=n
        elif p.value<value:
            if not p.right:
                n=node(value)
                n.parent=p
                p.right=n
                self.splay(n)
                return
            else:
                self.insert(value,p.right)
        elif p.value>value:
            if not p.left:
                n=node(value)
                n.parent=p
                p.left=n
                self.splay(n)
                return
            else:
                self.insert(value,p.left)
    def splay(self,root):
        while root.parent!=None:
            if root.parent.parent==None:
                if root.parent.left==root:
                    self.rightrotate(root.parent)
                elif root.parent.right==root:
                    self.leftrotate(root.parent)
            else:
                g=root.parent.parent
                p=root.parent
                if g.left==p and p.left==root:
                    self.rightrotate(g)
                    self.rightrotate(p)
                elif g.right==p and p.right==root:
                    self.leftrotate(g)
                    self.leftrotate(p)
                elif g.left==p and p.right==root:
                    self.leftrotate(p)
                    self.rightrotate(g)
                elif g.right==p and p.left==root:
                    self.rightrotate(p)
                    self.leftrotate(g)
    def search(self,value,p=None):
        if p is None:
            p=self.root
        if p.value==value:
            self.splay(p)
            return
        elif p.value!=value and p.left is None and p.right is None:
            print(value," Not found")
            print("-----------")
            self.splay(p)
            return
        elif p.value>value:
            self.search(value,p.left)
        elif p.value<value:
            self.search(value,p.right)
    def preorder(self,root):
        if root is not None:
            print(root.value,end =" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root is not None:
            self.preorder(root.left)
            print(root.value,end = " ")
            self.preorder(root.right)

    def postorder(self,root):
        if root is not None:
            self.preorder(root.left)
            self.preorder(root.right)
            print(root.value,end = " " )



    def split(self,root):
        tempr=None
        templ=None
        if root.left:
            templ=root.left
            root.left.parent=None
            root.left=None
        if root.right:
            tempr=root.right
            root.right.parent=None
            root.right=None
        self.join(templ,tempr)
    
    def join(self,left,right):
        if left:
            maxleft=self.maximum(left)
            self.splay(maxleft)
            if right is not None:
                maxleft.right=right
                right.parent=maxleft
            self.root=maxleft
        else:
            self.root=right
    def maximum(self,root):
        while root.right is not None:
            root=root.right
        return root
    def delete(self,value,p=None):
        if p is None:
            p=self.root
        if p is None:
            return
        if p.value==value:
            self.splay(p)
            self.split(p)
            return
        elif value<p.value:
            if not p.left:
                print("data not found")
                self.splay(p)
                return
            self.delete(value,p.left)
        elif value>p.value:
            if not p.right:
                print("data not found")
                self.splay(p)
                return
            self.delete(value,p.right)



SplayTree = splay()
while True:
    print("Choices:\n 1.insert \n 2.delete \n 3.search \n 4.Traversal")

    op = input("Enter:")

    if op.lower() == 'insert':
        n = int(input("Enter the no. of nodes:"))
        for i in range(n):
            SplayTree.insert(int(input("\nEnter the value:")))
            SplayTree.preorder(SplayTree.root)
        print("Done!")

    if op.lower() == 'delete':
        SplayTree.delete(int(input("Enter the value:")))
        SplayTree.preorder(SplayTree.root)
        print("Done!")

    if op.lower() == 'search':
        SplayTree.search(int(input("\nEnter the value: ")))

    if op.lower() == 'traversal':
        print("preorder traversal:")
        SplayTree.preorder(SplayTree.root)
        print()
        print("Postorder Traversal:")
        SplayTree.postorder(SplayTree.root)
        print()
        print("inorder TRaversal:")
        SplayTree.inorder(SplayTree.root)
    
        print()