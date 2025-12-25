# Functions

Functions let you organize code into reusable blocks. Learn how to define and use functions in Tourmaline.

## Defining Functions

Use the `function` keyword to define a function:

```python
function greet()
    print("Hello, World!")
end
```

Call the function:

```python
greet()  # Output: Hello, World!
```

!!! note
    All function blocks must end with the `end` keyword

## Function Parameters

Functions can accept parameters (inputs):

```python
function greet(name)
    print("Hello, " + name + "!")
end

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!
```

### Multiple Parameters

```python
function add(a, b)
    let result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result))
end

add(5, 3)   # 5 + 3 = 8
add(10, 20) # 10 + 20 = 30
```

### Any Number of Parameters

```python
function calculate_area(width, height)
    let area = width * height
    print("Area: " + str(area))
end

calculate_area(5, 10)  # Area: 50
```

## Return Values

Functions can return values using the `return` keyword:

```python
function add(x, y)
    return x + y
end

let sum = add(5, 3)
print("Sum: " + str(sum))  # Sum: 8
```

### Using Return Values

```python
function multiply(a, b)
    return a * b
end

let result = multiply(4, 7)
let doubled = multiply(result, 2)
print(doubled)  # 56
```

### Early Returns

```python
function is_positive(number)
    if number > 0
        return true
    end
    return false
end

print(is_positive(5))   # true
print(is_positive(-3))  # false
```

### Multiple Return Points

```python
function get_grade(score)
    if score >= 90
        return "A"
    elif score >= 80
        return "B"
    elif score >= 70
        return "C"
    elif score >= 60
        return "D"
    else
        return "F"
    end
end

print(get_grade(95))  # A
print(get_grade(75))  # C
```

## Functions Without Return

Functions without `return` statements return `nil`:

```python
function say_hello()
    print("Hello!")
end

let result = say_hello()  # Prints: Hello!
print(result)             # Prints: nil
```

## Variable Scope in Functions

### Local Variables

Variables declared inside functions are local:

```python
function calculate()
    let local_var = 10
    print(local_var)
end

calculate()           # Works: prints 10
# print(local_var)   # Error! local_var doesn't exist here
```

### Global Variables

Functions can access variables from outer scope:

```python
let global_count = 0

function increment()
    global_count += 1
    print("Count: " + str(global_count))
end

increment()  # Count: 1
increment()  # Count: 2
increment()  # Count: 3
```

## Practical Examples

### Temperature Converter

```python
function celsius_to_fahrenheit(celsius)
    let fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit
end

function fahrenheit_to_celsius(fahrenheit)
    let celsius = (fahrenheit - 32) * 5 / 9
    return celsius
end

let temp_c = 25
let temp_f = celsius_to_fahrenheit(temp_c)
print(str(temp_c) + "°C = " + str(temp_f) + "°F")

let temp_f2 = 77
let temp_c2 = fahrenheit_to_celsius(temp_f2)
print(str(temp_f2) + "°F = " + str(temp_c2) + "°C")
```

### Factorial Calculator

```python
function factorial(n)
    if n <= 1
        return 1
    end
    
    let result = 1
    let i = 2
    
    while i <= n
        result *= i
        i += 1
    end
    
    return result
end

print("5! = " + str(factorial(5)))    # 120
print("7! = " + str(factorial(7)))    # 5040
```

### Is Prime Checker

```python
function is_prime(num)
    if num < 2
        return false
    end
    
    if num == 2
        return true
    end
    
    let i = 2
    while i * i <= num
        if num % i == 0
            return false
        end
        i += 1
    end
    
    return true
end

print(is_prime(7))   # true
print(is_prime(10))  # false
print(is_prime(17))  # true
```

### String Utilities

```python
function repeat_string(text, times)
    let result = ""
    let i = 0
    
    while i < times
        result = result + text
        i += 1
    end
    
    return result
end

print(repeat_string("Hi! ", 3))  # Hi! Hi! Hi! 
print(repeat_string("=", 20))    # ====================
```

### List Operations

```python
function sum_list(numbers)
    let total = 0
    for num in numbers
        total += num
    end
    return total
end

function average_list(numbers)
    let total = sum_list(numbers)
    let count = len(numbers)
    return total / count
end

let scores = [85, 92, 78, 90, 88]
print("Sum: " + str(sum_list(scores)))        # 433
print("Average: " + str(average_list(scores))) # 86.6
```

### Validation Functions

```python
function is_valid_age(age)
    return age >= 0 and age <= 120
end

function is_valid_email(email)
    # Simple check: contains @ and has text before and after
    let has_at = false
    let before_at = false
    let after_at = false
    
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Simple iteration
        # This is simplified - real email validation is complex
    end
    
    # In practice, you'd use more sophisticated checking
    return true  # Placeholder
end

print(is_valid_age(25))    # true
print(is_valid_age(150))   # false
```

## Nested Functions

Functions can call other functions:

```python
function calculate_discount(price, discount_percent)
    return price * discount_percent / 100
end

function final_price(price, discount_percent)
    let discount = calculate_discount(price, discount_percent)
    let final = price - discount
    return final
end

let original = 100
let final = final_price(original, 20)
print("Original: $" + str(original))
print("Final: $" + str(final))  # $80
```

## Recursive Functions

Functions can call themselves (use with caution):

```python
function countdown(n)
    if n <= 0
        print("Done!")
        return
    end
    
    print(str(n))
    countdown(n - 1)
end

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Done!
```

!!! warning
    Be careful with recursion! Make sure you have a base case that stops the recursion, or you'll get infinite loops.

## Best Practices

### 1. Use Descriptive Names

```python
# Good
function calculate_total_price(items, tax_rate)
    # ...
end

# Less clear
function calc(x, y)
    # ...
end
```

### 2. Keep Functions Focused

```python
# Good: Each function does one thing
function calculate_subtotal(items)
    # Calculate subtotal
end

function calculate_tax(subtotal, tax_rate)
    # Calculate tax
end

function calculate_total(subtotal, tax)
    # Calculate total
end

# Less good: Function does too much
function process_order(items, tax_rate, discount)
    # Calculates everything at once
end
```

### 3. Document Complex Functions

```python
function calculate_compound_interest(principal, rate, time, frequency)
    # Calculate compound interest
    # principal: initial amount
    # rate: annual interest rate (as decimal, e.g., 0.05 for 5%)
    # time: number of years
    # frequency: times compounded per year
    
    let amount = principal * pow(1 + rate / frequency, frequency * time)
    return amount
end
```

### 4. Validate Inputs

```python
function divide(a, b)
    if b == 0
        print("Error: Cannot divide by zero")
        return nil
    end
    return a / b
end
```

## Common Patterns

### Function as Helper

```python
function print_separator()
    print("=" + "=" + "=" + "=" + "=" + "=" + "=" + "=")
end

print_separator()
print("Report")
print_separator()
```

### Function with Default Behavior

```python
function greet_user(name)
    if name == nil or name == ""
        name = "Guest"
    end
    print("Welcome, " + name + "!")
end

greet_user("Alice")  # Welcome, Alice!
greet_user("")       # Welcome, Guest!
```

## Next Steps

- **[Lists & Dictionaries](collections.md)** - Work with complex data in functions
- **[Exception Handling](exceptions.md)** - Handle errors in functions
- **[Built-in Functions](../stdlib/builtins.md)** - Explore ready-to-use functions