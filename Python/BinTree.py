###
# Defining a library to handle Binary trees in python


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left:
                self._insert_recursive(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert_recursive(node.right, data)
            else:
                node.right = TreeNode(data)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if not node:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.data)
            self._inorder_traversal_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result

    def _preorder_traversal_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_traversal_recursive(node.left, result)
            self._preorder_traversal_recursive(node.right, result)


    def postorder_traversal(self):
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result

    def _postorder_traversal_recursive(self, node, result):
        if node:
            self._postorder_traversal_recursive(node.left, result)
            self._postorder_traversal_recursive(node.right, result)
            result.append(node.data)

    def levelorder_traversal(self):
        result = []
        queue = []
        if self.root:
            queue.append(self.root)
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
    
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if not node:
            return 0
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1
    
    def is_empty(self):
        return self.root is None

    def size(self):
        return self._size_recursive(self.root)

    def _size_recursive(self, node):
        if not node:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)


