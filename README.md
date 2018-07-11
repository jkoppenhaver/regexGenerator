# regexGenerator
## Overview
This python script generates a regular expression that can be used to match words from a word list.  An online demo can be found on [my repl.it page](https://repl.it/@jkoppp/RegExGenerator).  This demo is not as actively maintained and may not match this repo exactly.
## Installation
This program requires Python3 to run.  It can also be run online using [repl.it](repl.it.com).

Note: For the prettyPrintTree method of the node class to work, graphviz must be installed on the system.  As of right now, this is not working on repl.it.  The script can generate a .gv file that can then be rendered using another tool but if graphviz can be installed on the machine the script runs on it should be able to render straight to .png or a similar format.

## Full Description
### Purpose
This script was origionally created to help with reddit automoderator configuration.  The automoderator can check posts for certain key words by using a regular expression.  This script can convert a text file of key words to a regular expression that matches any of the keywords.
### Main
The program uses the Node class to generate a tree type data structure.  This tree contains one character per leaf and each path down the tree represents a valid word.  This type of data structure allows a regular expression to be generated recursively and allows common groups of letters to be shared so they do not need to be repeated.

Example: A regular expresion that is looking for 'New York', 'New Jersey', or 'New Mexico' can check for 'New ' and then if that is found check for the three possible endings.  The shared characters at the begining do not need to be repeated.  The raw tree for this example would look like this.

![](https://i.imgur.com/HnPMnz5.png)

This is very inefficient because most of those leafs are not nodes are not needed separately.  In this file, a 'N' will never be found that isn't followed by an 'E'.  So these two nodes can be combined into one 'NE' node.  The program accounts for this and optimizes the original tree.  This optimization uses recursion to combine nodes that are only ever found together.  The optimized tree is much smaller and can be seen below.  More information about this optimization can be found in the [Tree Optimization](#tree-optimization) section.

![](https://i.imgur.com/Su7fTPC.png)

The regular expression is then generated from this optimized tree.

Example:  The regular expression for this example looks like this.
````
((NEW ((JERSEY)|(MEXICO)|(YORK))))
````
You can see how the common characters are grouped together and the shared characters are only included once.

### Node Class
This class provides functions to build and access the tree type data structure used in this project.  Nodes can be created with 0-1 parent node and unlimited children nodes.  The HEAD of the tree should be the only node with no parent.  Child nodes can be accessed directly by fetching the child array from the node or you can search for a child by the data it contains.  For this project, the data is always strings.
#### Visualizing the tree
There is a print method that returns a visual representation of the tree.  The default string method prints a text based representation of the tree.  Each node is printed with indentation to show what level the node is on.  Each node is also represented by a + or - to note whether the node is the end of a word in the list or not.  A + represents a valid end to a word.  A more advanced print method is also included.  The pretty print method uses graphviz to create a graphical representation of the tree.  This method uses square nodes to represent valid word ends and circles for other nodes.  However, this method is still under development and should be used with caution.  The images used in this file were generated using the pretty print method but had to be rendered separately.  The two print methods are shown below for the same tree.

![](https://i.imgur.com/9MIMtkZ.png)
![](https://i.imgur.com/w9cINfF.png)

#### Tree Optimization
The optimization of the tree is done in the colapse tree function.  This function moves through the tree recursively and checks each node.  If a node matches three criteria it can be combined with it's child.
+ The node must have only one child
+ The node must not be the end of a word in the input list
+ The node must not be the HEAD.  The HEAD of the tree can not be collasped.

Example: If the input list includes the words 'ABE', 'ABCD', 'F','FGH', and 'FGHI' then the raw tree that is generated looks like this.
![](https://i.imgur.com/xTATQvI.png)
The square nodes are valid ends which means that a word on the list ends at that node.  'FGH' is a valid word so that node is a valid end but 'FG' is not on the list so that node is not a valid end.  So, in this example, only two nodes meet all 3 criteria for the optimization.
+ Nodes A, F, and H can not be collapsed because they are valid ends
+ Nodes D, E, and I do not have children so they can not be combinded
+ Node B can not be collapsed because it has more than one child
+ Node C and G meet all three criterial so they can be combinded with the node below them.

This optimization results in the following tree. You can see that Nodes C and G were combined with the node below them.

![](https://i.imgur.com/w9cINfF.png)

