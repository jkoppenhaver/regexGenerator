class Node:
  
  def __init__(self, letter=None, par=None, end=False):
    self.parent = par
    self.data = letter
    self.validEnd = end
    self.child = []
  
  def addChild(self, data):
    self.child.append(Node(data, self))
    
  def getChildByData(self, d):
    for i in self.child:
      if i.data == d:
        return i
    return None
  
  def printTree(self, indent=""):
    if(self.data == None):
      if(self.validEnd):
        print(indent+'+'+"None")
      else:
        print(indent+'-'+"None")
      
    else:
      if(self.validEnd):
        print(indent+'|-+'+self.data)
      else:
        print(indent+'|--'+self.data)
    for chi in self.child:
      chi.printTree(indent+"   ")
  