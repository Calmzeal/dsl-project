from lark.indenter import Indenter

class DSLIndenter(Indenter):
    NL_type = '_NL'
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    tab_len = 2