from node import Node
#Set this to True to get a full tree print out
VERBOSE= True

def colapseTree(node):
  while((len(node.child) == 1) and not(node.validEnd) and (node.data != None)):
    node.data += node.child[0].data
    node.validEnd = node.child[0].validEnd
    node.child = node.child[0].child
  for child in node.child:
    colapseTree(child)
  return

def generateRegEx(node, regEx=""):
  regEx += '('
  if(node.data != None):
    regEx += node.data
  if(len(node.child) > 1):
    regEx += '('
  for c in node.child:
    regEx = generateRegEx(c, regEx)
  if(len(node.child) > 1):
    regEx += ')'
    if(node.validEnd):
      regEx += '?'
  if(node != node.parent.child[-1]):
    #Not Last Child
    regEx += ")|"
  else:
    if(len(node.parent.child) > 1):
      #Last And Not Only Child
      regEx += ')'
    elif(node.parent.validEnd):
      #Only Child And Parent is End
      regEx += ")?"
    else:
      #Only Child and Parent is not End
      regEx += ')'
  return regEx

#Open the input file and read each word into a list
f = open('input.txt', 'r')
wordlist = f.read().splitlines()
f.close()
wordlist = [s.upper() for s in wordlist]
#Sort this list into alphabetical order
#This may be a waste of time...
wordlist.sort()

#Remove all commented lines
i = 0
while(i < len(wordlist)-1):
  if(wordlist[i][0] != '#'):
    break
  i += 1
#Ensure the list has some words in it
if(i > len(wordlist)-1):
  print('No elements found in list.')
  exit(0)
del wordlist[:i]

#This empty node will act as the head of the tree
head = Node()

#Add each word to the tree by creating new nodes if they do not exist
for word in wordlist:
  parent = head
  for letter in word:
    if(parent.getChildByData(letter) == None):
      parent.addChild(letter)
    parent = parent.getChildByData(letter)
  parent.validEnd = True

#Colapse the tree to get rid of extra nodes that have no possibility
#  of being reached by themself.
colapseTree(head)

if(VERBOSE):
  head.printTree()
#This generates the regEx one letter at a time.
#Should be updated to generate from the head
fullRegEx = '('
for child in head.child:
  fullRegEx += generateRegEx(child)
fullRegEx += ')'
print(fullRegEx)