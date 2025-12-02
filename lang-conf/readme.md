# Tourmaline Language Support

Visual Studio Code extension providing comprehensive language support for Tourmaline (`.toma`) files.

## Features

### 🎨 Syntax Highlighting
Full syntax highlighting support for all Tourmaline language features:
- Keywords (`if`, `elif`, `else`, `while`, `for`, `func`, `let`, `return`, etc.)
- Operators (arithmetic, comparison, assignment, range)
- Data types (`int`, `str`, `bool`, `list`)
- String literals with escape sequences
- Numeric literals (integers and floats)
- Boolean constants (`true`, `false`)
- Comments (`#`)
- Function definitions and calls
- Variables and type annotations

### 📝 Code Snippets
25+ snippets to speed up your Tourmaline development:

#### Variables & Print
- `print` → Print statement
- `let` → Variable declaration
- `lett` → Typed variable declaration

#### Control Flow
- `if` → If statement
- `ife` → If-else statement
- `ifel` → If-elif-else statement
- `while` → While loop
- `for` → For range loop

#### Functions
- `func` → Function declaration
- `funct` → Function with typed parameters
- `ret` → Return statement

#### Data Structures
- `list` → List literal
- `idx` → List element access
- `range` → Range expression

#### Modules
- `import` → Import statement
- `module` → Module declaration

#### Operators & Comparisons
- `eq` → Equality comparison (`==`)
- `neq` → Not equal comparison (`!=`)
- `gt` → Greater than (`>`)
- `lt` → Less than (`<`)

### 🔧 Smart Editor Features
- **Auto-closing pairs** for brackets, quotes, and parentheses
- **Auto-indentation** after control structures
- **Code folding** between control structures and `end` keywords
- **Comment toggling** with `Ctrl+/` (or `Cmd+/` on Mac)

## Installation

### From VSIX
1. Download the `.vsix` file
2. Open VS Code
3. Go to Extensions (Ctrl+Shift+X)
4. Click "..." menu → "Install from VSIX..."
5. Select the downloaded file

### From Source
1. Clone this repository
2. Open the folder in VS Code
3. Press `F5` to launch Extension Development Host

## Usage

### Quick Start

Create a new file with `.toma` extension and start coding!

```tourmaline
# Simple Tourmaline program
let name = "World"
print "Hello, " + name

if name == "World"
    print "Welcome!"
else
    print "Hi there!"
end
```

### Using Snippets

Type a snippet prefix and press `Tab` or `Enter`:

1. Type `for` → Press `Tab`
2. Fill in the loop variable
3. Press `Tab` to move to start value
4. Continue tabbing through placeholders

### Example: Function with Snippets

```tourmaline
# Type 'func' and press Tab
func add(a: int, b: int)
    let result = a + b
    return result
end

# Type 'let' and press Tab
let sum = add(5, 3)
print sum
```

## Language Features

### Variables
```tourmaline
let x = 10
let name: str = "Alice"
let items = [1, 2, 3, 4]
```

### Control Flow
```tourmaline
# If-elif-else
if x > 10
    print "big"
elif x == 10
    print "exactly 10"
else
    print "small"
end

# While loop
while x < 20
    print x
    x = x + 1
end

# For loop
for i in 0..5
    print i
end
```

### Functions
```tourmaline
func greet(name: str)
    print "Hello, " + name
    return true
end

let result = greet("Bob")
```

### Lists
```tourmaline
let mylist = [1, 2, 3, 4]
print mylist[0]  # Prints: 1

for i in 0..3
    print mylist[i]
end
```

### Operators
- **Arithmetic**: `+`, `-`, `*`, `/`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Range**: `..` (inclusive range)

## Keyboard Shortcuts

| Command | Windows/Linux | macOS |
|---------|--------------|-------|
| Toggle Comment | `Ctrl+/` | `Cmd+/` |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Go to Definition | `F12` | `F12` |

## Known Issues

Please report issues on the [GitHub repository](https://github.com/yourusername/tourmaline-vscode).

## Release Notes

### 0.1.0

Initial release:
- Comprehensive syntax highlighting
- 25+ code snippets
- Auto-indentation and folding
- Comment toggling support

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## About Tourmaline

Tourmaline is a simple, readable programming language with:
- Clean, Python, Lua and Ruby-inspired syntax
- Strong type annotations
- List data structures
- Module system

Perfect for learning programming concepts or building small scripts!

---

**Enjoy coding in Tourmaline!** 💎