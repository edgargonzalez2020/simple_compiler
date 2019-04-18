# Gonzalez, Edgar.
# exg6686
# 2019-03-04
#---------#---------#---------#---------#---------#--------#
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Literal() :
  def __init__( self, lineNum, kind, value ) :
    self.m_NodeType = 'Literal'

    self.m_LineNum  = lineNum
    self.m_Kind     = kind
    self.m_Value    = value

  #---------------------------------------
  def dump( self, indent = 0, fp = sys.stdout ) :
    value = self.m_Value[1:-1] if self.m_Kind == 'string' else self.m_Value
    dumpHeaderLine( indent, self.m_LineNum,
      f'LITERAL {self.m_Kind!r} {value!r}', fp )

#---------#---------#---------#---------#---------#--------#
