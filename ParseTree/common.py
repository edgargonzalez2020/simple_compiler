# Gonzalez, Edgar.
# exg6686   
# 2019-03-04
#---------#---------#---------#---------#---------#--------#
INDENT_STR = '  '

#---------#---------#---------#---------#---------#--------#
def dumpHeaderLine( indent, lineNum, contents, fp ) :
  print( f'({lineNum:4d}) '+(INDENT_STR*indent)+contents, file = fp )

#---------#---------#---------#---------#---------#--------#
