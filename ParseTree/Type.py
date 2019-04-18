# Gonzalez, Edgar.
# exg6686
# 2019-04-17

import sys
from .common import *
#---------#---------#---------#---------#---------#--------#
class Type() :
    def __init__(self, lineNum, type) :
        self.lineNum = lineNum
        self.m_Type = type
    def dump (self, indent = 0, fp = sys.stdout ) :
        dumpHeaderLine( indent, self.lineNum,
                       f"TYPE (NAME) '{self.m_Type}'", fp = fp )
#---------#---------#---------#---------#---------#--------#