# Gonzalez, Edgar.
# exg6686
# 2019-04-17

import sys

from .common import  *

#---------#---------#---------#---------#---------#--------#
class Block_Stmt() :
    def __init__( self, lineNum, stmtDeclList ) :
        self.m_NodeType = 'Block_Stmt'
        self.m_LineNum = lineNum
        self.m_StmtDeclList = stmtDeclList
    def dump( self, indent = 0, fp = sys.stdout ) :
        dumpHeaderLine( indent,  self.m_LineNum,
                f'STATEMENT (BLOCK) <{len(self.m_StmtDeclList)}>', fp )
        for x in self.m_StmtDeclList:
            x.dump( indent + 1, fp = fp )

#---------#---------#---------#---------#---------#--------#