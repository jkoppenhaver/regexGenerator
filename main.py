from node import Node
#Set this to True to get a full tree print out
VERBOSE= True

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
head.collapse()

if(VERBOSE):
  head.printTree()
#This generates the regEx one letter at a time.
#Should be updated to generate from the head
fullRegEx = head.generateRegEx()
print(fullRegEx)