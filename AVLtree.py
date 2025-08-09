class AVLtree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def Height(self, curr):
        return curr.height if curr else 0

    def get_balance(self, curr):
        return self.Height(curr.left) - self.Height(curr.right) if curr else 0

    def rightRotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.Height(y.left), self.Height(y.right))
        x.height = 1 + max(self.Height(x.left), self.Height(x.right))

        return x

    def leftRotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.Height(x.left), self.Height(x.right))
        y.height = 1 + max(self.Height(y.left), self.Height(y.right))

        return y

    def insert(self, node, value):
       
        if not node:
            return self.Node(value)
        elif value < node.data:
            node.left = self.insert(node.left, value)
        elif value > node.data:
            node.right = self.insert(node.right, value)
        else:
            return node  

       
        node.height = 1 + max(self.Height(node.left), self.Height(node.right))

      
        balance = self.get_balance(node)

       
        if balance > 1 and value < node.left.data:
            return self.rightRotate(node)
        
        if balance < -1 and value > node.right.data:
            return self.leftRotate(node)
        
        if balance > 1 and value > node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        
        if balance < -1 and value < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def add(self, value):
        self.root = self.insert(self.root, value)

    def preOrderTraversal(self, curr):
        if curr:
            print(curr.data, end=" ")
            self.preOrderTraversal(curr.left)
            self.preOrderTraversal(curr.right)

    def Traversal(self):
        self.preOrderTraversal(self.root)
        print()


def Main():
    tree = AVLtree()
    for val in [30, 10 , 20]:
        tree.add(val)
    tree.Traversal()

Main()
