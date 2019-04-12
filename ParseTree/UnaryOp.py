# Gonzalez, Edgar.
# exg6686
# 2019-03-04


import sys
from .common import *

class UnaryOp():
    def __init__(self, linenum, op, right ):
        self.m_NodeType = 'UnaryOp'
        self.m_LineNum  = linenum
        self.m_Op       = op
        self.m_Right    = right
    def dump( self, indent = 0, fp = sys.stdout ):
        dumpHeaderLine( indent, self.m_LineNum, f'UNARY_OP {self.m_Op!r}',fp)
        self.m_Right.dump( indent+1, fp=fp )

