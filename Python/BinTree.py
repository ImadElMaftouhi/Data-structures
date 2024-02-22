###
# Defining a library to handle Binary trees in python
import tkinter as tk

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
    
    def _get_tree_height(self, node):
        if not node:
            return 0
        return max(self._get_tree_height(node.left), self._get_tree_height(node.right)) + 1

    def visualize_tree(self):
        tree_height = self._get_tree_height(self.root)
        node_width = 50
        node_height = 30
        canvas_width = 2 ** (tree_height - 1) * node_width
        canvas_height = tree_height * node_height

        root = tk.Tk()
        root.title("Binary Tree Visualization")
        root.geometry("800x600+0+0")
        
        canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)
        canvas.pack()

        self._visualize_tree_recursive(canvas, self.root, 0, 0, canvas_width, node_width)

        root.mainloop()

    def _visualize_tree_recursive(self, canvas, node, x, y, width, node_width):
        if node:
            canvas.create_oval(x, y, x + node_width, y + node_width, fill="white")
            canvas.create_text(x + node_width / 2, y + node_width / 2, text=str(node.data))

            if node.left:
                x_left = x - width / 4
                y_left = y + 2 * node_width
                canvas.create_line(x + node_width / 2, y + node_width, x_left + node_width / 2, y_left, arrow=tk.LAST)
                self._visualize_tree_recursive(canvas, node.left, x_left, y_left, width / 2, node_width)

            if node.right:
                x_right = x + width / 4
                y_right = y + 2 * node_width
                canvas.create_line(x + node_width / 2, y + node_width, x_right + node_width / 2, y_right, arrow=tk.LAST)
                self._visualize_tree_recursive(canvas, node.right, x_right, y_right, width / 2, node_width)



