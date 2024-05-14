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


  
    