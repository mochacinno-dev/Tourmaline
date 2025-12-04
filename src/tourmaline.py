import re
import math
from typing import Any, Dict, List, Callable

class TourmalineError(Exception):
    pass

class TourmalineInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.structs = {}
        self.return_value = None
        self.has_returned = False
        self.exception_caught = False
        self.exception_var = None
        self.setup_builtins()
    
    def setup_builtins(self):
        """Setup built-in functions"""
        self.builtins = {
            'print': lambda *args: print(*[str(a) for a in args]),
            'input': lambda prompt="": input(prompt),
            'len': len,
            'str': str,
            'int': self.safe_int,
            'float': self.safe_float,
            'type': lambda x: type(x).__name__,
            # Math functions
            'abs': abs,
            'sqrt': math.sqrt,
            'pow': pow,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'floor': math.floor,
            'ceil': math.ceil,
            'round': round,
            'min': min,
            'max': max,
        }
    
    def safe_int(self, value):
        """Safe integer conversion with better error handling"""
        try:
            if isinstance(value, str):
                # Handle floats in string form
                if '.' in value:
                    return int(float(value))
                return int(value)
            elif isinstance(value, float):
                return int(value)
            elif isinstance(value, bool):
                return 1 if value else 0
            elif isinstance(value, int):
                return value
            else:
                raise ValueError(f"Cannot convert {type(value).__name__} to int")
        except ValueError as e:
            raise TourmalineError(f"Cannot convert '{value}' to integer: {str(e)}")
    
    def safe_float(self, value):
        """Safe float conversion with better error handling"""
        try:
            if isinstance(value, str):
                return float(value)
            elif isinstance(value, (int, float)):
                return float(value)
            elif isinstance(value, bool):
                return 1.0 if value else 0.0
            else:
                raise ValueError(f"Cannot convert {type(value).__name__} to float")
        except ValueError as e:
            raise TourmalineError(f"Cannot convert '{value}' to float: {str(e)}")
    
    def tokenize(self, code: str) -> List[str]:
        """Simple tokenizer"""
        # Handle strings and preserve them
        tokens = []
        current = ""
        in_string = False
        string_char = None
        
        i = 0
        while i < len(code):
            char = code[i]
            
            if char in ('"', "'") and (i == 0 or code[i-1] != '\\'):
                if not in_string:
                    in_string = True
                    string_char = char
                    current = char
                elif char == string_char:
                    in_string = False
                    current += char
                    tokens.append(current)
                    current = ""
                    string_char = None
                    i += 1
                    continue
                else:
                    current += char
            elif in_string:
                current += char
            elif char in ' \t\n':
                if current:
                    tokens.append(current)
                    current = ""
            elif char in '()[]{},:':
                if current:
                    tokens.append(current)
                    current = ""
                tokens.append(char)
            elif char in '=!<>+-*/%':
                if current:
                    tokens.append(current)
                    current = ""
                # Check for multi-char operators
                if i + 1 < len(code) and code[i:i+2] in ['==', '!=', '<=', '>=', '+=', '-=', '*=', '/=']:
                    tokens.append(code[i:i+2])
                    i += 2
                    continue
                tokens.append(char)
            else:
                current += char
            
            i += 1
        
        if current:
            tokens.append(current)
        
        return tokens
    
    def parse_value(self, token: str) -> Any:
        """Parse a token into a value"""
        # String
        if token.startswith('"') or token.startswith("'"):
            return token[1:-1].replace('\\n', '\n').replace('\\t', '\t')
        # Boolean
        if token == 'true':
            return True
        if token == 'false':
            return False
        # None/nil
        if token == 'nil':
            return None
        # Number
        try:
            if '.' in token:
                return float(token)
            return int(token)
        except ValueError:
            pass
        # Variable reference (don't try to resolve functions here)
        if token in self.variables:
            return self.variables[token]
        if token in self.builtins:
            return self.builtins[token]
        
        # If it's a function name, return the name for later resolution
        if token in self.functions:
            return token
        
        raise TourmalineError(f"Undefined variable: {token}")
    
    def evaluate_expression(self, tokens: List[str], start: int = 0, end: int = None) -> Any:
        """Evaluate an expression"""
        if end is None:
            end = len(tokens)
        
        if start >= end:
            raise TourmalineError("Empty expression")
        
        # Handle list literals BEFORE anything else
        if tokens[start] == '[':
            return self.parse_list(tokens, start)
        
        # Handle dictionary literals BEFORE anything else
        if tokens[start] == '{':
            return self.parse_dict(tokens, start)
        
        # Single token
        if end - start == 1:
            return self.parse_value(tokens[start])
        
        # Now resolve all function calls in the expression
        tokens = self.resolve_function_calls(tokens, start, end)
        start = 0
        end = len(tokens)
        
        # Check again after function resolution
        if start >= end:
            return None
        
        if end - start == 1:
            return self.parse_value(tokens[0])
        
        # Handle parentheses (wrapped expression)
        if tokens[start] == '(' and tokens[end-1] == ')':
            depth = 1
            i = start + 1
            valid_wrap = True
            while i < end - 1:
                if tokens[i] == '(':
                    depth += 1
                elif tokens[i] == ')':
                    depth -= 1
                    if depth == 0:
                        valid_wrap = False
                        break
                i += 1
            if valid_wrap:
                return self.evaluate_expression(tokens, start + 1, end - 1)
        
        # Handle dictionary literals
        if tokens[start] == '{':
            return self.parse_dict(tokens, start)
        
        # Logical OR
        for i in range(end - 1, start, -1):
            if tokens[i] == 'or':
                left = self.evaluate_expression(tokens, start, i)
                right = self.evaluate_expression(tokens, i + 1, end)
                return left or right
        
        # Logical AND
        for i in range(end - 1, start, -1):
            if tokens[i] == 'and':
                left = self.evaluate_expression(tokens, start, i)
                right = self.evaluate_expression(tokens, i + 1, end)
                return left and right
        
        # Comparison operators
        for i in range(end - 1, start, -1):
            if tokens[i] in ['==', '!=', '<', '>', '<=', '>=']:
                left = self.evaluate_expression(tokens, start, i)
                right = self.evaluate_expression(tokens, i + 1, end)
                op = tokens[i]
                if op == '==': return left == right
                if op == '!=': return left != right
                if op == '<': return left < right
                if op == '>': return left > right
                if op == '<=': return left <= right
                if op == '>=': return left >= right
        
        # Addition and subtraction
        for i in range(end - 1, start, -1):
            if tokens[i] in ['+', '-'] and i > start:
                left = self.evaluate_expression(tokens, start, i)
                right = self.evaluate_expression(tokens, i + 1, end)
                if tokens[i] == '+':
                    return left + right
                else:
                    return left - right
        
        # Multiplication, division, modulo
        for i in range(end - 1, start, -1):
            if tokens[i] in ['*', '/', '%']:
                left = self.evaluate_expression(tokens, start, i)
                right = self.evaluate_expression(tokens, i + 1, end)
                if tokens[i] == '*':
                    return left * right
                elif tokens[i] == '/':
                    return left / right
                else:
                    return left % right
        
        # Member access (dot notation)
        for i in range(start, end):
            if tokens[i] == '.':
                obj = self.evaluate_expression(tokens, start, i)
                member = tokens[i + 1]
                if isinstance(obj, dict):
                    return obj.get(member)
                raise TourmalineError(f"Cannot access member '{member}'")
        
        # Index access
        for i in range(start, end):
            if tokens[i] == '[':
                obj = self.evaluate_expression(tokens, start, i)
                depth = 1
                j = i + 1
                while j < end and depth > 0:
                    if tokens[j] == '[':
                        depth += 1
                    elif tokens[j] == ']':
                        depth -= 1
                    j += 1
                index = self.evaluate_expression(tokens, i + 1, j - 1)
                return obj[index]
        
        raise TourmalineError(f"Cannot evaluate expression: {' '.join(tokens[start:end])}")
    
    def parse_arguments(self, tokens: List[str], start: int) -> List[Any]:
        """Parse function arguments"""
        if start >= len(tokens) or tokens[start] != '(':
            raise TourmalineError("Expected '('")
        
        depth = 1
        i = start + 1
        args = []
        arg_start = i
        
        while i < len(tokens) and depth > 0:
            if tokens[i] == '(':
                depth += 1
            elif tokens[i] == ')':
                depth -= 1
                if depth == 0:
                    if i > arg_start:
                        args.append(self.evaluate_expression(tokens, arg_start, i))
                    break
            elif tokens[i] == '[':
                depth += 1
            elif tokens[i] == ']':
                depth -= 1
            elif tokens[i] == ',' and depth == 1:
                if i > arg_start:
                    args.append(self.evaluate_expression(tokens, arg_start, i))
                arg_start = i + 1
            i += 1
        
        return args
    
    def parse_list(self, tokens: List[str], start: int) -> List[Any]:
        """Parse a list literal"""
        if tokens[start] != '[':
            raise TourmalineError("Expected '['")
        
        depth = 1
        i = start + 1
        items = []
        item_start = i
        
        while i < len(tokens) and depth > 0:
            if tokens[i] == '[':
                depth += 1
            elif tokens[i] == ']':
                depth -= 1
                if depth == 0:
                    if i > item_start:
                        items.append(self.evaluate_expression(tokens, item_start, i))
            elif tokens[i] == ',' and depth == 1:
                if i > item_start:
                    items.append(self.evaluate_expression(tokens, item_start, i))
                item_start = i + 1
            i += 1
        
        return items
    
    def parse_dict(self, tokens: List[str], start: int) -> Dict[str, Any]:
        """Parse a dictionary literal"""
        if tokens[start] != '{':
            raise TourmalineError("Expected '{'")
        
        depth = 1
        i = start + 1
        result = {}
        
        while i < len(tokens) and depth > 0:
            if tokens[i] == '{':
                depth += 1
                i += 1
            elif tokens[i] == '}':
                depth -= 1
                if depth == 0:
                    break
                i += 1
            elif tokens[i] == ',':
                i += 1
            else:
                # Parse key
                key_start = i
                while i < len(tokens) and tokens[i] != ':':
                    if tokens[i] in ['{', '[']:
                        # Skip nested structures
                        bracket = tokens[i]
                        close_bracket = '}' if bracket == '{' else ']'
                        depth2 = 1
                        i += 1
                        while i < len(tokens) and depth2 > 0:
                            if tokens[i] == bracket:
                                depth2 += 1
                            elif tokens[i] == close_bracket:
                                depth2 -= 1
                            i += 1
                    else:
                        i += 1
                
                if key_start >= i:
                    raise TourmalineError("Expected key in dictionary")
                    
                key = self.evaluate_expression(tokens, key_start, i)
                
                if i >= len(tokens) or tokens[i] != ':':
                    raise TourmalineError("Expected ':' after dictionary key")
                i += 1  # Skip ':'
                
                # Parse value
                value_start = i
                while i < len(tokens) and tokens[i] not in [',', '}']:
                    if tokens[i] in ['{', '[']:
                        bracket = tokens[i]
                        close_bracket = '}' if bracket == '{' else ']'
                        depth2 = 1
                        i += 1
                        while i < len(tokens) and depth2 > 0:
                            if tokens[i] == bracket:
                                depth2 += 1
                            elif tokens[i] == close_bracket:
                                depth2 -= 1
                            i += 1
                    else:
                        i += 1
                
                if value_start >= i:
                    raise TourmalineError("Expected value in dictionary")
                
                value = self.evaluate_expression(tokens, value_start, i)
                result[str(key)] = value
        
        return result
    
    def resolve_function_calls(self, tokens: List[str], start: int, end: int) -> List[str]:
        """Resolve all function calls in a token list and return new token list"""
        result = []
        i = start
        
        while i < end:
            # Skip dictionary literals entirely
            if tokens[i] == '{':
                depth = 1
                result.append(tokens[i])
                i += 1
                while i < end and depth > 0:
                    if tokens[i] == '{':
                        depth += 1
                    elif tokens[i] == '}':
                        depth -= 1
                    result.append(tokens[i])
                    i += 1
                continue
            
            # Skip list literals entirely
            if tokens[i] == '[':
                depth = 1
                result.append(tokens[i])
                i += 1
                while i < end and depth > 0:
                    if tokens[i] == '[':
                        depth += 1
                    elif tokens[i] == ']':
                        depth -= 1
                    result.append(tokens[i])
                    i += 1
                continue
            
            # Check if this is a function call
            if i + 1 < end and tokens[i + 1] == '(':
                func_name = tokens[i]
                
                if func_name in self.functions or func_name in self.builtins:
                    # Find matching closing parenthesis
                    depth = 1
                    j = i + 2
                    while j < end and depth > 0:
                        if tokens[j] == '(':
                            depth += 1
                        elif tokens[j] == ')':
                            depth -= 1
                        j += 1
                    
                    # Parse and call the function
                    try:
                        args = self.parse_arguments(tokens, i + 1)
                        
                        if func_name in self.functions:
                            func_result = self.call_user_function(func_name, args)
                        else:
                            func_result = self.builtins[func_name](*args)
                        
                        # Add result as a token (preserve type for non-strings)
                        if func_result is not None:
                            if isinstance(func_result, str):
                                result.append('"' + func_result + '"')
                            else:
                                result.append(str(func_result))
                    except Exception as e:
                        raise TourmalineError(f"Error calling function '{func_name}': {e}")
                    
                    i = j
                    continue
            
            result.append(tokens[i])
            i += 1
        
        return result
    
    def call_user_function(self, func_name: str, args: List[Any]) -> Any:
        """Call a user-defined function"""
        if func_name not in self.functions:
            raise TourmalineError(f"Function '{func_name}' not defined")
        
        func_lines = self.functions[func_name]
        
        # Parse function definition to get parameters
        first_line = func_lines[0].strip()
        tokens = self.tokenize(first_line)
        
        # Extract parameter names
        params = []
        if '(' in tokens:
            paren_idx = tokens.index('(')
            i = paren_idx + 1
            while i < len(tokens) and tokens[i] != ')':
                if tokens[i] != ',':
                    params.append(tokens[i])
                i += 1
        
        # Save current variable state
        saved_vars = self.variables.copy()
        
        # Set parameter values
        for i, param in enumerate(params):
            if i < len(args):
                self.variables[param] = args[i]
        
        # Set a flag for return value
        self.return_value = None
        self.has_returned = False
        
        # Execute function body
        body = '\n'.join(func_lines[1:-1])  # Exclude first and last (end) lines
        try:
            self.execute(body)
        finally:
            # Get return value before restoring
            result = self.return_value
            # Restore variable state
            self.variables = saved_vars
            # Clear return flags
            self.has_returned = False
            self.return_value = None
        
        return result
    
    def execute(self, code: str):
        """Execute Tourmaline code"""
        lines = code.split('\n')
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            if not line or line.startswith('#'):
                i += 1
                continue
            
            tokens = self.tokenize(line)
            
            if not tokens:
                i += 1
                continue
            
            # Variable declaration
            if tokens[0] == 'let':
                if len(tokens) < 4 or tokens[2] != '=':
                    raise TourmalineError("Invalid variable declaration")
                var_name = tokens[1]
                value = self.evaluate_expression(tokens, 3)
                self.variables[var_name] = value
            
            # Variable assignment
            elif len(tokens) >= 3 and tokens[1] in ['=', '+=', '-=', '*=', '/=']:
                var_name = tokens[0]
                if var_name not in self.variables:
                    raise TourmalineError(f"Variable '{var_name}' not declared")
                
                op = tokens[1]
                value = self.evaluate_expression(tokens, 2)
                
                if op == '=':
                    self.variables[var_name] = value
                elif op == '+=':
                    self.variables[var_name] += value
                elif op == '-=':
                    self.variables[var_name] -= value
                elif op == '*=':
                    self.variables[var_name] *= value
                elif op == '/=':
                    self.variables[var_name] /= value
            
            # Function definition
            elif tokens[0] == 'function':
                func_name = tokens[1]
                # Find end of function
                func_lines = [line]
                i += 1
                depth = 1
                while i < len(lines) and depth > 0:
                    l = lines[i].strip()
                    func_lines.append(lines[i])
                    if l.startswith('function') or l.startswith('if') or l.startswith('while') or l.startswith('for'):
                        depth += 1
                    elif l == 'end':
                        depth -= 1
                    i += 1
                
                self.functions[func_name] = func_lines
                continue
            
            # Struct definition
            elif tokens[0] == 'struct':
                struct_name = tokens[1]
                struct_fields = []
                i += 1
                while i < len(lines):
                    l = lines[i].strip()
                    if l == 'end':
                        break
                    if l and not l.startswith('#'):
                        struct_fields.append(l)
                    i += 1
                
                self.structs[struct_name] = struct_fields
            
            # Try-except block
            elif tokens[0] == 'try':
                try_lines = []
                except_lines = []
                exception_var = None
                
                i += 1
                depth = 1
                in_except = False
                
                while i < len(lines) and depth > 0:
                    l = lines[i].strip()
                    
                    if l.startswith('try') or l.startswith('if') or l.startswith('while') or l.startswith('for') or l.startswith('function'):
                        depth += 1
                        if in_except:
                            except_lines.append(lines[i])
                        else:
                            try_lines.append(lines[i])
                    elif l == 'end':
                        depth -= 1
                        if depth > 0:
                            if in_except:
                                except_lines.append(lines[i])
                            else:
                                try_lines.append(lines[i])
                    elif l.startswith('except') and depth == 1:
                        in_except = True
                        # Parse exception variable if present
                        except_tokens = self.tokenize(l)
                        if len(except_tokens) > 1:
                            exception_var = except_tokens[1]
                    else:
                        if in_except:
                            except_lines.append(lines[i])
                        else:
                            try_lines.append(lines[i])
                    
                    i += 1
                
                # Execute try block
                try:
                    self.execute('\n'.join(try_lines))
                except (TourmalineError, Exception) as e:
                    # Store exception in variable if specified
                    if exception_var:
                        self.variables[exception_var] = str(e)
                    # Execute except block
                    if except_lines:
                        self.execute('\n'.join(except_lines))
                
                continue
            
            # If statement
            elif tokens[0] == 'if':
                condition = self.evaluate_expression(tokens, 1)
                if_lines = []
                elif_blocks = []
                else_lines = []
                
                i += 1
                depth = 1
                current_block = if_lines
                
                while i < len(lines) and depth > 0:
                    l = lines[i].strip()
                    
                    if l.startswith('if') or l.startswith('while') or l.startswith('for') or l.startswith('function'):
                        depth += 1
                        current_block.append(lines[i])
                    elif l == 'end':
                        depth -= 1
                        if depth > 0:
                            current_block.append(lines[i])
                    elif l.startswith('elif') and depth == 1:
                        elif_tokens = self.tokenize(l)
                        elif_condition = self.evaluate_expression(elif_tokens, 1)
                        elif_blocks.append((elif_condition, []))
                        current_block = elif_blocks[-1][1]
                    elif l == 'else' and depth == 1:
                        current_block = else_lines
                    else:
                        current_block.append(lines[i])
                    
                    i += 1
                
                if condition:
                    self.execute('\n'.join(if_lines))
                else:
                    executed = False
                    for elif_cond, elif_lines_block in elif_blocks:
                        if elif_cond:
                            self.execute('\n'.join(elif_lines_block))
                            executed = True
                            break
                    if not executed and else_lines:
                        self.execute('\n'.join(else_lines))
                
                continue
            
            # While loop
            elif tokens[0] == 'while':
                condition_tokens = tokens[1:]
                loop_lines = []
                i += 1
                depth = 1
                
                while i < len(lines) and depth > 0:
                    l = lines[i].strip()
                    if l.startswith('while') or l.startswith('for') or l.startswith('if') or l.startswith('function'):
                        depth += 1
                    elif l == 'end':
                        depth -= 1
                    
                    if depth > 0:
                        loop_lines.append(lines[i])
                    i += 1
                
                while self.evaluate_expression(condition_tokens):
                    self.execute('\n'.join(loop_lines))
                
                continue
            
            # For loop
            elif tokens[0] == 'for':
                var_name = tokens[1]
                if tokens[2] != 'in':
                    raise TourmalineError("Expected 'in' in for loop")
                
                iterable = self.evaluate_expression(tokens, 3)
                loop_lines = []
                i += 1
                depth = 1
                
                while i < len(lines) and depth > 0:
                    l = lines[i].strip()
                    if l.startswith('for') or l.startswith('while') or l.startswith('if') or l.startswith('function'):
                        depth += 1
                    elif l == 'end':
                        depth -= 1
                    
                    if depth > 0:
                        loop_lines.append(lines[i])
                    i += 1
                
                for item in iterable:
                    if self.has_returned:
                        break
                    self.variables[var_name] = item
                    self.execute('\n'.join(loop_lines))
                
                continue
            
            # Return statement
            elif tokens[0] == 'return':
                if len(tokens) > 1:
                    self.return_value = self.evaluate_expression(tokens, 1)
                else:
                    self.return_value = None
                self.has_returned = True
                return
            
            # Function call or expression
            else:
                try:
                    self.evaluate_expression(tokens)
                except Exception as e:
                    # Silent errors for expressions that don't return values
                    pass
            
            i += 1

