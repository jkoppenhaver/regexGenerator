from graphviz import Graph
class Node:
  ########################################################
  # __init__
  # Description: Creates a new node
  # Parameters:
  #		letter (Optional)- String that holds the node data
  #		par (Optional)- This node's parent
  #		end (Optional) - Boolean that stores whether or not
  #						 this node is a valid end to a word
  # Returns: Nothing
  #########################################################
  def __init__(self, letter=None, par=None, end=False):
    self.parent = par
    self.data = letter
    self.validEnd = end
    self.child = []
    return
  
  ########################################################
  # addChild
  # Description: Creates and adds a new child node
  # Parameters:
  #		data - String that holds the childs data
  # Returns: Nothing
  #########################################################
  def addChild(self, data):
    self.child.append(Node(data, self))
    return
  
  ########################################################
  # getChildByData
  # Description: Searches for and returns a child that
  #				 matches the data.
  # Parameters:
  #		d - String to search for
  # Returns: Child with matching data or None if no child
  #			 is found
  #########################################################
  def getChildByData(self, d):
    for i in self.child:
      if i.data == d:
        return i
    return None
  
  ########################################################
  # collapseTree
  # Description: Recursive meathod that reduces the trees
  #				 size by combining elements that do not
  #				 occur in the word list separately
  # Parameters: None
  # Returns: None
  #########################################################
    def collapseTree(self):
    while((len(self.child) == 1) and not(self.validEnd) and (self.data != None)):
      self.data += self.child[0].data
      self.validEnd = self.child[0].validEnd
      self.child = self.child[0].child
    for child in self.child:
      child.collapseTree()
    return
  
  ########################################################
  # generateRegEx
  # Description: Creates a regular expression string that
  #				 matches all words found in the list.
  # Parameters:
  #		regEx (Private)- This paramater is only used for
  #						 recurrsion.  Do not pass a
  #						 parameter when calling this function
  # Returns: A regular expression as a string
  #########################################################
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
  
  ########################################################
  # printTree
  # Description: Creates a text based representation of the
  #				 tree.
  # Parameters:
  #		string (Private) - This paramater is only used for
  #						   recurrsion.  Do not pass a
  #						   parameter when calling this
  #						   function
  #		indent (Private) - This paramater is only used for
  #						   recurrsion.  Do not pass a
  #						   parameter when calling this
  #						   function
  # Returns: Text represntaion of the tree as a string
  #########################################################
  def printTree(self, string="", indent=""):
    if(self.data == None):
      if(self.validEnd):
        string += indent+'+'+"None"
      else:
        string += indent+'-'+"None"
    else:
      if(self.validEnd):
        string += indent+'|-+'+self.data
      else:
        string += indent+'|--'+self.data
    string += "\n"
    for chi in self.child:
      string = chi.printTree(string, indent+"   ")
    return string
  
  ########################################################
  # __str__
  # Description: This function ensures if you use the
  #				 print() function a string representation
  #				 is given
  # Parameters: None
  # Returns: Text represntaion of the tree as a string
  #########################################################
  def __str__(self):
    return self.printTree()
  
  ########################################################
  # prettyPrintTree
  # Description: This function ensures uses graphviz to
  #				 create a graphical representation of the
  #				 tree.  This method requires graphviz to
  #				 be installed on the machine or else the
  #				 graphic will have to be generated separately
  # Parameters:
  #				graph - A graphviz graph object
  #				parent_index (Private) - This paramater is
  #										 only used for
  #										 recurrsion.  Do
  #										 not pass a
  #										 parameter when
  #										 calling this
  #										 function
  #				current_index (Private) - This paramater is
  #										 only used for
  #										 recurrsion.  Do
  #										 not pass a
  #										 parameter when
  #										 calling this
  #										 function
  # Returns: A graphviz Graph object
  #########################################################
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
  