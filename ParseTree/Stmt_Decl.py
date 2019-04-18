# Gonzalez, Edgar.
# exg6686
# 2019-04-17

import sys

from .common import *

#---------#---------#---------#---------#---------#--------#
class Stmt_Decl() :
    def __init__(self, lineNum, stmtDecl ) :
        self.m_NodeType = 'Stmt_Decl'
        self.m_LineNum = lineNum
        self.m_Stmt_Decl = stmtDecl
    def dump( self, indent = 0, fp = sys.stdout ) :
        self.m_Stmt_Decl.dump( indent + 1, fp = fp )