# Example usage and REPL
if __name__ == "__main__":
    import sys
    
    interpreter = TourmalineInterpreter()
    
    # Check if a file is provided as argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not filename.endswith('.trm'):
            print(f"Error: File must have .trm extension")
            sys.exit(1)
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            interpreter.execute(code)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            sys.exit(1)
        except TourmalineError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
    else:
        # Interactive mode
        print("Tourmaline Language Interpreter v0.5.1 - Sunny Road")
        print("Type 'exit' to quit")
        print("Usage: python interpreter.py <file.trm> to run a file")
        print()
        
        example_code = '''# Tourmaline Example Code
let name = "World"
print("Hello, " + name + "!\\n")

# Type conversions
let str_num = "42"
let num = int(str_num)
print("String to int: " + str(num))

let str_float = "3.14"
let pi = float(str_float)
print("String to float: " + str(pi))

let int_val = 100
let float_val = float(int_val)
print("Int to float: " + str(float_val))

# Exception handling
try
    let bad_conversion = int("not a number")
    print("This won't print")
except error
    print("Caught error: " + error)
end

print("Program continues after error!")
'''
        
        print("Running example code:")
        print("-" * 50)
        try:
            interpreter.execute(example_code)
        except Exception as e:
            print(f"Error: {e}")
        
        print("\n" + "-" * 50)
        print("Interactive mode (type 'exit' to quit):")
        
        while True:
            try:
                code = input(">>> ")
                if code.strip().lower() == 'exit':
                    break
                if code.strip():
                    interpreter.execute(code)
            except TourmalineError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")