# Gonzalez, Edgar.
# exg6686
# 2019-03-04
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Identifier() :
  def __init__( self, lineNum, identifier ) :
    self.m_NodeType = 'Identifier'

    self.m_LineNum  = lineNum
    self.m_ID       = identifier

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    dumpHeaderLine( indent, self.m_LineNum,
      f'IDENTIFIER {self.m_ID!r}', fp )
  def get_id(self):
    return self.m_ID

#---------#---------#---------#---------#---------#--------#
