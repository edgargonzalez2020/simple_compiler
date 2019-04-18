# Gonzalez, Edgar.
# exg6686
# 2019-03-04
#---------#---------#---------#---------#---------#--------#
import sys
import traceback
import re

import ply
import ply.yacc
import ply.lex

from pathlib            import Path
from time               import time

from Exceptions         import *
from ParseTree          import *

#---------#---------#---------#---------#---------#--------#
lexer  = None
parser = None

#---------#---------#---------#---------#---------#--------#
# Lexical analysis section

tokens = (
    'ID', 'INT_LITERAL','STRING_LITERAL',
    'PLUS', 'ASSIGN','MINUS','TIMES', 'DIVIDE', 'MODULUS', 'POWER','LT','LTE','EQUALS','NE','GT','GTE',
    'AND', 'OR','NOT','COLON', 'INT', 'IF', 'ELSE','READ','WRITE','WHILE','COMMA',
    'LPAREN', 'RPAREN', 'SEMICOLON', 'LBRACE', 'RBRACE'
)
reserved = {
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT',
    'read': 'READ',
    'write': 'WRITE',
}
# Tokens
t_COMMA          = r','
t_RBRACE         = r'}'
t_LBRACE         = r'{'
t_WHILE          = r'while'
t_WRITE          = r'write'
t_READ           = r'read'
t_ELSE           = r'else'
t_IF             = r'if'
t_INT            = r'int'
t_COLON          = r':'
t_NOT            = r'!'
t_OR             = r'\|\|'
t_AND            = r'&&'
t_GTE            = r'>='
t_GT             = r'>'
t_NE             = r'!='
t_LTE            = r'<='
t_LT             = r'<'
t_ASSIGN         = r'='
t_EQUALS         = r'=='
t_MINUS          = r'-'
t_TIMES          = r'\*'
t_DIVIDE         = r'/'
t_MODULUS        = r'%'
t_POWER          = r'\^'
t_LPAREN         = r'\('
t_PLUS           = r'\+'
t_RPAREN         = r'\)'
t_SEMICOLON      = r';'

t_STRING_LITERAL = r'\"(\\.|[^"\\])*\"'

def t_ID( t ) :
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get( t.value, 'ID' )
    return t

def t_INT_LITERAL( t ) :
    r'\d+'
    t.value = int( t.value )
    return t

#-------------------
# Ignored characters
# Space, formfeed, carriage return, tab, vertical tab
t_ignore = ' \f\r\t\v'

# Eats characters from the // marker to the end of the line.
def t_comment( _ ) :
    r'//[^\n]*'

# Keep track of what line we're on.
def t_newline( t ) :
    r'\n+'
    t.lexer.lineno += t.value.count( '\n' )

#-------------------
def t_error( t ) :
    # Go through elaborate shennanigans to determine the column
    # at which the lexical error occurred.
    lineStart = t.lexer.lexdata.rfind('\n', 0, t.lexer.lexpos) + 1
    column = t.lexer.lexpos - lineStart + 1

    msg = f'Illegal character "{t.value[0]}" at line {t.lexer.lineno}, column {column}.'

    #t.lexer.skip( 1 ) -- We used to just skip the character.
    #                  -- Now we throw an exception.

    raise LexicalError( msg )

#---------#---------#---------#---------#---------#--------#
# Syntactic analysis section

#-------------------
# The start symbol.
start = 'program'

#-------------------
# Precedence rules for the operators
precedence = (
    ( 'right', 'ASSIGN' ),
    ( 'left','OR'),
    ( 'left', 'AND'),
    ( 'left','EQUALS','NE'),
    ( 'nonassoc','LT','LTE','GT','GTE'),
    ( 'left',  'PLUS', 'MINUS' ),
    ( 'left','TIMES', 'DIVIDE', 'MODULUS'),
    ('left', 'NOT'),
    ( 'right', 'POWER' ),
    ( 'right', 'UMINUS', 'UPLUS')
)

