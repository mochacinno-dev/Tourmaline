# Syntax Reference

Complete syntax reference for the Tourmaline programming language.

## Comments

```python
# This is a single-line comment

let x = 10  # Comments can appear at the end of lines

# Multiple lines require multiple # symbols
# Like this
# And this
```

## Variables

### Declaration

```python
let variable_name = value
```

### Assignment

```python
variable_name = new_value
```

### Compound Assignment

```python
variable += value   # Addition
variable -= value   # Subtraction
variable *= value   # Multiplication
variable /= value   # Division
```

## Data Types

### Literals

```python
42              # Integer
3.14            # Float
"text"          # String (double quotes)
'text'          # String (single quotes)
true            # Boolean true
false           # Boolean false
nil             # Null/None value
[1, 2, 3]       # List
{"key": "val"}  # Dictionary
```

## Operators

### Arithmetic

```python
+   # Addition
-   # Subtraction
*   # Multiplication
/   # Division
%   # Modulo (remainder)
```

### Comparison

```python
==  # Equal to
!=  # Not equal to
<   # Less than
>   # Greater than
<=  # Less than or equal to
>=  # Greater than or equal to
```

### Logical

```python
and  # Logical AND
or   # Logical OR
```

## Control Flow

### If Statement

```python
if condition
    # code
end
```

### If-Elif-Else

```python
if condition1
    # code
elif condition2
    # code
elif condition3
    # code
else
    # code
end
```

### While Loop

```python
while condition
    # code
end
```

### For Loop

```python
for variable in iterable
    # code
end
```

## Functions

### Function Definition

```python
function name(param1, param2)
    # code
    return value
end
```

### Function Call

```python
name(arg1, arg2)
```

### Function Without Parameters

```python
function name()
    # code
end
```

### Function Without Return

```python
function name()
    # code
end  # Returns nil
```

## Collections

### Lists

```python
# Creation
let list = [item1, item2, item3]

# Empty list
let empty = []

# Access
let item = list[index]

# Modification
list[index] = new_value
```

### Dictionaries

```python
# Creation
let dict = {
    "key1": value1,
    "key2": value2
}

# Empty dictionary
let empty = {}

# Access
let value = dict["key"]

# Access with dot notation (for library functions)
library.function()
```

## Exception Handling

### Try-Except

```python
try
    # code that might fail
except
    # error handling
end
```

### Try-Except with Variable

```python
try
    # code that might fail
except error_variable
    # error handling using error_variable
end
```

## Imports

```python
import library_name
```

### Using Imported Libraries

```python
import random

let num = random.randint(1, 10)
```

## Keywords

Reserved words in Tourmaline:

- `let` - Variable declaration
- `function` - Function definition
- `return` - Return from function
- `if` - Conditional statement
- `elif` - Else if
- `else` - Else clause
- `while` - While loop
- `for` - For loop
- `in` - For loop iterator
- `end` - Block terminator
- `try` - Exception handling
- `except` - Exception handler
- `import` - Import library
- `true` - Boolean true
- `false` - Boolean false
- `nil` - Null value
- `and` - Logical AND
- `or` - Logical OR

## Whitespace & Indentation

Tourmaline uses `end` keywords instead of indentation:

```python
# Indentation is optional but recommended for readability
if condition
    print("True")    # Indented (recommended)
end

if condition
print("True")        # Not indented (works but less readable)
end
```

## Naming Rules

### Valid Identifiers

- Must start with a letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers, and underscores
- Case-sensitive
- Cannot be a keyword

```python
# Valid
let userName = "Alice"
let user_name = "Bob"
let _private = "secret"
let user123 = "Charlie"

# Invalid
let 123user = "Invalid"    # Starts with number
let user-name = "Invalid"  # Contains hyphen
let user name = "Invalid"  # Contains space
let let = "Invalid"        # Keyword
```

## String Escape Sequences

```python
\n  # Newline
\t  # Tab
\"  # Double quote
\'  # Single quote
\\  # Backslash
```

**Example:**

```python
let text = "Line 1\nLine 2\tTabbed"
print(text)
# Output:
# Line 1
# Line 2    Tabbed
```

## Precedence Rules

Operations are evaluated in this order (highest to lowest):

1. Parentheses `()`
2. Function calls `function()`
3. Member access `.`
4. Index access `[]`
5. Multiplication `*`, Division `/`, Modulo `%`
6. Addition `+`, Subtraction `-`
7. Comparison `<`, `>`, `<=`, `>=`
8. Equality `==`, `!=`
9. Logical AND `and`
10. Logical OR `or`

