# Gonzalez, Edgar.
# exg6686
# 2019-04-17
import sys
from .common import *
#---------#---------#---------#---------#---------#--------#
class Declaration() :
    def __init__( self, lineNum, id, type, assign ) :
        self.m_lineNum = lineNum
        self.m_Type = type
        self.m_Assign = assign
        self.m_ID = id
    def dump( self, indent = 0, fp = sys.stdout ) :
        header = 'DECLARATION (VARIABLE-NO-INIT) ' if self.m_Assign is None else 'DECLARATION (VARIABLE) '
        dumpHeaderLine(indent, self.m_lineNum,
                       header + f'ID(\'{self.m_ID.get_id()}\')', fp = fp)
        self.m_Type.dump( indent + 1, fp = fp )
        if self.m_Assign is not None :
            self.m_Assign.dump( indent + 1, fp = fp )
#---------#---------#---------#---------#---------#--------#