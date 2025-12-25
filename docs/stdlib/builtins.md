# Built-in Functions

Tourmaline includes a set of built-in functions that are always available without importing.

## Input/Output Functions

### `print()`

Output text to the console.

**Syntax:**
```python
print(value1, value2, ...)
```

**Parameters:**
- Any number of values to print

**Examples:**
```python
print("Hello, World!")
print("Score:", 95)
print("Values:", 1, 2, 3)

let name = "Alice"
print("Welcome, " + name + "!")
```

**Output:**
```
Hello, World!
Score: 95
Values: 1 2 3
Welcome, Alice!
```

---

### `input()`

Get input from the user.

**Syntax:**
```python
input(prompt)
```

**Parameters:**
- `prompt` (optional): Text to display to the user

**Returns:** String containing user input

**Examples:**
```python
let name = input("What is your name? ")
print("Hello, " + name + "!")

let age_str = input("Enter your age: ")
let age = int(age_str)
print("You are " + str(age) + " years old")
```

!!! tip
    `input()` always returns a string. Use `int()` or `float()` to convert to numbers.

---

## Type Conversion Functions

### `str()`

Convert any value to a string.

**Syntax:**
```python
str(value)
```

**Examples:**
```python
let num = 42
let text = str(num)
print("Number: " + text)  # Number: 42

let flag = true
print("Status: " + str(flag))  # Status: true

let items = [1, 2, 3]
print(str(items))  # [1, 2, 3]
```

---

### `int()`

Convert a value to an integer.

**Syntax:**
```python
int(value)
```

**Parameters:**
- `value`: String, float, or boolean to convert

**Returns:** Integer value

**Examples:**
```python
# String to int
let num = int("42")
print(num + 10)  # 52

# Float to int (truncates)
let decimal = int(9.8)
print(decimal)  # 9

# String with decimal to int
let value = int("42.7")
print(value)  # 42

# Boolean to int
print(int(true))   # 1
print(int(false))  # 0
```

**Error Handling:**
```python
try
    let bad = int("not a number")
except error
    print("Conversion failed")
end
```

---

### `float()`

Convert a value to a float.

**Syntax:**
```python
float(value)
```

**Parameters:**
- `value`: String, integer, or boolean to convert

**Returns:** Float value

**Examples:**
```python
# String to float
let num = float("3.14")
print(num)  # 3.14

# Int to float
let whole = float(10)
print(whole)  # 10.0

# Boolean to float
print(float(true))   # 1.0
print(float(false))  # 0.0
```

---

### `type()`

Get the type of a value.

**Syntax:**
```python
type(value)
```

**Returns:** String describing the type

**Examples:**
```python
print(type(42))          # int
print(type(3.14))        # float
print(type("hello"))     # str
print(type(true))        # bool
print(type([1, 2, 3]))   # list
print(type({"a": 1}))    # dict
print(type(nil))         # NoneType
```

---

## Utility Functions

### `len()`

Get the length of a collection.

**Syntax:**
```python
len(collection)
```

**Parameters:**
- `collection`: List, string, or dictionary

**Returns:** Integer length

**Examples:**
```python
# List length
let numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

# String length
let text = "Hello"
print(len(text))  # 5

# Dictionary length
let person = {"name": "Alice", "age": 30}
print(len(person))  # 2

# Empty collections
print(len([]))   # 0
print(len(""))   # 0
```

---

## Comparison Functions

### `min()`

Find the minimum value.

**Syntax:**
```python
min(value1, value2, ...)
```

**Parameters:**
- Two or more values to compare

**Returns:** The smallest value

**Examples:**
```python
print(min(5, 3, 9, 1))     # 1
print(min(10, 20))         # 10
print(min(-5, -10, -3))    # -10

let a = 15
let b = 8
let smallest = min(a, b)
print(smallest)  # 8
```

---

### `max()`

Find the maximum value.

**Syntax:**
```python
max(value1, value2, ...)
```

**Parameters:**
- Two or more values to compare

