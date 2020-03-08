class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:

  def __init__(self):
    self.root = None

  def insert(self,data):
    new_node = Node(data)
    if self.root == None:
      self.root = new_node
      return
    else:
      curr_node = self.root
      while True:
        if data < curr_node.data:
          #Left
          if curr_node.left == None:
            curr_node.left = new_node
            return 
          else:
            curr_node = curr_node.left
        elif data > curr_node.data:
            #Right
            if curr_node.right == None:
              curr_node.right = new_node
              return
            else:
              curr_node = curr_node.right

  def lookup(self,data):
    curr_node = self.root
    while True:
      if curr_node == None:
        return False
      if curr_node.data == data:
        return True
      elif data < curr_node.data:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right
    
  def print_tree(self):
    if self.root != None:
      self.printt(self.root)
#Inorder Traversal (We get sorted order of elements in tree)

  def printt(self,curr_node):
    if curr_node != None:
      self.printt(curr_node.left)
      print(str(curr_node.data))
      self.printt(curr_node.right)
      
  def remove(self,data):
    if self.root == None:
      return False
    current_node = self.root
    parent_node = None
    while True:
      if data < current_node.data:
        parent_node = current_node
        current_node = current_node.left
      elif data > current_node.data:
        parent_node = current_node
        current_node = current_node.right
      elif data == current_node.data:
        #Got a match! Start to work! 

        #Option 1: No right child:
        if current_node.right == None:
          if parent_node == None:
            self.root = current_node.left
          else:
            # parent > current value, 
            # make current left child a child of parent
            if current_node.data < parent_node.data:
              parent_node.left = current_node.left
            
            # parent < current value,
            # make left child a right child of parent
            elif current_node.data > parent_node.data:
              parent_node.right = current_node.left
        
        #Option 2: Right child which doesn't have a left child
        elif current_node.right.left == None:
          current_node.right.left = current_node.left
          if parent_node == None:
            self.root = current_node.right
          else:

            # parent > current, 
            # make right child of the left the parent
            if current_node.data < parent_node.data:
              parent_node.left = current_node.right

            # parent < current, 
            # make right child a right child of the parent
            if current_node.data > parent_node.data:
              parent_node.right = current_node.right

        # Option 3: Right child that has a left child
        else:

          # find the right child's left most child
          leftmost = current_node.right.leftmost
          leftmostparent = current_node.right
          while leftmost.left != None:
            leftmostparent = leftmost
            leftmost = leftmost.leftmost

          # parent's left subtree is now leftmost's right subtree
          leftmostparent.left = leftmost.right
          leftmost.left = current_node.left
          leftmost.right = current_node.right

          if parent_node == None:
            self.root = leftmost
          else:
            if current_node.data < parent_node.data:
              parent_node.left = leftmost
            elif current_node.data > parent_node.data:
              parent_node.right = leftmost

    return True


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()
