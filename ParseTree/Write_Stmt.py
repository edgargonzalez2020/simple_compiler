# Gonzalez, Edgar.
# exg6686
# 2019-03-04

import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Write_Stmt() :
    def __init__( self, lineNum, stringList ) :
        self.m_LineNum = lineNum
        self.m_StringList = stringList
    def dump( self, indent = 0, fp = sys.stdout ) :
        dumpHeaderLine( indent , self.m_LineNum,
                        f'STATEMENT (WRITE) <{len(self.m_StringList)}>', fp = fp )
        for x in self.m_StringList:
            x.dump( indent + 1 , fp = fp )
#---------#---------#---------#---------#---------#--------#