**Examples:**

```python
let result = 2 + 3 * 4      # 14 (multiplication first)
let result = (2 + 3) * 4    # 20 (parentheses first)
let result = 10 > 5 and 3 < 7   # true (comparison before and)
```

## File Extensions

Tourmaline recognizes three file extensions:

- `.trm` - Standard Tourmaline files
- `.tli` - Tourmaline Language Interpreter files
- `.tour` - Alternative extension

All extensions work identically.

## Program Structure

A typical Tourmaline program:

```python
########################
# Program Description
# Author: Name
########################

# Imports (if needed)
import random

# Global variables
let global_var = "value"

# Function definitions
function helper_function(param)
    # Function code
    return result
end

# Main program code
let data = [1, 2, 3, 4, 5]

for item in data
    print(item)
end
```

## Complete Example

```python
########################
# Calculator Program
########################

# Function to add two numbers
function add(a, b)
    return a + b
end

# Function to get valid number
function get_number(prompt)
    while true
        let input_str = input(prompt)
        try
            let num = float(input_str)
            return num
        except error
            print("Please enter a valid number")
        end
    end
end

# Main program
print("=== Simple Calculator ===")

let num1 = get_number("Enter first number: ")
let num2 = get_number("Enter second number: ")

let sum = add(num1, num2)
let difference = num1 - num2
let product = num1 * num2

print("\nResults:")
print("Sum: " + str(sum))
print("Difference: " + str(difference))
print("Product: " + str(product))

if num2 != 0
    let quotient = num1 / num2
    print("Quotient: " + str(quotient))
else
    print("Cannot divide by zero")
end
```

## Style Guidelines

### Recommended Conventions

**Variable Naming:**
```python
let user_name = "Alice"     # snake_case (recommended)
let userName = "Bob"        # camelCase (also acceptable)
let MAX_SIZE = 100          # UPPERCASE for constants
```

**Function Naming:**
```python
function calculate_total()  # snake_case (recommended)
function calculateTotal()   # camelCase (also acceptable)
```

**Indentation:**
```python
# Use 4 spaces (recommended)
if condition
    print("Indented with 4 spaces")
end

# Or 2 spaces (also acceptable)
if condition
  print("Indented with 2 spaces")
end
```

**Line Length:**
- Keep lines under 80-100 characters when possible
- Break long lines for readability

**Comments:**
```python
# Use comments to explain WHY, not WHAT
let tax_rate = 0.08  # State sales tax rate

# Not: let tax_rate = 0.08  # Tax rate is 0.08
```

## Common Patterns

### Input Validation Loop

```python
while true
    let value = input("Enter value: ")
    if validate(value)
        break
    end
    print("Invalid input, try again")
end
```

### Counter Loop

```python
let counter = 0
while counter < 10
    print(counter)
    counter += 1
end
```

### List Iteration

```python
for item in list
    process(item)
end
```

### Dictionary Iteration

```python
# Iterate over keys
let dict = {"a": 1, "b": 2, "c": 3}
# Note: Direct iteration not shown in examples
# Access with dict["key"]
```

## Error Messages

Common syntax errors and their meanings:

| Error | Cause | Solution |
|-------|-------|----------|
| `Undefined variable: x` | Using undeclared variable | Use `let x = value` first |
| `Expected 'end'` | Missing `end` keyword | Add `end` to close block |
| `Invalid variable declaration` | Wrong `let` syntax | Use `let name = value` |
| `Expected '('` | Missing parentheses | Add `()` for function call |
| `Cannot evaluate expression` | Invalid expression syntax | Check operators and values |

## Quick Reference Card

```python
# Variables
let name = value

# Output
print(value)

# Input
let x = input("prompt")

# Types
int(x), float(x), str(x)

# Conditionals
if cond
    code
elif cond
    code
else
    code
end

# Loops
while cond
    code
end

for var in list
    code
end

# Functions
function name(params)
    code
    return value
end

# Collections
let list = [1, 2, 3]
let dict = {"key": "value"}

# Exception Handling
try
    code
except error
    handler
end
```

---

For more detailed information on specific features, see:
- **[Variables & Types](../guide/variables.md)**
- **[Operators](../guide/operators.md)**
- **[Control Flow](../guide/control-flow.md)**
- **[Functions](../guide/functions.md)**