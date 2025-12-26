# Error Messages

Guide to common error messages in Tourmaline and how to fix them.

## Variable Errors

### Undefined Variable

**Error Message:**
```
Undefined variable: variable_name
```

**Cause:** Trying to use a variable that hasn't been declared with `let`.

**Examples:**
```python
# Wrong
print(name)  # name not declared

# Right
let name = "Alice"
print(name)
```

**Solution:** Always declare variables with `let` before using them.

---

### Invalid Variable Declaration

**Error Message:**
```
Invalid variable declaration
```

**Cause:** Incorrect `let` statement syntax.

**Examples:**
```python
# Wrong
let x  # Missing value
let = 5  # Missing variable name
x = 5  # Missing 'let' for first declaration

# Right
let x = 5
```

**Solution:** Use the format `let variable_name = value`.

---

## Function Errors

### Function Not Defined

**Error Message:**
```
Function 'function_name' not defined
```

**Cause:** Calling a function that doesn't exist.

**Examples:**
```python
# Wrong
my_function()  # Function doesn't exist

# Right
function my_function()
    print("Hello")
end

my_function()
```

**Solution:** Define the function before calling it, or check the spelling.

---

### Expected '('

**Error Message:**
```
Expected '('
```

**Cause:** Missing parentheses in function call or definition.

**Examples:**
```python
# Wrong
function greet name
    print(name)
end

# Wrong
print "Hello"

# Right
function greet(name)
    print(name)
end

print("Hello")
```

**Solution:** Always include parentheses for function calls and definitions.

---

### Expected 'end'

**Error Message:**
```
Expected 'end'
```

**Cause:** Missing `end` keyword to close a block.

**Examples:**
```python
# Wrong
function greet()
    print("Hello")
# Missing 'end'

# Wrong
if x > 5
    print("Big")
# Missing 'end'

# Right
function greet()
    print("Hello")
end

if x > 5
    print("Big")
end
```

**Solution:** Every function, if, while, and for block needs an `end` keyword.

---

## Type Errors

### Cannot Convert to Integer

**Error Message:**
```
Cannot convert 'value' to integer
```

**Cause:** Trying to convert a non-numeric string to an integer.

**Examples:**
```python
# Wrong
let num = int("hello")

# Right
try
    let num = int("hello")
except error
    print("Invalid number")
end

# Or with valid input
let num = int("42")
```

**Solution:** Validate input before conversion or use try-except blocks.

---

### Cannot Convert to Float

**Error Message:**
```
Cannot convert 'value' to float
```

**Cause:** Trying to convert a non-numeric string to a float.

**Examples:**
```python
# Wrong
let num = float("abc")

# Right
try
    let num = float("abc")
except error
    print("Invalid number")
end
```

**Solution:** Use try-except or validate input first.

---

## List Errors

### List Index Out of Range

**Error Message:**
```
Index out of range
```

**Cause:** Accessing a list index that doesn't exist.

**Examples:**
```python
let fruits = ["apple", "banana"]

# Wrong
print(fruits[5])  # Only indices 0-1 exist

# Right
if len(fruits) > 5
    print(fruits[5])
else
    print("Index too large")
end
```

**Solution:** Check list length before accessing indices.

---

### Item Not Found in List

**Error Message:**
```
Item 'value' not found in list
```

**Cause:** Trying to remove an item that doesn't exist.

**Examples:**
```python
let fruits = ["apple", "banana"]

# Wrong
remove(fruits, "cherry")  # cherry not in list

# Right
try
    remove(fruits, "cherry")
except error
    print("Item not found")
end
```

**Solution:** Check if item exists before removing, or use try-except.

---

### Cannot Pop from Empty List

**Error Message:**
```
Cannot pop from empty list
```

**Cause:** Trying to pop from a list with no items.

**Examples:**
```python
let items = []

# Wrong
let item = pop(items)

# Right
if len(items) > 0
    let item = pop(items)
else
    print("List is empty")
end
```

**Solution:** Check list length before popping.

---

## Dictionary Errors

### Key Not Found

**Error Message:**
```
Key 'key_name' not found
```

**Cause:** Accessing a dictionary key that doesn't exist.

**Examples:**
```python
let person = {"name": "Alice"}

# Wrong
print(person["age"])  # age key doesn't exist

# Right
try
    print(person["age"])
except error
    print("Age not found")
end
```

**Solution:** Check if key exists or use try-except blocks.

---

## Expression Errors

### Cannot Evaluate Expression

**Error Message:**
```
Cannot evaluate expression: ...
```

**Cause:** Invalid expression syntax or operation.

