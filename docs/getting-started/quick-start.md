# Quick Start Guide

Get up and running with Tourmaline in minutes!

## Your First Line of Code

Open the Tourmaline REPL:

```bash
python Tourmaline.py
```

Try these commands:

```python
>>> print("Hello, World!")
Hello, World!

>>> let x = 42
>>> print(x)
42

>>> let name = "Alice"
>>> print("Hello, " + name + "!")
Hello, Alice!
```

## Basic Concepts

### Variables

Declare variables with `let`:

```python
let age = 25
let name = "Bob"
let price = 19.99
let is_active = true
let nothing = nil
```

### Printing Output

```python
print("Simple text")
print("Number: " + str(42))
print("Multiple", "arguments", "work", "too")
```

### Getting Input

```python
let user_name = input("Enter your name: ")
print("Hello, " + user_name + "!")
```

## Data Types

Tourmaline supports several data types:

| Type | Example | Description |
|------|---------|-------------|
| Integer | `42` | Whole numbers |
| Float | `3.14` | Decimal numbers |
| String | `"hello"` | Text in quotes |
| Boolean | `true`, `false` | True/false values |
| Nil | `nil` | Represents nothing |
| List | `[1, 2, 3]` | Ordered collection |
| Dictionary | `{"key": "value"}` | Key-value pairs |

## Basic Operations

### Arithmetic

```python
let a = 10
let b = 3

print(a + b)  # 13 - Addition
print(a - b)  # 7  - Subtraction
print(a * b)  # 30 - Multiplication
print(a / b)  # 3.333... - Division
print(a % b)  # 1  - Modulo (remainder)
```

### Comparisons

```python
let x = 5
let y = 10

print(x == y)  # false - Equal to
print(x != y)  # true  - Not equal to
print(x < y)   # true  - Less than
print(x > y)   # false - Greater than
print(x <= y)  # true  - Less than or equal
print(x >= y)  # false - Greater than or equal
```

### Logical Operators

```python
let is_sunny = true
let is_warm = false

print(is_sunny and is_warm)  # false - Both must be true
print(is_sunny or is_warm)   # true  - At least one must be true
```

## Control Flow

### If Statements

```python
let temperature = 25

if temperature > 30
    print("It's hot!")
elif temperature > 20
    print("It's pleasant!")
else
    print("It's cold!")
end
```

!!! tip
    Always end your `if` blocks with `end`

### While Loops

```python
let count = 1

while count <= 5
    print("Count: " + str(count))
    count += 1
end
```

### For Loops

```python
let fruits = ["apple", "banana", "cherry"]

for fruit in fruits
    print("I like " + fruit)
end
```

## Functions

Define reusable code with functions:

```python
function greet(name)
    print("Hello, " + name + "!")
end

greet("Alice")
greet("Bob")
```

Functions with return values:

```python
function add(x, y)
    return x + y
end

let result = add(5, 3)
print("5 + 3 = " + str(result))
```

## Working with Lists

```python
# Create a list
let numbers = [1, 2, 3, 4, 5]

# Access elements (0-indexed)
print(numbers[0])  # 1
print(numbers[2])  # 3

# Get list length
print(len(numbers))  # 5

# Add items
append(numbers, 6)
print(numbers)  # [1, 2, 3, 4, 5, 6]
```

## Working with Dictionaries

```python
# Create a dictionary
let person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Access values
print(person["name"])  # Alice
print(person["age"])   # 30
```

## Comments

```python
# This is a single-line comment

let x = 10  # Comments can go at the end of lines

# Use comments to explain your code
# Multiple comment lines are fine
```

## Quick Reference Card

```python
# Variables
let name = "value"

# Output
print("text")

# Input
let var = input("prompt")

# Conditionals
if condition
    # code
elif condition
    # code
else
    # code
end

# Loops
while condition
    # code
end

for item in list
    # code
end

# Functions
function name(param1, param2)
    # code
    return value
end

# Lists
let list = [1, 2, 3]

# Dictionaries
let dict = {"key": "value"}
```

## Try It Yourself!

Create a file called `practice.trm`:

```python
# Temperature Converter
print("=== Temperature Converter ===")

let celsius = input("Enter temperature in Celsius: ")
let c = float(celsius)
let fahrenheit = c * 9 / 5 + 32

print(str(c) + "°C = " + str(fahrenheit) + "°F")
```

Run it:

```bash
python Tourmaline.py practice.trm
```

## Next Steps

- **[Write Your First Program](first-program.md)** - Build a complete project
- **[Language Guide](../guide/variables.md)** - Deep dive into features
- **[Examples](../examples/basic.md)** - Learn from code samples

---

!!! note
    This guide covers the essentials. There's much more to explore in Tourmaline!