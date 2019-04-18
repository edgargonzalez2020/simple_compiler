# Gonzalez, Edgar.
# exg6686
# 2019-04-17

import sys

from .common import *
#---------#---------#---------#---------#---------#--------#
class If_Stmt() :
    def __init__( self, lineNum, expression, blockStmt, elseOpt ) :
        self.m_NodeType = 'If_Stmt'
        self.m_LineNum = lineNum
        self.m_expression = expression
        self.m_blockStmt = blockStmt
        self.m_elseOpt = elseOpt
    def dump( self, indent = 0 , fp = sys.stdout ) :
        if_str = 'STATEMENT (IF-THEN)' if self.m_elseOpt is None else 'STATEMENT (IF-THEN-ELSE)'
        dumpHeaderLine( indent, self.m_LineNum,
                        if_str, fp = fp)
        self.m_expression.dump( indent + 1, fp = fp )
        self.m_blockStmt.dump( indent + 1, fp = fp )
        if self.m_elseOpt is not None :
            self.m_elseOpt.dump( indent + 1, fp = fp )
#---------#---------#---------#---------#---------#--------#