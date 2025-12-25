# Variables & Data Types

Learn how to store and work with data in Tourmaline.

## Variable Declaration

In Tourmaline, all variables must be declared using the `let` keyword:

```python
let message = "Hello"
let count = 42
let price = 19.99
```

!!! warning
    You cannot use a variable before declaring it with `let`. This will cause an error:
    
    ```python
    name = "Alice"  # Error! Must use 'let' first
    ```

## Data Types

Tourmaline supports several fundamental data types:

### Integer

Whole numbers without decimal points:

```python
let age = 25
let year = 2024
let negative = -10
let zero = 0
```

### Float

Numbers with decimal points:

```python
let pi = 3.14159
let temperature = 23.5
let price = 99.99
let small = 0.001
```

### String

Text enclosed in single or double quotes:

```python
let name = "Alice"
let greeting = 'Hello, World!'
let empty = ""
```

**String Concatenation:**

```python
let first = "John"
let last = "Doe"
let full_name = first + " " + last
print(full_name)  # John Doe
```

**Special Characters:**

```python
let multiline = "Line 1\nLine 2"  # \n for newline
let tabbed = "Name:\tValue"        # \t for tab
```

### Boolean

True or false values:

```python
let is_active = true
let is_complete = false
let has_access = true
```

Booleans are used in conditions:

```python
let is_adult = true

if is_adult
    print("Access granted")
end
```

### Nil

Represents the absence of a value:

```python
let nothing = nil
let unset = nil
```

Check for nil:

```python
let value = nil

if value == nil
    print("Value is nil")
end
```

### Lists

Ordered collections of items:

```python
let numbers = [1, 2, 3, 4, 5]
let fruits = ["apple", "banana", "cherry"]
let mixed = [1, "hello", true, 3.14]
let empty_list = []
```

### Dictionaries

Key-value pairs:

```python
let person = {
    "name": "Alice",
    "age": 30,
    "email": "alice@example.com"
}

let config = {
    "debug": true,
    "port": 8080,
    "host": "localhost"
}
```

## Type Checking

Use the `type()` function to check a variable's type:

```python
let x = 42
print(type(x))  # int

let name = "Alice"
print(type(name))  # str

let items = [1, 2, 3]
print(type(items))  # list
```

## Type Conversion

### String Conversions

Convert any value to a string with `str()`:

```python
let num = 42
let text = str(num)
print("Number: " + text)

let flag = true
print("Status: " + str(flag))
```

### Integer Conversions

Convert to integer with `int()`:

```python
# From string
let num_str = "123"
let num = int(num_str)
print(num + 10)  # 133

# From float (truncates decimal)
let decimal = 9.8
let whole = int(decimal)
print(whole)  # 9

# From boolean
let flag = true
print(int(flag))  # 1
```

!!! tip
    `int()` can convert strings that contain floats:
    
    ```python
    let value = int("42.7")  # Converts to 42
    ```

### Float Conversions

Convert to float with `float()`:

```python
# From string
let num_str = "3.14"
let num = float(num_str)
print(num * 2)  # 6.28

# From integer
let whole = 10
let decimal = float(whole)
print(decimal)  # 10.0

# From boolean
let flag = true
print(float(flag))  # 1.0
```

### Conversion Error Handling

Invalid conversions raise errors. Use exception handling:

```python
try
    let bad_num = int("not a number")
except error
    print("Conversion failed: " + error)
end
```

## Variable Assignment

### Simple Assignment

```python
let x = 10
x = 20  # Update existing variable
```

!!! note
    After declaring with `let`, use the variable name alone for updates

### Compound Assignment

Shorthand operators for common operations:

```python
let counter = 10

counter += 5   # Same as: counter = counter + 5
counter -= 3   # Same as: counter = counter - 3
counter *= 2   # Same as: counter = counter * 2
counter /= 4   # Same as: counter = counter / 4
```

**Examples:**

```python
let score = 100

score += 50     # score is now 150
score -= 20     # score is now 130
score *= 2      # score is now 260
score /= 10     # score is now 26
```

## Variable Scope

Variables declared inside functions are local:

```python
let global_var = "I'm global"

function my_function()
    let local_var = "I'm local"
    print(local_var)      # Works
    print(global_var)     # Also works
end

my_function()
# print(local_var)  # Error! local_var doesn't exist here
```

## Naming Conventions

**Valid variable names:**

- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Are case-sensitive

```python
let userName = "Alice"      # Valid
let user_name = "Bob"       # Valid
let _private = "secret"     # Valid
let user123 = "Charlie"     # Valid
```

**Invalid variable names:**

```python
let 123user = "Invalid"     # Error! Starts with number
let user-name = "Invalid"   # Error! Contains hyphen
let user name = "Invalid"   # Error! Contains space
```

**Best Practices:**

```python
# Use descriptive names
let user_age = 25           # Good
let x = 25                  # Less clear

# Use snake_case for multi-word names
let first_name = "John"     # Recommended
let firstName = "John"      # Also works

# Use meaningful names
let total_price = 99.99     # Clear
let tp = 99.99              # Unclear
```

## Constants

Tourmaline doesn't have built-in constants, but by convention, use UPPERCASE names:

```python
let MAX_USERS = 100
let PI = 3.14159
let API_KEY = "secret123"
```

!!! warning
    This is just a naming convention. The values can still be changed.

## Examples

### Working with Multiple Variables

```python
# Declare multiple variables
let name = "Alice"
let age = 30
let salary = 50000.0
let is_employee = true

# Use them together
print("Employee: " + name)
print("Age: " + str(age))
print("Salary: $" + str(salary))
print("Active: " + str(is_employee))
```

### Type Conversions in Practice

```python
# Calculator example
let num1 = input("Enter first number: ")
let num2 = input("Enter second number: ")

# Convert strings to floats
let a = float(num1)
let b = float(num2)

let sum = a + b
let product = a * b

print("Sum: " + str(sum))
print("Product: " + str(product))
```

### Dynamic Typing

```python
# Variables can change type
let value = 42          # Integer
print(type(value))      # int

value = "Hello"         # Now a string
print(type(value))      # str

value = [1, 2, 3]       # Now a list
print(type(value))      # list
```

!!! tip
    While Tourmaline allows changing types, it's good practice to keep variables consistently typed

## Next Steps

- **[Learn about Operators](operators.md)** - Manipulate your variables
- **[Control Flow](control-flow.md)** - Make decisions with your data
- **[Lists & Dictionaries](collections.md)** - Work with complex data structures