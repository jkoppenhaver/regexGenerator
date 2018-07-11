from graphviz import Graph
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
  
    def collapseTree(self):
    while((len(self.child) == 1) and not(self.validEnd) and (self.data != None)):
      self.data += self.child[0].data
      self.validEnd = self.child[0].validEnd
      self.child = self.child[0].child
    for child in self.child:
      child.collapseTree()
    return

  def generateRegEx(self, regEx=""):
    if(self.data != None):
      regEx += '('
      regEx += self.data
    if(len(self.child) > 1):
      regEx += '('
    for c in self.child:
      regEx = c.generateRegEx(regEx)
    if(len(self.child) > 1):
      regEx += ')'
      if(self.validEnd):
        regEx += '?'
    if(self.data != None):
      if(self != self.parent.child[-1]):
        #Not Last Child
        regEx += ")|"
      else:
        if(len(self.parent.child) > 1):
          #Last And Not Only Child
          regEx += ')'
        elif(self.parent.validEnd):
          #Only Child And Parent is End
          regEx += ")?"
        else:
          #Only Child and Parent is not End
          regEx += ')'
    return regEx
  
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
    
    def prettyPrintTree(self, graph, parent_index=None,  current_index=0):
    if(self.data == None):
      label = "HEAD"
    else:
      label = self.data
    if(self.validEnd):
      graph.node(str(current_index), label, shape="square")
    else:
      graph.node(str(current_index), label, shape="circle")
    if(parent_index != None):
      graph.edge(str(parent_index), str(current_index))
    index = current_index+1
    for chi in self.child:
      index = chi.prettyPrintTree(graph, current_index, index)
    return index
  