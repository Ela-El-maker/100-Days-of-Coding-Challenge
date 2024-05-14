class Node(object):
  def __init__(self, val):
    self.lchild = None
    self.rchild = None

class BinarySearchTree(object):
  def insert(self, root, node):

    if root is None:
      return node


    if root.val < node.val:
      root.rchild = self.insert(root.rchild,node)
    else:
      root.lchild = self.insert(root.lchild,node)
    return root

  def inOrderPlace(self,root):
    if not root:
      return None
    else:
      self.inOrderPlace(root,lchild)
      print root.val
      self.inOrderPlace(root,rchild)


  def preOrderPlace(self,root):
    if not root:
      return None
    else:
      print(root.val)
      self.preOrderPlace(root,lchild)
      self.preOrderPlace(root,rchild)

  def postOrderPlace(self,root):
    if not root:
      return None
    else:
      self.postOrderPlace(root,lchild)
      self.postOrderPlace(root,rchild)
      print(root.val)



"""Create different node and insert data into it"""

r = Node(3)
node = BinarySearchTree()
nodeList = [1,22,3,44,5,66,7,88,9]

for nd in nodeList:
  node.insert(r,Node(nd))



print("-------In order------")
print(node.inOrderPlace(r))
print("-------Pre order------")
print(node.preOrderPlace(r))
print("-------Post order------")
print(node.postOrderPlace(r))

    