**Examples:**
```python
# Wrong
let result = 5 + * 3  # Invalid operators

# Wrong
let x = (5 + 3  # Unmatched parentheses

# Right
let result = 5 + 3
let x = (5 + 3) * 2
```

**Solution:** Check expression syntax and operator usage.

---

### Division by Zero

**Error Message:**
```
Division by zero
```

**Cause:** Attempting to divide by zero.

**Examples:**
```python
# Wrong
let result = 10 / 0

# Right
let divisor = 0
if divisor != 0
    let result = 10 / divisor
else
    print("Cannot divide by zero")
end
```

**Solution:** Check for zero before dividing.

---

## Import Errors

### Library Not Found

**Error Message:**
```
Library 'library_name' not found
```

**Cause:** Trying to import a library that doesn't exist.

**Examples:**
```python
# Wrong
import nonexistent

# Right
import random  # Built-in library
```

**Solution:** Only import built-in libraries (currently: `random`).

---

### Function Not Found in Library

**Error Message:**
```
Library 'library' has no function 'function_name'
```

**Cause:** Calling a function that doesn't exist in the library.

**Examples:**
```python
import random

# Wrong
let num = random.nonexistent()

# Right
let num = random.randint(1, 10)
```

**Solution:** Check the library documentation for available functions.

---

## Control Flow Errors

### Invalid 'if' Statement

**Error Message:**
```
Invalid if statement
```

**Cause:** Incorrect if statement syntax.

**Examples:**
```python
# Wrong
if
    print("Hello")
end

# Wrong
if x  # Missing comparison
    print("Hello")
end

# Right
if x > 5
    print("Hello")
end
```

**Solution:** Include a condition after `if`.

---

### Invalid 'while' Loop

**Error Message:**
```
Invalid while loop
```

**Cause:** Incorrect while loop syntax.

**Examples:**
```python
# Wrong
while
    print("Hello")
end

# Right
while x < 10
    print(x)
    x += 1
end
```

**Solution:** Include a condition after `while`.

---

### Invalid 'for' Loop

**Error Message:**
```
Invalid for loop / Expected 'in' in for loop
```

**Cause:** Incorrect for loop syntax.

**Examples:**
```python
# Wrong
for item fruits
    print(item)
end

# Right
for item in fruits
    print(item)
end
```

**Solution:** Use the format `for variable in iterable`.

---

## Common Mistake Patterns

### Forgetting String Conversion

```python
# Wrong
let age = 25
print("Age: " + age)  # Error: can't concatenate int to string

# Right
let age = 25
print("Age: " + str(age))
```

### Using = Instead of ==

```python
# Wrong
if x = 5  # Assignment, not comparison
    print("Five")
end

# Right
if x == 5  # Comparison
    print("Five")
end
```

### Missing Quotes for Strings

```python
# Wrong
let name = Alice  # Treated as variable

# Right
let name = "Alice"  # String literal
```

### Incorrect Indentation Confusion

```python
# Indentation is optional in Tourmaline
# But 'end' keywords are required

# Wrong
if condition
    print("Yes")
# Missing 'end'

# Right
if condition
    print("Yes")
end
```

## Debugging Tips

### 1. Read the Error Message Carefully

Error messages usually indicate:
- What went wrong
- Where it happened (which line or expression)
- What was expected

### 2. Check Common Issues

- Missing `let` for variable declaration
- Missing `end` keywords
- Typos in variable/function names
- Missing quotes around strings
- Missing `str()` when concatenating

### 3. Use Print Statements

```python
# Debug by printing values
print("x is: " + str(x))
print("Type of x: " + type(x))
```

### 4. Test Small Parts

```python
# Test expressions separately
let a = 5
let b = 3
print(a + b)  # Make sure this works
let result = a + b
```

### 5. Use Try-Except for Testing

```python
try
    # Test risky code here
    let result = int(user_input)
except error
    print("Error occurred: " + error)
end
```

## Getting Help

If you encounter an error not listed here:

1. **Check the syntax reference** - [Syntax Reference](syntax.md)
2. **Review examples** - [Examples](../examples/basic.md)
3. **Report the issue** - [GitHub Issues](https://github.com/mochacinno-dev/Tourmaline/issues)

## Prevention Checklist

Before running your code, check:

- [ ] All variables declared with `let`
- [ ] All blocks closed with `end`
- [ ] All function calls have parentheses
- [ ] String concatenation uses `str()` for non-strings
- [ ] Comparisons use `==` not `=`
- [ ] List indices are within bounds
- [ ] Division operations check for zero
- [ ] Input is validated before conversion

---

**Remember:** Error messages are helpful! They tell you exactly what went wrong and often suggest how to fix it.