#-------------------
# PROGRAM ...
def p_program( p ) :
    'program : block_stmt'
    p[0] = Program( p.lineno(1), p[1] )
def p_block_stmt( p ) :
    '''block_stmt : LBRACE stmt_decl_list RBRACE'''
    print('BLOCK', p[2])
    p[0] = Block_Stmt( p.lineno(1), p[2] )
def p_stmt_decl_list( p ) :
    '''stmt_decl_list : epsilon
                      | stmt_decl_list_more stmt_decl semicolon_opt'''
    if p[1] is not None :
        p[1].append(p[2])
        p[0] = p[1]
    else :
        p[0] = []
def p_stmt_decl_list_more( p ) :
    '''stmt_decl_list_more : epsilon
                           | stmt_decl_list_more stmt_decl SEMICOLON'''
    if p[1] is not None :
        p[1].append(p[2])
        p[0] = p[1]
    else :
        p[0] = []
def p_stmt_decl( p ) :
    '''stmt_decl : stmt
                 | decleration'''
    p[0] = p[1]
def p_semicolon_opt( p ) :
    '''semicolon_opt : epsilon
                     | SEMICOLON'''
    pass

#-------------------
# STATEMENTS ...
#-------------------
# IDENTIFIER ...
def p_decleration( p ) :
    'decleration : identifier COLON type assignment_opt'
    p[0] = Declaration( p.lineno(1), p[1], p[3], p[4] )

def p_type( p ) :
    'type : INT'
    p[0] = Type( p.lineno(1), p[1] )

def p_identifier( p ) :
    'identifier : ID'
    p[0] = Identifier( p.lineno( 1 ), p[1] )

#-------------------
# EXPRESSIONS ...
# Binary operator expression

def p_lvalue( p ):
    'lvalue : identifier '
    p[0] = Lvalue( p.lineno(1), p[1] )

