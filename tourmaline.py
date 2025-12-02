import re # Regular expressions for parsing
from typing import List, Tuple, Any # Type hints for clarity
import sys # For CLI argument handling
import os # For filesystem checks

# -------------------------
# Simple AST Node Classes
# -------------------------
class Node: pass

class Program(Node):
    def __init__(self, stmts): self.stmts = stmts

class Print(Node):
    def __init__(self, expr): self.expr = expr

class Let(Node):
    def __init__(self, name, typ, expr): self.name = name; self.typ = typ; self.expr = expr

class If(Node):
    def __init__(self, cond, then_body, elifs, else_body):
        self.cond = cond; self.then_body = then_body; self.elifs = elifs; self.else_body = else_body

class While(Node):
    def __init__(self, cond, body): self.cond = cond; self.body = body

class ForRange(Node):
    def __init__(self, var, start, end, body): self.var = var; self.start = start; self.end = end; self.body = body

class Func(Node):
    def __init__(self, name, params, body): self.name = name; self.params = params; self.body = body

class Return(Node):
    def __init__(self, expr): self.expr = expr

class ExprStmt(Node):
    def __init__(self, expr): self.expr = expr

# Expressions
class BinOp(Node):
    def __init__(self, left, op, right): self.left = left; self.op = op; self.right = right

class Number(Node):
    def __init__(self, value): self.value = int(value)

class String(Node):
    def __init__(self, value): self.value = value

class Bool(Node):
    def __init__(self, value: bool): self.value = value

class Var(Node):
    def __init__(self, name): self.name = name

class Call(Node):
    def __init__(self, name, args): self.name = name; self.args = args

class List(Node):
    def __init__(self, elements): self.elements = elements

class Module(Node):
    def __init__(self, name, body): self.name = name; self.body = body

class Import(Node):
    def __init__(self, module_name): self.module_name = module_name

class Index(Node):
    def __init__(self, collection, index): self.collection = collection; self.index = index
# -------------------------
# Tiny parser (line-based)
# -------------------------

def is_int(s: str) -> bool: # Check if string is integer
    try:
        int(s) # Try conversion
        return True
    except:
        return False

def split_outside(s: str, sep: str) -> List[str]:
    """
    Split the string 's' by separator 'sep', but only when the
    separator appears at the top level - that is, not inside parentheses
    and not inside string literals.
    
    This is useful for parsing argument lists like:
        a, b, (c,d), "x,y", e
    which should split into:
        ["a", "b", "(c,d)", "\"x,y\"", "e"]
    """
    parts = []                              # Final list of split segments
    cur = ''                                # Current segment being constructed
    depth = 0                               # Parenthesis nesting depth - 0 means top-level
    in_str = False                          # Whether we're currently inside a quoted string
    i = 0                                   # Manual index for processing characters
    while i < len(s):
        c = s[i]                            # Current character
        if c == '"':                        # Toggle string mode when encountering an unescaped quote
            in_str = not in_str     
            cur += c
        elif not in_str:                    # Only treat parentheses or separators if NOT inside a string
            if c == '(':                    # Increase depth when entering parentheses
                depth += 1; cur += c
            elif c == ')':                  # Decrease depth when exiting parentheses
                depth -= 1; cur += c
            elif c == sep and depth == 0:   # Separator at top level -> Perform the split
                parts.append(cur)
                cur = ''                    # Start new segment
            else:                           # Normal character (outside string, not a split point)
                cur += c
        else:                               # Inside a string: everything counts literally
            cur += c
        i += 1                              # Move to next character
    parts.append(cur)                       # Add the final segment
                                            # Strip whitespace and remove empty segments
    return [p.strip() for p in parts if p.strip() != '']

def parse_expr(token: str):
    token = token.strip()
    if token == '':
        raise RuntimeError("Empty expression")

    if token.startswith('(') and token.endswith(')'):
        return parse_expr(token[1:-1])

    if token.startswith('"') and token.endswith('"'):
        return String(token[1:-1])
    
    m = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\[(.*)\]$', token)
    if m:
        name = m.group(1)
        idx_expr = parse_expr(m.group(2))
        return Index(Var(name), idx_expr)

    if token.startswith('[') and token.endswith(']'):
        inner = token[1:-1].strip()
        if not inner:
            return List([])
        parts = split_outside(inner, ',')
        elements = [parse_expr(p) for p in parts]
        return List(elements)

    if '..' in token:
        left, right = token.split('..', 1)
        return BinOp(parse_expr(left), '..', parse_expr(right))

    for op in ['==', '!=', '>=', '<=', '+', '-', '*', '/', '>', '<']:
        if op in token:
            left, right = token.split(op, 1)
            return BinOp(parse_expr(left), op, parse_expr(right))

    if is_int(token):
        return Number(token)

    return Var(token)

