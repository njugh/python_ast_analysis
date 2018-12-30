# -*- coding: utf-8 -*

import ast

leaf_list = ['Load', 'Store', 'Del', 'AugLoad', 'AugStore', 'Param',
             'Add', 'Sub', 'Mult', 'MatMult' 'Div', 'Mod', 'Pow', 'LShift', 'RShift', 'BitOr', 'BitXor', 'BitAnd',
             'FloorDiv',
             'Invert', 'Not', 'UAdd', 'USub',
             'And', 'or',
             'Eq', 'NotEq', 'Lt', 'LtE', 'Gt', 'GtE', 'Is', 'IsNot', 'In', 'NotIn']


def append(s1, s2):
    s1 += s2
    s1 += ' '
    return s1


class CodeVisitor(ast.NodeVisitor):

    def __init__(self):
        super(CodeVisitor, self).__init__()
        self.str = ""

    def generic_visit(self, node):
        name = type(node).__name__
        if name in leaf_list:
            return name
        else:
            self.str = append(self.str, name)
            ast.NodeVisitor.generic_visit(self, node)
            self.str = append(self.str, '%s End' % (name))
            return None

    def visit_FunctionDef(self, node):
        self.str = append(self.str, type(node).__name__)
        self.str = append(self.str, node.name)
        ast.NodeVisitor.generic_visit(self, node)
        self.str = append(self.str, "%s End" % (type(node).__name__))

    def visit_keyword(self, node):
        self.str = append(self.str, type(node).__name__)
        self.str = append(self.str, node.arg)
        ast.NodeVisitor.generic_visit(self, node)
        self.str = append(self.str, "%s End" % (type(node).__name__))

    def visit_Attribute(self, node):
        self.str = append(self.str, type(node).__name__)
        ast.NodeVisitor.visit(self, node.value)
        atype = ast.NodeVisitor.visit(self, node.ctx)
        self.str = append(self.str, node.attr)
        self.str = append(self.str, atype)
        self.str = append(self.str, "%s End" % (type(node).__name__))

    def visit_Subscript(self, node):
        self.str = append(self.str, type(node).__name__)
        ast.NodeVisitor.visit(self, node.value)
        ast.NodeVisitor.visit(self, node.slice)
        ast.NodeVisitor.visit(self, node.ctx)
        self.str = append(self.str, "%s End" % (type(node).__name__))

    def visit_ImportFrom(self, node):
        self.str = append(self.str, type(node).__name__)
        self.str = append(self.str, str(node.module))
        ast.NodeVisitor.generic_visit(self, node)
        self.str = append(self.str, "%s End" % (type(node).__name__))

    def visit_alias(self, node):
        self.str = append(self.str, node.name)
        self.str = append(self.str, str(node.asname))

    def visit_Compare(self, node):
        self.str = append(self.str, type(node).__name__)
        for i in range(len(node.ops)):
            op = ast.NodeVisitor.visit(self, node.ops[i])
            self.str = append(self.str, op)
        ast.NodeVisitor.generic_visit(self, node)
        self.str = append(self.str, "%s End" % (type(node).__name__))

    def visit_Name(self, node):
        ntype = ast.NodeVisitor.visit(self, node.ctx)
        self.str = append(self.str, type(node).__name__)
        self.str = append(self.str, node.id)
        self.str = append(self.str, ntype)


def process_file(code):
    f = open(code, 'r')
    try:
        ast_text = ast.parse(f.read(), mode='exec')
    except:
        return '', ''
    # get AST str
    tree = ast.dump(ast_text)
    # visit AST node
    visitor = CodeVisitor()
    visitor.visit(ast_text)
    return tree, visitor.str
