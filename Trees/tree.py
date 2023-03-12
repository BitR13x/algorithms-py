class Node():

    def __repr__(self) -> str:
        left = f"Node({self.left.data})" if self.left else "None"
        right = f"Node({self.right.data})" if self.right else "None"
        return f"Node(data={self.data}, left={left}, right={right})"

    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class Tree:

    def PrintTree(self, root=None):
        if root:
            self.PrintTree(root.right)
            print(root.data, end=" ")
            self.PrintTree(root.left)

    def levelOrder(self, root):
        queue = [root] if root else []
        while queue:
            m = queue.pop()
            print(m.data, end=" ")
            if m.left:
                queue.insert(0, m.left)
            if m.right:
                queue.insert(0, m.right)

    def insert(self, root, data):
        if root:
            if root.data > data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        else:
            return Node(data)
        return root


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)

print(root)