def p_expression_binop( p ) :
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression DIVIDE expression
                  | expression MODULUS expression
                  | expression TIMES expression
                  | expression POWER expression
                  | expression LT expression
                  | expression LTE expression
                  | expression GT expression
                  | expression GTE expression
                  | expression AND expression
                  | expression OR expression
                  | expression EQUALS expression
                  | expression NE expression
                  | lvalue ASSIGN expression
                  '''
    p[0] = BinaryOp( p.lineno(2), p[2], p[1], p[3] )
# Unary operator expression 
def p_expression_unop( p ):
    ''' expression : MINUS expression %prec UMINUS
                   | PLUS expression %prec UPLUS
                   | NOT expression'''
    p[0] = UnaryOp( p.lineno(2), p[1], p[2] )

# Parenthesized expression
def p_expression_group( p ) :
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

# Integer literal
def p_literal( p ) :
    '''literal : STRING_LITERAL
               | INT_LITERAL'''
    if type(p[1]) is not int:
        p[0] = Literal( p.lineno(1), 'string', p[1] )
    else :
        p[0] = Literal( p.lineno(1), 'int', p[1] )

def p_expression_int_literal( p ) :
    '''expression : literal
                  | lvalue'''
    p[0] = p[1]


def p_assignment_opt( p ):
    '''assignment_opt : epsilon
                      | ASSIGN expression'''
    if p[1] is None :
        p[0] = None
    else :
        p[0] = p[2]
def p_expr_stmt( p ) :
    '''expr_stmt : expression'''
    p[0] = Statement_Expression(p.lineno(1), p[1])
def p_stmt( p ) :
    '''stmt : block_stmt
            | expr_stmt
            | if_stmt
            | read_stmt
            | while_stmt
            | write_stmt'''
    p[0] = p[1]
def p_if_stmt( p ) :
    'if_stmt : IF expression block_stmt else_opt'
    p[0] = If_Stmt( p.lineno(1), p[2], p[3],p[4] )

def p_else_opt( p ) :
    '''else_opt : epsilon
                | ELSE block_stmt'''
    if p[1] is None :
        p[0] = None
    else :
        p[0] = p[2]


def p_read_stmt( p ) :
    'read_stmt : READ LPAREN lvalue_list RPAREN'
    p[0] = Read_Stmt( p.lineno(1), p[3] )

def p_lvalue_list( p ) :
    '''lvalue_list : lvalue_more lvalue'''
    if p[1] is None:
        p[0] = []
    else :
        p[1].append(p[2])
        p[0] = p[1]

def p_lvalue_more( p ) :
    '''lvalue_more : epsilon
                   | lvalue_more lvalue COMMA '''
    if p[1] is None:
        p[0] = []
    else :
        p[1].append(p[2])
        p[0] = p[1]

def p_while_stmt( p ) :
    'while_stmt : WHILE expression block_stmt'
    p[0] = While_Stmt( p.lineno(1), p[2], p[3] )
def p_write_stmt( p ):
    'write_stmt : WRITE LPAREN expr_string_list RPAREN'
    print('WRITE', p[3])
    p[0] = Write_Stmt( p.lineno(1), p[3] )

def p_expr_string_list( p ) :
    '''expr_string_list : epsilon
                        | expr_string_more expression'''
    if p[1] is None:
        p[0] = []
    else :
        p[1].append(p[2])
        p[0] = p[1]

def p_expr_string_more( p ) :
    '''expr_string_more : epsilon
                        | expr_string_more expression COMMA'''
    if p[1] is None:
        p[0] = []
    else :
        p[1].append(p[2])
        p[0] = p[1]

#-------------------
# The 'empty' value.  It's possible to just have an empty RHS
# in a production, but having the non-terminal 'epsilon' makes
# it much more obvious that the empty string is being parsed.
def p_epsilon( p ) :
    'epsilon :'
    p[0] = None

#-------------------
# Gets called if an unexpected token (or the EOF) is seen during
# a parse.  We throw an exception
def p_error( p ) :
    msg = 'Syntax error at '
    if p is None :
        msg += 'EOF.'

    else :
        # Go through elaborate shennanigans to determine the column
        # at which the parse error occurred.
        lineStart = lexer.lexdata.rfind('\n', 0, p.lexpos) + 1
        column = p.lexpos - lineStart + 1

        msg += f'token "{p.value}", line {p.lineno}, column {column}'

    raise SyntacticError( msg )
#---------#---------#---------#---------#---------#--------#
def _main( inputFileName ) :
    global lexer
    global parser

    begin = time()

    fileName  = str( Path( inputFileName ).name )
    parseFile = str( Path( inputFileName ).with_suffix( '.parse' ) )

    print( f'* Reading source file {inputFileName!r} ...' )

    strt = time()
    with open( inputFileName, 'r' ) as fp :
        data = fp.read()

    print( f'    Read succeeded.  ({time()-strt:.3f}s)\n* Beginning parse ...' )

    try :
        strt    = time()
        lexer   = ply.lex.lex()
        parser  = ply.yacc.yacc()
        program = parser.parse( data, tracking=True )
        strt = time()
        with open( parseFile, 'w' ) as fp :
            if program is not None:
                program.dump( fp = fp )

        print( f'    Parse dumped.  ({time()-strt:.3f}s)' )

        total = time() - begin
        print( f'# Total time {total:.3f}s.\n#----------')

    except LexicalError as e :
        print( 'Exception detected during lexical analysis.' )
        print( e )
        #traceback.print_exc()
        sys.exit( 1 )

    except SyntacticError as e :
        print( 'Exception detected during syntactic analysis.' )
        print( e )
        #traceback.print_exc()
        sys.exit( 1 )

    except :
        print( '*** (Unknown) exception detected during parse/result dump.' )
        traceback.print_exc()
        sys.exit( 1 )

#---------#---------#---------#
if __name__ == '__main__' :
    if len( sys.argv ) > 1 :
        _main( sys.argv[ 1 ] )

    else :
        print( 'Input file name required.' )

#---------#---------#---------#---------#---------#--------#
