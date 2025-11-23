import basic


class Codegen:
  def __init__(self):
    self.code = []  # list[(op, arg)]

  def emit(self, op, arg=None):
    self.code.append((op, arg))

  def compile(self, source_name, text):
    # Parse to AST without executing
    lexer = basic.Lexer(source_name, text)
    tokens, error = lexer.make_tokens()
    if error:
      return None, error
    parser = basic.Parser(tokens)
    ast = parser.parse()
    if ast.error:
      return None, ast.error
    self.visit(ast.node)
    self.emit('HALT')
    return self.code, None

  # Visitors for subset
  def visit(self, node):
    method = getattr(self, f'visit_{type(node).__name__}', self.no_visit)
    return method(node)

  def no_visit(self, node):
    # For nodes outside subset we just ignore values to keep demo simple
    return None

  def visit_ListNode(self, node):
    for n in node.element_nodes:
      self.visit(n)
      # discard top-level expression value to avoid stack growth,
      # but skip if the last op was PRINT (already consumed)
      if not self.code:
        continue
      last_op, _ = self.code[-1]
      if last_op != 'PRINT':
        self.emit('POP')

  def visit_NumberNode(self, node):
    if node.tok.type == basic.TT_INT:
      self.emit('PUSH_INT', node.tok.value)
    else:
      self.emit('PUSH_FLOAT', node.tok.value)

  def visit_StringNode(self, node):
    self.emit('PUSH_STR', node.tok.value)

  def visit_BinOpNode(self, node):
    self.visit(node.left_node)
    self.visit(node.right_node)
    t = node.op_tok.type
    if t == basic.TT_PLUS:
      self.emit('ADD')
    elif t == basic.TT_MINUS:
      self.emit('SUB')
    elif t == basic.TT_MUL:
      self.emit('MUL')
    elif t == basic.TT_DIV:
      self.emit('DIV')
    elif t == basic.TT_MOD:
      self.emit('MOD')
    elif t == basic.TT_POW:
      self.emit('POW')

  def visit_CallNode(self, node):
    # Support PRINT(expr) or ECHO(expr)
    target = getattr(node.node_to_call, 'var_name_tok', None)
    if target and target.value in ('PRINT', 'ECHO') and len(node.arg_nodes) == 1:
      self.visit(node.arg_nodes[0])
      self.emit('PRINT')
      return
    # Fallback: evaluate args and discard (no-op in subset)
    for arg in node.arg_nodes:
      self.visit(arg)
      self.emit('POP')


