class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class Binary_search_tree:
    def __init__(self):
        self.root=None

    #FIRST WAY INSERT
    # def insert(self,value):
    #     if self.root==None:
    #         self.root=node(value)
    #     else:
    #         self._insert(value,self.root)
    #
    # def _insert(self,value,cur_node):
    #     if value<cur_node.value:
    #         if cur_node.left_child==None:
    #             cur_node.left_child=node(value)
    #         else:
    #             self._insert(value,cur_node.left_child)
    #     elif value>cur_node.value:
    #         if cur_node.right_child==None:
    #             cur_node.right_child=node(value)
    #         else:
    #             self._insert(value,cur_node.right_child)
    #     else:
    #         print("Value already in tree !!")

    # SECOND WAY INSERT
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.value:
                    if current.left_child:
                        current = current.left_child
                    else:
                        current.left_child = Node(val)
                        break
                elif val > current.value:
                    if current.right_child:
                        current = current.right_child
                    else:
                        current.right_child = Node(val)
                        break
                else:
                    break

    # FIRST WAY PRINT
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    #FIRST WAY HEIGHT
    def height(self):
        if self.root!=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node==None: return cur_height
        left_height=self._height(cur_node.left_child,cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height,right_height)

    # FIRST WAY SEACRH
    def search(self,value):
        if self.root!=None:
            return self._search(value,self.root)
        else:
            return False

    def _search(self,value,cur_node):
        if value==cur_node.value:
            return True
        elif value<cur_node.value and cur_node.left_child!=None:
            return self._search(value,cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child!=None:
            return self._search(value, cur_node.right_child)
        return False

def fill_tree(tree,num_elems=100,max_int=1000):
    from random import randint
    for i in range(num_elems):
        cur_elem=randint(0,max_int)
        tree.insert(cur_elem)
    return tree

tree = Binary_search_tree()
#FIRST WAY INSERT FROM RANDOM DATA
# tree = fill_tree(tree)

#SECOND WAY INSERT FROM MANUAL DATA
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)


#SECOND WAY PRINT
def print2(root):
    if root != None:
        print2(root.left_child)
        print(str(root.value))
        print2(root.right_child)

# print(print2(tree.root))
tree.print_tree()

# SECOND WAY HEIGHT
def height2(root):
    if root != None:
        return 1 + max(height2(root.left_child), height2(root.right_child))
    else:
        return -1
print("Tree height 1 => ",str(tree.height()))
print("Tree height 2 => ",str(height2(tree.root)))

#SECOND WAY SEACRH
def search2(root,value):
    if value == root.value:
        return True

    elif value < root.value and root.left_child!=None :
        return search2(root.left_child, value)
    elif value > root.value and root.right_child!=None :
        return search2(root.right_child, value)
    return False


print(tree.search(10))
print(tree.search(30))
print("SEARCH ",search2(tree.root,40))
