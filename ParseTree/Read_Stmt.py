# Gonzalez, Edgar.
# exg6686
# 2019-03-04

import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Read_Stmt() :
    def __init__( self, lineNum, lvalueList ) :
        self.m_LineNum = lineNum
        self.m_LvalueList = lvalueList
    def dump( self, indent = 0, fp = sys.stdout ) :
        dumpHeaderLine( indent, self.m_LineNum,
                        f'STATEMENT (READ) <{len(self.m_LvalueList)}>', fp = fp )
        for x in self.m_LvalueList :
            x.dump( indent + 1 , fp = fp )

#---------#---------#---------#---------#---------#--------#