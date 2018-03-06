class TreeNode:

    def __init__(self, key, val, left=None, right = None, parent=None, balance=0):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = balance

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChild(self):
        return self.leftChild or self.rightChild

    def hasBothChild(self):
        return  self.leftChild and self.rightChild

    def replaceNodeDate(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.rightChild():
            self.rightChild.parent = self

class BinarySearchTree(TreeNode):
    def __init__(self):
        self.root = None
        self.size = 0
    def length(self):
        return  self.size
    def __len__(self):
        return self.size

    def inorder(self,node):
        if node.leftChild:
            self.inorder(node.leftChild)
        print(self.print_node(node))
        if node.rightChild:
            self.inorder(node.rightChild)

    def levelorder(self,node): # 广度优先遍历
        nodes = []
        nodes.append(node)
        while len(nodes)>0:
            current_node = nodes.pop(0)
            print(self.print_node(current_node))
            if current_node.leftChild:
                nodes.append(current_node.leftChild)
            if current_node.rightChild:
                nodes.append(current_node.rightChild)

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)


    def __setitem__(self, key, value):
        self.put(key,value)

    def get(self,key,onlyValue=False,forTree= False):                                      #查找具有给定关键字的结点
        if self.root:
            res = self._get(key,self.root)
            if forTree:
                return res
            if res:
                if onlyValue:
                    return self.print_node(res)[1]
                return self.print_node(res)
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        """
        迭代版本

        while currentNode and key != currentNode.key:
            if currentNode.key < key:
                currentNode = currentNode.rightChild
            else:
                currentNode = currentNode.leftChild

        return currentNode
         """

        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key < key:
            return self._get(key,currentNode.rightChild)
        else:
            return self._get(key,currentNode.leftChild)
    def minimum(self,node,forTree=False):
        while node.leftChild:
            node = node.leftChild
        if forTree:
            return node
        return self.print_node(node)
    def maximum(self,node):
        while node.rightChild:
            node = node.rightChild
        return self.print_node(node)
    def __getitem__(self, item):
        return self.get(item)
    def __contains__(self, item):
        if self._get(item,self.root):
            return True
        else:
            return False
    def delete(self,key):
        if self.size>1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise  KeyError("Error, key not in tree")

    def __delitem__(self, key):
        self.delete(key)



    def print_node(self,node):
        if node.parent:
            return [node.key,node.payload,node.parent.key]
        else:
            return [node.key,node.payload]

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChild():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.minimum(self.rightChild,forTree=True)
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ


    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


class AVLTree(BinarySearchTree):

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)
    """
    迭代版本
    """
    # def _put(self,key,val,currentNode):    #这里树不为空
    #     while currentNode:
    #         tmpCurrrentNode = currentNode
    #         if key < currentNode.key:
    #             currentNode = currentNode.leftChild
    #         else:
    #             currentNode = currentNode.rightChild
    #     z = TreeNode(key,val,parent=tmpCurrrentNode)
    #     if z.key < tmpCurrrentNode.key:
    #         tmpCurrrentNode.leftChild = z
    #     else:
    #         tmpCurrrentNode.rightChild = z
    #     self.updateBalance(z)


    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)



    def rotateLeft(self,rotRoot): #rotate left
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)        #参考wiki
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot): #rotate right
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild # deal child
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot #deal child parent
        newRoot.parent = rotRoot.parent #deal root parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot #deal new root right child
        rotRoot.parent = newRoot #deal old root parent
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)






print('test avl')
mytree = AVLTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
mytree[5]='dog'
mytree[1]='cat'
mytree.levelorder(mytree.root)



















# print('test bst')
#
# mytree = BinarySearchTree()
#
# mytree[3]="red"
# mytree[4]="blue"
# mytree[6]="yellow"
# mytree[2]="at"
# mytree[5]='dog'
# mytree[1]='cat'
# print(mytree.minimum(mytree.root))
# print(mytree.print_node(mytree.root))
# print(mytree.maximum(mytree.root))