**Returns:** The largest value

**Examples:**
```python
print(max(5, 3, 9, 1))     # 9
print(max(10, 20))         # 20
print(max(-5, -10, -3))    # -3

let a = 15
let b = 8
let largest = max(a, b)
print(largest)  # 15
```

---

## Quick Reference Table

| Function | Purpose | Example | Result |
|----------|---------|---------|--------|
| `print()` | Output to console | `print("Hi")` | Displays: Hi |
| `input()` | Get user input | `input("Name: ")` | Returns string |
| `str()` | Convert to string | `str(42)` | "42" |
| `int()` | Convert to integer | `int("42")` | 42 |
| `float()` | Convert to float | `float("3.14")` | 3.14 |
| `type()` | Get value type | `type(42)` | "int" |
| `len()` | Get length | `len([1,2,3])` | 3 |
| `min()` | Find minimum | `min(1,2,3)` | 1 |
| `max()` | Find maximum | `max(1,2,3)` | 3 |

## Practical Examples

### Input Validation

```python
function get_valid_age()
    while true
        let age_str = input("Enter your age: ")
        
        try
            let age = int(age_str)
            if age >= 0 and age <= 120
                return age
            else
                print("Age must be between 0 and 120")
            end
        except error
            print("Please enter a valid number")
        end
    end
end

let user_age = get_valid_age()
print("Your age is: " + str(user_age))
```

### Type Checking

```python
function describe_value(value)
    let value_type = type(value)
    
    if value_type == "int" or value_type == "float"
        print("It's a number: " + str(value))
    elif value_type == "str"
        print("It's text with length: " + str(len(value)))
    elif value_type == "list"
        print("It's a list with " + str(len(value)) + " items")
    elif value_type == "bool"
        print("It's a boolean: " + str(value))
    else
        print("It's a " + value_type)
    end
end

describe_value(42)
describe_value("Hello")
describe_value([1, 2, 3])
describe_value(true)
```

### Range Finder

```python
function find_range(numbers)
    if len(numbers) == 0
        print("List is empty")
        return nil
    end
    
    let minimum = numbers[0]
    let maximum = numbers[0]
    
    for num in numbers
        minimum = min(minimum, num)
        maximum = max(maximum, num)
    end
    
    let range = maximum - minimum
    
    print("Minimum: " + str(minimum))
    print("Maximum: " + str(maximum))
    print("Range: " + str(range))
    
    return range
end

let data = [23, 45, 12, 67, 34, 89, 15]
find_range(data)
```

### Data Formatter

```python
function format_table_row(values)
    let row = ""
    for value in values
        # Convert everything to string and pad
        let str_val = str(value)
        let padding = 15 - len(str_val)
        
        row = row + str_val
        
        let i = 0
        while i < padding
            row = row + " "
            i += 1
        end
    end
    
    print(row)
end

print("Name           Age            City")
print("-" + "-" + "-" + "-" + "-" + "-" + "-" + "-")
format_table_row(["Alice", 30, "NYC"])
format_table_row(["Bob", 25, "LA"])
format_table_row(["Charlie", 35, "Chicago"])
```

## Notes

!!! note "String Conversion"
    When using `print()` with the `+` operator, always convert non-strings with `str()`:
    
    ```python
    let age = 25
    print("Age: " + str(age))  # Correct
    # print("Age: " + age)     # Error!
    ```

!!! tip "Input Conversion"
    Remember that `input()` always returns a string:
    
    ```python
    let num = input("Enter number: ")  # String
    let number = int(num)              # Convert to integer
    ```

!!! warning "Type Errors"
    Attempting invalid conversions will raise errors:
    
    ```python
    try
        let x = int("hello")  # Error!
    except error
        print("Cannot convert 'hello' to int")
    end
    ```

## Next Steps

- **[Math Functions](math.md)** - Mathematical operations
- **[List Operations](lists.md)** - Working with lists
- **[Random Library](random.md)** - Generate random values