def parse_lines(lines: List[str], i=0) -> Tuple[List[Node], int]:
    stmts: List[Node] = []
    while i < len(lines):
        raw = lines[i]; i += 1
        line = raw.strip()

        if line == '' or line.startswith('#'):
            continue

        if line.startswith('print '):
            expr = line[len('print '):].strip()
            stmts.append(Print(parse_expr(expr)))

        elif line.startswith('let '):
            body = line[len('let '):].strip()
            if '=' not in body:
                raise RuntimeError("let must have '='")
            left, right = body.split('=', 1)
            left = left.strip(); right = right.strip()

            if ':' in left:
                name, typ = [p.strip() for p in left.split(':',1)]
            else:
                name, typ = left, None

            stmts.append(Let(name, typ, parse_expr(right)))

        elif line.startswith('if '):
            cond = parse_expr(line[len('if '):].strip())
            then_body, i = parse_lines(lines, i)
            elifs = []
            else_body = []

            while i < len(lines):
                nxt = lines[i].strip()
                if nxt.startswith('elif '):
                    i += 1
                    econd = parse_expr(nxt[len('elif '):].strip())
                    ebody, i = parse_lines(lines, i)
                    elifs.append((econd, ebody))
                elif nxt == 'else':
                    i += 1
                    else_body, i = parse_lines(lines, i)
                elif nxt == 'end':
                    i += 1
                    break
                else:
                    break

            stmts.append(If(cond, then_body, elifs, else_body))

        elif line.startswith('while '):
            cond = parse_expr(line[len('while '):].strip())
            body, i = parse_lines(lines, i)
            stmts.append(While(cond, body))

        elif line.startswith('for '):
            m = re.match(r'for\s+([A-Za-z_][A-Za-z0-9_]*)\s+in\s+(.*)$', line)
            if not m:
                raise RuntimeError("bad for syntax")
            var = m.group(1)
            rng = m.group(2).strip()
            if '..' not in rng:
                raise RuntimeError("for only supports ranges a..b")
            a,b = rng.split('..',1)
            start = parse_expr(a)
            end = parse_expr(b)
            body, i = parse_lines(lines, i)
            stmts.append(ForRange(var, start, end, body))

        elif line.startswith('func '):
            rest = line[len('func '):].strip()
            name = rest[:rest.index('(')].strip()
            args_raw = rest[rest.index('(')+1:rest.rindex(')')].strip()
            params = []
            if args_raw:
                parts = split_outside(args_raw, ',')
                for p in parts:
                    if ':' in p:
                        n,t = [q.strip() for q in p.split(':',1)]
                    else:
                        n,t = p.strip(), None
                    params.append((n,t))
            body, i = parse_lines(lines, i)
            stmts.append(Func(name, params, body))

        elif line == 'end':
            return stmts, i

        elif line.startswith('return '):
            expr = parse_expr(line[len('return '):].strip())
            stmts.append(Return(expr))

        else:
            if '=' in line:
                left, right = line.split('=',1)
                left = left.strip(); right = right.strip()
                stmts.append(Let(left, None, parse_expr(right)))
            else:
                stmts.append(ExprStmt(parse_expr(line)))

    return stmts, i

# -------------------------
# Compiler -> bytecode
# -------------------------

