# regexGenerator
## Overview
This python script generates a regular expression that can be used to match words from a word list.  An online demo can be found on [my repl.it page](https://repl.it/@jkoppp/RegExGenerator).  This demo is not as actively maintained and may not match this repo exactly.
## Installation
This program requires Python3 to run.  It can also be run online using [repl.it](repl.it.com).

Note: For the prettyPrintTree method of the node class to work, graphviz must be installed on the system.  As of right now, this is not working on repl.it.  The script can generate a .gv file that can then be rendered using another tool but if graphviz can be installed on the machine the script runs on it should be able to render straight to .png or a similar format.

## Full Description
### Purpose
This script was origionally created to help with [reddit](reddit.com) automoderator configuration.  The automoderator can check posts for certain key words by using a regular expression.  This script can convert a text file of key words to a regular expression that matches any of the keywords.
### Main
The program uses the Node class to generate a tree type data structure.  This tree contains one character per leaf and each path down the tree represents a valid word.  This type of data structure allows a regular expression to be generated recursively and allows common groups of letters to be shared so they do not need to be repeated.

Example: A regular expresion that is looking for 'New York', 'New Jersey', or 'New Mexico' can check for 'New ' and then if that is found check for the three possible endings.  The shared characters at the begining do not need to be repeated.

However, a tree with only one character per leaf would be very large.  This program collapse the tree so that characters that only ever appear together and in the same order can be combined into one leaf.  This can be demonstrated by using the example from above.

Example: The raw tree for an input file containing 'New York', 'New Jersey', and 'New Mexico' creates one leaf for each character and looks like this.

![](https://i.imgur.com/HnPMnz5.png)

This is very inefficient because most of those leafs are not nodes are not needed separate.  In this file, a 'N' will never be found that isn't followed by an 'E'.  So these two nodes can be combined into one 'NE' node.  The program accounts for this and optimizes the original tree.  This optimization uses recursion to combine nodes that are only ever found together.  The optimized tree is much smaller and can be seen below.

![](https://i.imgur.com/Su7fTPC.png)

The regular expression is then generated from this optimized tree.

Example:  The regular expression for this example looks like this.
''''
((NEW ((JERSEY)|(MEXICO)|(YORK))))
''''
You can see how the common characters are grouped together and the shared characters are only included once.

### Node Class
Coming Soon...



