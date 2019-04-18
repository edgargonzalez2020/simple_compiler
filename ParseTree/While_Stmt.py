# Gonzalez, Edgar.
# exg6686
# 2019-03-04
import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class While_Stmt() :
    def __init__( self, lineNum, expression, blockStmt ) :
        self.m_LineNum = lineNum
        self.m_Expression = expression
        self.m_BlockStmt = blockStmt
    def dump( self, indent = 0, fp = sys.stdout ) :
        dumpHeaderLine( indent , self.m_LineNum,
                        'STATEMENT (WHILE)', fp = fp )
        self.m_Expression.dump( indent + 1 , fp = fp )
        self.m_BlockStmt.dump( indent + 1, fp = fp )
#---------#---------#---------#---------#---------#--------#