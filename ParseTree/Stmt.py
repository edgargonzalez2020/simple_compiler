# Gonzalez, Edgar.
# exg6686
# 2019-03-04
import sys
from .common import *
#---------#---------#---------#---------#---------#--------#
class Stmt() :
    def __init__( self, lineNum, stmt ) :
        self.m_NodeType = 'Stmt'
        self.m_LineNum = lineNum
        self.m_Stmt = stmt
    def dump( self, indent = 0, fp = sys.stdout ) :
        self.m_Stmt.dump( indent + 1, fp = fp )

#---------#---------#---------#---------#---------#--------#