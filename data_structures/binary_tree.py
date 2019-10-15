
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, new_value):
        self.value = new_value

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

    def get_value(self):
        return self.value

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left
    
    def balanced(self)
        return self.left and self.right

class BinaryTree:
    def __init__(self, root_node=None):
        self.root_node = root_node
    
    def set_root(self, new_root):
        self.root_node = new_root

    def add_node(self, item):
        new_node= TreeNode(item)
    
        if self.root_node == None:
            self.root_node = new_node
        else:
            self._add_node_recursive(self.root_node, new_node)

    def _check_tree_balance(self, node)
        if node == None:
            return False
        if not node.left and not node.right:
            return True
        elif _check_tree_balance(node.get_left()) and _check_tree_balance(node.get_right)    
#### NOT DONE HERE.  Need to address to go right.

    def _add_node_recursive(self, current, to_add)
        if current.balanced():
            if current.get_left().balanced() and current.get_right().balanced()
                
                return _add_node_recursive(current.get_left(), to_add)
            elif current.get_left().balanced and not current.get_right().balanced():
                return _add_node_recursive(current.get_right(), to_add)
            else:
                return _add_node_recursive(current.get_left(), to_add)    
        else:
            if current.left == None and current.right == None:
                current.set_left(to_add)
            elif current.left and not current.right:
                current.set_right(to_add)
            else:
                return _add_node_recursive(current.get_left(), to_add)
            