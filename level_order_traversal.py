class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def LevelOrderTraversal(root):
    this_level = [root]
    while this_level:
        next_level = []
        for i in this_level:
            print(i.data),
            if i.left: next_level.append(i.left)
            if i.right: next_level.append(i.right)

        this_level = next_level

root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
LevelOrderTraversal(root)