class Compiler:
    def __init__(self):
        self.consts: List[Any] = []
        self.const_map = {}
        self.code: List[Tuple[str, Any]] = []
        self.functions = {}

    def add_const(self, v):
        key = (type(v), v)
        if key in self.const_map:
            return self.const_map[key]
        idx = len(self.consts)
        self.consts.append(v)
        self.const_map[key] = idx
        return idx

    def emit(self, instr: str, arg=None):
        self.code.append((instr, arg))

    def compile_program(self, program: Program):
        for s in program.stmts:
            if isinstance(s, Func):
                self.compile_func(s)

        for s in program.stmts:
            if not isinstance(s, Func):
                self.compile_stmt(s)

        self.emit('HALT', None)
        return {'code': self.code, 'consts': self.consts, 'functions': self.functions}

    def compile_stmt(self, s: Node):
        if isinstance(s, Print):
            self.compile_expr(s.expr)
            self.emit('PRINT', None)

        elif isinstance(s, Let):
            self.compile_expr(s.expr)
            self.emit('STORE', s.name)

        elif isinstance(s, If):
            # Compile condition
            self.compile_expr(s.cond)
            jfalse_pos = len(self.code); self.emit('JUMP_IF_FALSE', None)

            # compile then body
            for stmt in s.then_body: self.compile_stmt(stmt)

            # after then, jump to end
            jend_positions = []
            jend_positions.append(len(self.code)); self.emit('JUMP', None)

            # fix the initial jump to after then
            self.code[jfalse_pos] = ('JUMP_IF_FALSE', len(self.code))

            # compile elifs
            for (ec, ebody) in s.elifs:
                self.compile_expr(ec)
                ef_jfalse = len(self.code); self.emit('JUMP_IF_FALSE', None)
                for stmt in ebody: self.compile_stmt(stmt)
                jend_positions.append(len(self.code)); self.emit('JUMP', None)
                # set this elif's false jump to after its body (i.e., next code position)
                self.code[ef_jfalse] = ('JUMP_IF_FALSE', len(self.code))

            # compile else body (if any)
            if s.else_body:
                for stmt in s.else_body: self.compile_stmt(stmt)

            # now patch all JUMP placeholders that belong to this if/elif block to jump to end
            end_pos = len(self.code)
            for idx in jend_positions:
                # ensure that we only patch JUMP instructions that still have None (placeholders)
                instr, arg = self.code[idx]
                if instr == 'JUMP' and arg is None:
                    self.code[idx] = ('JUMP', end_pos)

        elif isinstance(s, Module):
            subcompiler = Compiler()
            subcompiler.compile_stmt(s.body)
            self.funcs[s.name] = subcompiler.functions
            
        elif isinstance(s, Import):
            module_funcs = self.funcs.get(s.module_name, {})
            self.funcs.update(module_funcs)
        
        elif isinstance(s, While):
            loop_start = len(self.code)
            self.compile_expr(s.cond)
            jfalse_pos = len(self.code); self.emit('JUMP_IF_FALSE', None)

            for stmt in s.body: self.compile_stmt(stmt)

            self.emit('JUMP', loop_start)
            self.code[jfalse_pos] = ('JUMP_IF_FALSE', len(self.code))

        elif isinstance(s, ForRange):
            # initialize loop variable to start
            self.compile_expr(s.start)
            self.emit('STORE', s.var)

            loop_start = len(self.code)

            # check loop condition: while var <= end
            self.emit('LOAD', s.var)
            self.compile_expr(s.end)
            # use '<=' to continue while var <= end
            self.emit('BINOP', '<=')
            jfalse_pos = len(self.code); self.emit('JUMP_IF_FALSE', None)

            # body
            for stmt in s.body: self.compile_stmt(stmt)

            # increment var by 1
            self.emit('LOAD', s.var)
            self.emit('PUSH_CONST', self.add_const(1))
            self.emit('BINOP', '+')
            self.emit('STORE', s.var)
            # jump back to loop start to re-evaluate
            self.emit('JUMP', loop_start)

            # patch exit jump
            self.code[jfalse_pos] = ('JUMP_IF_FALSE', len(self.code))

        elif isinstance(s, ExprStmt):
            self.compile_expr(s.expr)
            self.emit('POP', None)

        elif isinstance(s, Return):
            self.compile_expr(s.expr)
            self.emit('RET', None)

        else:
            raise RuntimeError(f"Unsupported statement: {type(s)}")

    def compile_expr(self, e: Node):
        if isinstance(e, Number):
            idx = self.add_const(e.value)
            self.emit('PUSH_CONST', idx)

        elif isinstance(e, String):
            idx = self.add_const(e.value)
            self.emit('PUSH_CONST', idx)

        elif isinstance(e, Bool):
            idx = self.add_const(e.value)
            self.emit('PUSH_CONST', idx)

        elif isinstance(e, Var):
            self.emit('LOAD', e.name)

        elif isinstance(e, BinOp):
            if e.op == '..':
                self.compile_expr(e.left)
                self.compile_expr(e.right)
                self.emit('RANGE', None)
            else:
                self.compile_expr(e.left)
                self.compile_expr(e.right)
                self.emit('BINOP', e.op)

        elif isinstance(e, Call):
            for arg in e.args: self.compile_expr(arg)
            self.emit('CALL', (e.name, len(e.args)))
            
        elif isinstance(e, List):
            for element in e.elements:
                self.compile_expr(element)
            self.emit('PUSHLIST', len(e.elements))  # push list of N elements

        elif isinstance(e, Index):
            self.compile_expr(e.collection)
            self.compile_expr(e.index)
            self.emit('INDEX', None)
        else:
            raise RuntimeError(f"Unsupported expr: {type(e)}")

    def compile_func(self, f: Func):
        subc = Compiler()

        for stmt in f.body:
            subc.compile_stmt(stmt)

        subc.emit('RET', None)
        obj = {'code': subc.code, 'consts': subc.consts, 'params': f.params}
        self.functions[f.name] = obj

