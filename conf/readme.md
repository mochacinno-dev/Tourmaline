# Tourmaline Language Support for VS Code

![Version](https://img.shields.io/badge/version-1.0.0-pink)
![Tourmaline](https://img.shields.io/badge/Tourmaline-Tourmal%20Waters-blue)

Visual Studio Code extension providing comprehensive language support for **Tourmaline** (`.trm`) files - a simple, easy to learn programming language with beautiful syntax inspired by Lua and Ruby.

## Features

✨ **Syntax Highlighting**
- Complete syntax highlighting for all Tourmaline constructs
- Keywords: `let`, `if`, `elif`, `else`, `while`, `for`, `in`, `function`, `struct`, `end`
- Logical operators: `and`, `or`, `not`
- Built-in functions: `print`, `input`, `str`, `int`, `float`, `len`, `sqrt`, `pow`, `abs`, `min`, `max`, `floor`, `ceil`, `round`, `sin`, `cos`, `tan`
- Constants: `true`, `false`, `nil`
- String escape sequences: `\n`, `\t`

🎯 **IntelliSense & Snippets**
- 40+ code snippets for rapid development
- Auto-completion for keywords and built-in functions
- Smart bracket matching and auto-closing
- Automatic indentation


📦 **Code Folding**
- Fold `if`, `while`, `for`, `function`, and `struct` blocks
- Clean code organization

## Supported Language Features

### Data Types
- **Integers**: `42`, `-10`
- **Floats**: `3.14`, `-0.5`
- **Strings**: `"Hello"`, `'World'`
- **Booleans**: `true`, `false`
- **Nil**: `nil`
- **Lists**: `[1, 2, 3]`
- **Dictionaries**: `{"key": "value"}`

### Control Flow
```tourmaline
# If statements
if score >= 90
    print("Grade A")
elif score >= 80
    print("Grade B")
else
    print("Grade C")
end

# While loops
while counter < 10
    counter += 1
end

# For loops
for item in collection
    print(item)
end
```

### Functions
```tourmaline
function greet(name)
    print("Hello, " + name + "!")
end

greet("World")
```

### Structs
```tourmaline
struct Person
    name
    age
end
```

## Snippet Examples

Type these prefixes and press Tab:

- `print` → `print(value)`
- `let` → `let name = value`
- `if` → If statement block
- `ife` → If-else block
- `ifel` → If-elif-else block
- `while` → While loop block
- `for` → For-in loop block
- `function` → Function declaration
- `struct` → Struct declaration
- `list` → `[elements]`
- `dict` → `{"key": value}`
- `hello` → Hello World template
- `main` → Main program template

## Installation

### From VSIX (Recommended)
1. Download the `.vsix` file from the releases
2. Open VS Code
3. Press `Ctrl+Shift+P` / `Cmd+Shift+P`
4. Type "Install from VSIX"
5. Select the downloaded file

### From Source
1. Clone the repository
2. Copy the extension folder to:
   - **Windows**: `%USERPROFILE%\.vscode\extensions`
   - **macOS/Linux**: `~/.vscode/extensions`
3. Restart VS Code

## Usage

1. Create a new file with `.trm` extension
2. Start typing Tourmaline code
3. Use `Ctrl+Space` for auto-completion
4. Run your code: `python tourmaline.py yourfile.trm`

## Examples

### Hello World
```tourmaline
let name = "World"
print("Hello, " + name + "!")
```

### FizzBuzz
```tourmaline
let i = 1
while i <= 100
    if i % 15 == 0
        print("FizzBuzz")
    elif i % 3 == 0
        print("Fizz")
    elif i % 5 == 0
        print("Buzz")
    else
        print(str(i))
    end
    i += 1
end
```

### Functions and Lists
```tourmaline
function sum_list(numbers)
    let total = 0
    for num in numbers
        total += num
    end
    print("Sum: " + str(total))
end

let nums = [1, 2, 3, 4, 5]
sum_list(nums)
```

## Tourmaline Language

Tourmaline is a simple, easy to learn programming language designed for education and scripting. It features:

- Clean, readable syntax inspired by Lua and Ruby
- Dynamic typing with integers, floats, strings, booleans, lists, and dictionaries
- Control flow with if/elif/else, while, and for loops
- First-class functions
- Struct definitions
- Rich set of built-in math functions
- Easy string manipulation

### Version: 0.6.0 - Green Valley

## Requirements

- Visual Studio Code 1.50.0 or higher
- Python 3.6+ (to run Tourmaline code)

## Contributing

Contributions are welcome! Please visit the [GitHub repository](https://github.com/mochacinno-dev/Tourmaline) to report issues or submit pull requests.

## Release Notes

### 1.0.0 - Tourmal Waters
- Full syntax highlighting support
- 40+ code snippets
- Auto-completion and IntelliSense
- Code folding support
- Support for all language features:
  - Variables with `let`
  - Functions with parameters
  - Structs
  - Lists and dictionaries
  - All operators (arithmetic, comparison, logical, compound assignment)
  - All built-in functions

## License

GNU General Public License v3.0 - Made by **The Mocha Foundation**

---

**Enjoy coding with Tourmaline!**