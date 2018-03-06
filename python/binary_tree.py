"""
list 实现二叉树
"""
# def binary_tree(root):
#     return [root,[],[]]
# def insert_left(root,new_branch):
#     t = root.pop(1)
#     if len(t) > 1:
#         root.insert(1,[new_branch,t,[]])
#     else:
#         root.insert(1,[new_branch,[],[]])
#     return root
# def insert_right(root,new_branch):
#     t = root.pop(2)
#     if len(t) > 1:
#         root.insert(2,[new_branch,[],t])
#     else:
#         root.insert(2,[new_branch,[],[]])
#     return root
#
# def get_root_val(root):
#     return root[0]
# def set_root_val(root,new_val):
#     root[0] = new_val
# def get_left_child(root):
#     return root[1]
# def get_right_child(root):
#     return root[2]
#
# r = binary_tree(3)
# insert_left(r, 4)
# insert_left(r, 5)
# insert_right(r, 6)
# insert_right(r, 7)
# print(r)
# l = get_left_child(r)
# print(l)
# set_root_val(l, 9)
# print(r)
# insert_left(l, 11)
# print(r)
# print(get_right_child(get_right_child(r)))
"""
类定义二叉树
"""
class binary_tree:
    def __init__(self,root):
        self.root = root
        self.left_child = None
        self.right_child = None
    def insert_left(self,new_node):
        if self.left_child is None:
            self.left_child = binary_tree(new_node)
        else:
            t = binary_tree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = binary_tree(new_node)
        else:
            t = binary_tree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child
    def get_right_child(self):
        return self.right_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root

r = binary_tree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())