# -------------------------
# Small stack-based VM
# -------------------------

class Frame:
    def __init__(self, code, consts, locals_):
        self.code = code
        self.consts = consts
        self.locals = locals_
        self.stack = []
        self.ip = 0

class VM:
    def __init__(self, compiled):
        self.code = compiled['code']
        self.consts = compiled['consts']
        self.funcs = compiled['functions']
        self.globals = {}
        self.stack = []
        self.ip = 0
        self.running = True
        
    def import_module(self, name):
        if name in self.modules:
            # Module already loaded
            return self.modules[name]
        # Load module code and execute to initialize
        # For simplicity, assume modules compiled separately and available
        module_funcs = self.funcs.get(name, {})
        self.modules[name] = module_funcs
        return module_funcs

    def run(self):
        while self.ip < len(self.code) and self.running:
            instr, arg = self.code[self.ip]; self.ip += 1

            if instr == 'PUSH_CONST':
                self.stack.append(self.consts[arg])

            elif instr == 'LOAD':
                self.stack.append(self.globals.get(arg, None))

            elif instr == 'STORE':
                val = self.stack.pop()
                self.globals[arg] = val

            elif instr == 'PRINT':
                v = self.stack.pop()
                print("PRINT output:", v)
                if isinstance(v, List):
                    s = "[" + ", ".join(str(x) for x in v) + "]"
                    print(s)
                else:
                    print(v)

            elif instr == 'POP':
                if not self.stack:
                    raise RuntimeError("POP on empty stack")
                self.stack.pop()

            elif instr == 'BINOP':
                op = arg
                b = self.stack.pop()
                a = self.stack.pop()

                if op == '+':
                    if isinstance(a, str) or isinstance(b, str):
                        self.stack.append(str(a) + str(b))
                    else:
                        self.stack.append(a + b)
                elif op == '-':
                    self.stack.append(a - b)
                elif op == '*':
                    self.stack.append(a * b)
                elif op == '/':
                    if isinstance(a, int) and isinstance(b, int):
                        self.stack.append(a // b)
                    else:
                        self.stack.append(a / b)
                elif op == '==':
                    self.stack.append(a == b)
                elif op == '!=':
                    self.stack.append(a != b)
                elif op == '>':
                    self.stack.append(a > b)
                elif op == '<':
                    self.stack.append(a < b)
                elif op == '>=':
                    self.stack.append(a >= b)
                elif op == '<=':
                    self.stack.append(a <= b)
                else:
                    raise RuntimeError(f"Unknown BINOP {op}")

            elif instr == 'RANGE':
                end = self.stack.pop()
                start = self.stack.pop()
                self.stack.append(range(start, end + 1))

            elif instr == 'JUMP':
                self.ip = arg

            elif instr == 'JUMP_IF_FALSE':
                cond = self.stack.pop()
                if not cond:
                    self.ip = arg

            elif instr == 'CALL':
                name, argc = arg

                if name == 'print':
                    args = [self.stack.pop() for _ in range(argc)][::-1]
                    for a in args:
                        print(a)
                    self.stack.append(None)

                elif name in self.funcs:
                    func_obj = self.funcs[name]
                    frame = Frame(func_obj['code'], func_obj['consts'], {})

                    for (pname, ptype) in reversed(func_obj['params']):
                        if argc <= 0:
                            break
                        val = self.stack.pop()
                        frame.locals[pname] = val
                        argc -= 1

                    saved = (self.code, self.consts, self.ip, self.stack, self.globals)

                    self.code = frame.code
                    self.consts = frame.consts
                    self.ip = 0
                    self.stack = []
                    self.globals = frame.locals

                    while self.ip < len(self.code):
                        instr2, arg2 = self.code[self.ip]
                        self.ip += 1

                        if instr2 == 'PUSH_CONST':
                            self.stack.append(self.consts[arg2])

                        elif instr2 == 'LOAD':
                            self.stack.append(self.globals.get(arg2, None))

                        elif instr2 == 'STORE':
                            val = self.stack.pop()
                            self.globals[arg2] = val

                        elif instr2 == 'PRINT':
                            v = self.stack.pop()
                            print(v)

                        elif instr2 == 'POP':
                            if not self.stack:
                                raise RuntimeError("POP on empty stack in func")
                            self.stack.pop()

                        elif instr2 == 'BINOP':
                            op2 = arg2
                            b2 = self.stack.pop()
                            a2 = self.stack.pop()

                            if op2 == '+':
                                if isinstance(a2, str) or isinstance(b2, str):
                                    self.stack.append(str(a2) + str(b2))
                                else:
                                    self.stack.append(a2 + b2)
                            elif op2 == '-':
                                self.stack.append(a2 - b2)
                            elif op2 == '*':
                                self.stack.append(a2 * b2)
                            elif op2 == '/':
                                if isinstance(a2, int) and isinstance(b2, int):
                                    self.stack.append(a2 // b2)
                                else:
                                    self.stack.append(a2 / b2)
                            elif op2 == '==':
                                self.stack.append(a2 == b2)
                            elif op2 == '!=':
                                self.stack.append(a2 != b2)
                            elif op2 == '>':
                                self.stack.append(a2 > b2)
                            elif op2 == '<':
                                self.stack.append(a2 < b2)
                            elif op2 == '>=':
                                self.stack.append(a2 >= b2)
                            elif op2 == '<=':
                                self.stack.append(a2 <= b2)
                            else:
                                raise RuntimeError("Unknown BINOP in func")

                        elif instr2 == 'RET':
                            retval = self.stack.pop() if self.stack else None
                            self.code, self.consts, self.ip, caller_stack, caller_globals = saved
                            self.stack = caller_stack
                            self.globals = caller_globals
                            self.stack.append(retval)
                            break

                        elif instr2 == 'JUMP':
                            self.ip = arg2

                        elif instr2 == 'JUMP_IF_FALSE':
                            cond2 = self.stack.pop()
                            if not cond2:
                                self.ip = arg2

                        elif instr2 == 'CALL':
                            name2, argc2 = arg2
                            if name2 == 'print':
                                args2 = [self.stack.pop() for _ in range(argc2)][::-1]
                                for a in args2:
                                    print(a)
                                self.stack.append(None)
                            else:
                                raise RuntimeError("Nested user-defined CALL inside function not supported")

                        else:
                            raise RuntimeError("Unsupported func instr: " + str(instr2))

                else:
                    raise RuntimeError(f"Unknown function '{name}'")

            elif instr == 'RET':
                self.running = False
                return

            elif instr == 'HALT':
                return

            elif instr == 'PUSHLIST':
                count = arg
                elements = [self.stack.pop() for _ in range(count)]
                elements.reverse()
                self.stack.append(elements)
            
            elif instr == 'INDEX':
                idx = self.stack.pop()
                collection = self.stack.pop()
                if isinstance(collection, list) and isinstance(idx, int):
                    elem = collection[idx]
                    print("INDEX operation:", elem)
                    self.stack.append(elem)
                else:
                    print("INDEX operation failed")
                    self.stack.append(None)
            else:
                raise RuntimeError(f"Unknown instruction: {instr}")

# -------------------------
# Runner
# -------------------------

def run_tourmaline(source: str):
    lines = source.splitlines()
    stmts, _ = parse_lines(lines)
    prog = Program(stmts)
    comp = Compiler()
    compiled = comp.compile_program(prog)
    vm = VM(compiled)
    vm.run()

# =====================================================================
# =====================================================================
#                     ***   CLI WRAPPER ADDED   ***
# =====================================================================
# Allows invoking:
#
#     python tourmaline_fixed.py myscript.toma
#         or
#     toma myscript.toma
#
# Does NOT modify or remove anything above.
# =====================================================================

def main():
    if len(sys.argv) < 2:
        print("Usage: toma <file.toma>")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"Error: file not found: {filename}")
        sys.exit(1)

    with open(filename, "r", encoding="utf-8") as f:
        source = f.read()

    run_tourmaline(source)

# If run directly, use CLI instead of example demo.
if __name__ == '__main__':
    main()
