# Gonzalez, Edgar.
# exg6686
# 2019-03-04

import sys

from .common       import *

#---------#---------#---------#---------#---------#--------#
class Lvalue() :
    def __init__( self, lineNum, lvalue ) :
        self.m_LineNum = lineNum
        self.m_Lvalue = lvalue
    def dump( self, indent = 0, fp = sys.stdout ) :
        dumpHeaderLine( indent, self.m_LineNum,
                        f'LVALUE (NAME) ID(\'{self.m_Lvalue.get_id()}\')', fp = fp )

# ---------#---------#---------#---------#---------#--------#