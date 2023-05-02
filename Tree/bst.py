class BSTNode:
    # creating constructor for class BSTNOde
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree:
    # creating constructor for class BinarySearchTree
    def __init__(self):
        self._root = None
        self._size = 0

    def size(self):
        # returns the size of tree
        return self._size

    # function to insert node in a tree
    def add(self, key, value):
        node = BSTNode(key, value)
        temp = self._root
        prev = None

        # determines the node to which new node is to be inserted
        while temp != None:
            prev = temp
            if key <= temp.key:
                temp = temp.left
            else:
                temp = temp.right
        # if root node is empty i.e no node in a tree
        if prev == None:
            self._root = node
        elif key < prev.key:
            prev.left = node
        else:
            prev.right = node
        node.parent = prev
        self._size += 1

    # fucntion to search in a tree
    def search(self, key):
        temp = self._root

        # search for required key in a tree
        while temp != None:
            if key < temp.key:
                temp = temp.left
            elif key > temp.key:
                temp = temp.right
            else:
                break
        if temp == None:
            return False
        else:
            return temp.value

    # fucntion to find the smallest key value pair in tree by moving towards left of the tree

    def smallest(self):
        temp = self._root
        # finds the smallest key in tree
        try:
            while temp.left != None:
                temp = temp.left
            return (temp.key, temp.value)
        except:
            return None

    # fucntion to fins the largest key value pair in tree by moving towards right of the tree
    def largest(self):
        temp = self._root
        try:
            while temp.right != None:
                temp = temp.right
            return (temp.key, temp.value)
        except:
            return None

    # function to remove the key value pair in a tree
    def remove(self, key):
        # searches whether the key is present in tree or not
        if self.search(key) == False:
            return False
        temp = self._root

        # finds the required key value node in a tree to be deleted
        while temp.key != key:
            if key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        # deletion of a tree with no child
        if temp.left == None and temp.right == None:
            try:
                if temp.parent.left == temp:
                    temp.parent.left = None
                    temp = None
                else:
                    temp.parent.right = None
                    temp = None
                self._size -= 1
                return
            except:
                temp = None
                self._root = None
                self._size -= 1
                return
        # deletion of a node with only a left child
        if temp.left != None and temp.right == None:
            try:
                temp.left.parent = temp.parent
                temp.parent.left = temp.left
                temp = None
                self._size -= 1
                return
            except:
                self._root = temp.left
                temp = None
                self._size -= 1
                return
        # deletion if a node with only a right child
        if temp.left == None and temp.right != None:
            try:
                temp.right.parent = temp.parent
                temp.parent.right = temp.right
                temp = None
                self._size -= 1
                return
            except:
                self._root = temp.right
                temp = None
                self._size -= 1
                return
        # deletion of a node with two children
        if temp.left != None and temp.right != None:
            swap = temp.left
            while swap.right != None:
                swap = swap.right
            temp.key = swap.key
            temp.value = swap.value
            if swap.left == None:
                if swap.parent.left == swap:
                    swap.parent.left = None
                else:
                    swap.parent.right = None
                swap = None
                self._size -= 1
                return
            else:
                if swap.parent.left == swap:
                    swap.parent.left = swap.left
                    swap.left.parent = swap.parent
                else:
                    swap.parent.right = swap.right
                    swap.left.right = swap.parent
                swap = None
                self._size -= 1

    # fucntion which does inorder traversal
    def inorder_walk(self):
        nodes = []
        self._inorder_walk(nodes, self._root)
        return nodes

    def _inorder_walk(self, nodes, node):
        if node == None:
            return
        self._inorder_walk(nodes, node.left)
        nodes.append(node.key)
        self._inorder_walk(nodes, node.right)

    # fucntion which does preorder traversal
    def preorder_walk(self):
        nodes = []
        self._preorder_walk(nodes, self._root)
        return nodes

    def _preorder_walk(self, nodes, node):
        if node == None:
            return
        nodes.append(node.key)
        self._preorder_walk(nodes, node.left)
        self._preorder_walk(nodes, node.right)

    # fucntion which does postorder traversal
    def postorder_walk(self):
        nodes = []
        self._postorder_walk(nodes, self._root)
        return nodes

    def _postorder_walk(self, nodes, node):
        if node == None:
            return
        self._postorder_walk(nodes, node.left)
        self._postorder_walk(nodes, node.right)
        nodes.append(node.key)
