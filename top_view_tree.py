class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#FISRT WAY==============================================
# def _top_view(root, m, hd,level):
#     if not root:
#         return
#     if hd in m:
#         if level < m[hd][1]:
#             m.update( {hd : [root.data,level] })
#     else:
#         m[hd] = [root.data,level]
#
#     _top_view(root.left, m, hd-1,level+1)
#     _top_view(root.right,m, hd+1, level+1)
#
# def top_view(root):
#     m={}
#     _top_view(root, m, 0,0)
#     print(m.items())
#     for key,value in m.items():
#         print (value[0]),
#=============================================================

#SECOND WAY====================================================
# def printLeft(root):
#     if root.left is not None:
#         printLeft(root.left)
#     print(root.data),
#
#
# def printRight(root):
#     print(root.data),
#     if root.right is not None:
#         printRight(root.right)
#
#
# def top_view(root):
#     printLeft(root)
#     printRight(root.right)
#==================================================================

#THIRD WAY===================================================
def top_view(root,count=0):
    if root != None:
        if count <=0:
            print(top_view(root.left, -1))
        print(root.data)
        if count >= 0:
            print(top_view(root.right, 1))

#=============================================================


# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.right = Node(4)
# root.left.right.right = Node(5)
# root.left.right.right.right = Node(6)
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)

root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
top_view(root)