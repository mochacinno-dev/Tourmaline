# Operators

Operators are symbols that perform operations on values. Tourmaline supports arithmetic, comparison, logical, and assignment operators.

## Arithmetic Operators

Perform mathematical calculations.

### Addition (`+`)

```python
let a = 5
let b = 3
let sum = a + b
print(sum)  # 8
```

**String Concatenation:**
```python
let first = "Hello"
let last = "World"
let message = first + " " + last
print(message)  # Hello World
```

### Subtraction (`-`)

```python
let a = 10
let b = 4
let difference = a - b
print(difference)  # 6
```

**Negative Numbers:**
```python
let x = 5
let y = -3
let result = x + y
print(result)  # 2
```

### Multiplication (`*`)

```python
let a = 6
let b = 7
let product = a * b
print(product)  # 42
```

### Division (`/`)

```python
let a = 20
let b = 4
let quotient = a / b
print(quotient)  # 5.0
```

!!! warning
    Division by zero will cause an error:
    
    ```python
    try
        let result = 10 / 0
    except error
        print("Cannot divide by zero!")
    end
    ```

**Float Division:**
```python
let a = 7
let b = 2
let result = a / b
print(result)  # 3.5
```

### Modulo (`%`)

Returns the remainder of division:

```python
let a = 17
let b = 5
let remainder = a % b
print(remainder)  # 2
```

**Check Even/Odd:**
```python
let number = 7

if number % 2 == 0
    print("Even")
else
    print("Odd")
end
```

**Cycle Through Values:**
```python
let index = 0
let items = ["A", "B", "C"]

while index < 10
    let position = index % len(items)
    print(items[position])
    index += 1
end
# Output: A, B, C, A, B, C, A, B, C, A
```

## Comparison Operators

Compare values and return boolean results.

### Equal To (`==`)

```python
let a = 5
let b = 5
print(a == b)  # true

let x = "hello"
let y = "hello"
print(x == y)  # true
```

### Not Equal To (`!=`)

```python
let a = 5
let b = 3
print(a != b)  # true

let x = "cat"
let y = "dog"
print(x != y)  # true
```

### Less Than (`<`)

```python
let a = 3
let b = 7
print(a < b)  # true
print(b < a)  # false
```

### Greater Than (`>`)

```python
let a = 10
let b = 5
print(a > b)  # true
print(b > a)  # false
```

### Less Than or Equal To (`<=`)

```python
let a = 5
let b = 5
let c = 3

print(a <= b)  # true (equal)
print(c <= b)  # true (less than)
print(b <= c)  # false
```

### Greater Than or Equal To (`>=`)

```python
let a = 10
let b = 10
let c = 15

print(a >= b)  # true (equal)
print(c >= b)  # true (greater than)
print(b >= c)  # false
```

## Logical Operators

Combine boolean expressions.

### AND (`and`)

Returns `true` only if both operands are `true`:

```python
let a = true
let b = true
let c = false

print(a and b)  # true
print(a and c)  # false
print(c and c)  # false
```

**Practical Example:**
```python
let age = 25
let has_license = true

if age >= 18 and has_license
    print("Can drive")
else
    print("Cannot drive")
end
```

**Multiple Conditions:**
```python
let score = 85
let attendance = 95
let participation = 80

if score >= 80 and attendance >= 90 and participation >= 75
    print("Excellent student!")
end
```

### OR (`or`)

Returns `true` if at least one operand is `true`:

```python
let a = true
let b = false
let c = false

print(a or b)  # true
print(b or c)  # false
print(a or c)  # true
```

**Practical Example:**
```python
let is_weekend = true
let is_holiday = false

if is_weekend or is_holiday
    print("No work today!")
end
```

**Multiple Options:**
```python
let choice = "b"

if choice == "a" or choice == "A" or choice == "1"
    print("Option A selected")
elif choice == "b" or choice == "B" or choice == "2"
    print("Option B selected")
end
```

## Assignment Operators

Assign and update variable values.

### Simple Assignment (`=`)

```python
let x = 10
let name = "Alice"
let is_active = true
```

### Compound Assignment

#### Addition Assignment (`+=`)

```python
let counter = 5
counter += 3  # Same as: counter = counter + 3
print(counter)  # 8
```

**String Concatenation:**
```python
let message = "Hello"
message += " World"
print(message)  # Hello World
```

#### Subtraction Assignment (`-=`)

```python
let balance = 100
balance -= 25  # Same as: balance = balance - 25
print(balance)  # 75
```

#### Multiplication Assignment (`*=`)

```python
let value = 5
value *= 3  # Same as: value = value * 3
print(value)  # 15
```

#### Division Assignment (`/=`)

```python
let amount = 100
amount /= 4  # Same as: amount = amount / 4
print(amount)  # 25.0
```

## Operator Precedence

Operations are evaluated in a specific order:

| Priority | Operators | Description |
|----------|-----------|-------------|
| 1 (Highest) | `()` | Parentheses |
| 2 | Function calls | `func()` |
| 3 | `.` `[]` | Member/Index access |
| 4 | `*` `/` `%` | Multiplication, Division, Modulo |
| 5 | `+` `-` | Addition, Subtraction |
| 6 | `<` `>` `<=` `>=` | Comparison |
| 7 | `==` `!=` | Equality |
| 8 | `and` | Logical AND |
| 9 (Lowest) | `or` | Logical OR |

### Examples

```python
# Multiplication before addition
let result = 2 + 3 * 4
print(result)  # 14, not 20

# Use parentheses to change order
let result2 = (2 + 3) * 4
print(result2)  # 20

# Complex expression
let x = 10 + 5 * 2 - 3
# 10 + (5 * 2) - 3
# 10 + 10 - 3
# 17
print(x)  # 17

# Comparison before and
let result3 = 5 > 3 and 10 < 20
# (5 > 3) and (10 < 20)
# true and true
# true
print(result3)  # true
```

## Practical Examples

### Calculator Functions

```python
function calculate(a, b, operation)
    if operation == "+"
        return a + b
    elif operation == "-"
        return a - b
    elif operation == "*"
        return a * b
    elif operation == "/"
        if b != 0
            return a / b
        else
            print("Error: Division by zero")
            return nil
        end
    elif operation == "%"
        return a % b
    else
        print("Invalid operation")
        return nil
    end
end

print(calculate(10, 5, "+"))   # 15
print(calculate(10, 5, "-"))   # 5
print(calculate(10, 5, "*"))   # 50
print(calculate(10, 5, "/"))   # 2.0
print(calculate(10, 3, "%"))   # 1
```

### Range Checker

```python
function in_range(value, min_val, max_val)
    return value >= min_val and value <= max_val
end

let score = 85

if in_range(score, 90, 100)
    print("Grade: A")
elif in_range(score, 80, 89)
    print("Grade: B")
elif in_range(score, 70, 79)
    print("Grade: C")
elif in_range(score, 60, 69)
    print("Grade: D")
else
    print("Grade: F")
end
```

### Even/Odd Counter

```python
function count_even_odd(numbers)
    let even_count = 0
    let odd_count = 0
    
    for num in numbers
        if num % 2 == 0
            even_count += 1
        else
            odd_count += 1
        end
    end
    
    print("Even numbers: " + str(even_count))
    print("Odd numbers: " + str(odd_count))
end

let data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_even_odd(data)
# Even numbers: 5
# Odd numbers: 5
```

### Discount Calculator

```python
function calculate_final_price(price, discount_percent)
    let discount = price * discount_percent / 100
    let final = price - discount
    return final
end

function apply_bulk_discount(price, quantity)
    # 10% off for 10+ items, 20% off for 50+ items
    if quantity >= 50
        return calculate_final_price(price * quantity, 20)
    elif quantity >= 10
        return calculate_final_price(price * quantity, 10)
    else
        return price * quantity
    end
end

let item_price = 25
let qty = 15

let total = apply_bulk_discount(item_price, qty)
print("Total: $" + str(total))  # $337.5 (10% discount applied)
```

### Password Validator

```python
function validate_password(password)
    let length = len(password)
    let has_number = false
    let has_upper = false
    let has_lower = false
    
    # Check length
    if length < 8
        print("Password must be at least 8 characters")
        return false
    end
    
    # In a real implementation, you'd check for numbers and case
    # This is a simplified version
    
    let is_valid = length >= 8 and length <= 20
    
    if is_valid
        print("Password is valid")
        return true
    else
        print("Password is invalid")
        return false
    end
end

validate_password("short")      # Too short
validate_password("ValidPass123")  # Valid
```

### Temperature Range Checker

```python
function check_temperature(temp)
    if temp < 0
        print("Freezing!")
    elif temp >= 0 and temp < 10
        print("Very cold")
    elif temp >= 10 and temp < 20
        print("Cold")
    elif temp >= 20 and temp < 30
        print("Comfortable")
    elif temp >= 30 and temp < 40
        print("Hot")
    else
        print("Very hot!")
    end
end

check_temperature(-5)   # Freezing!
check_temperature(15)   # Cold
check_temperature(25)   # Comfortable
check_temperature(38)   # Hot
```

## Common Patterns

### Increment Counter

```python
let count = 0
count += 1  # Increment by 1
```

### Toggle Boolean

```python
let is_active = true
is_active = false  # Toggle off

# Or check and toggle:
if is_active
    is_active = false
else
    is_active = true
end
```

### Accumulator Pattern

```python
let total = 0
let numbers = [10, 20, 30, 40, 50]

for num in numbers
    total += num
end

print("Total: " + str(total))  # 150
```

### Min/Max Tracking

```python
let numbers = [45, 23, 89, 12, 67]
let maximum = numbers[0]
let minimum = numbers[0]

for num in numbers
    if num > maximum
        maximum = num
    end
    if num < minimum
        minimum = num
    end
end

print("Max: " + str(maximum))  # 89
print("Min: " + str(minimum))  # 12
```

## Tips & Best Practices

!!! tip "Use Parentheses for Clarity"
    Even when not required, parentheses make complex expressions clearer:
    
    ```python
    # Less clear
    let result = a + b * c - d / e
    
    # More clear
    let result = a + (b * c) - (d / e)
    ```

!!! tip "Avoid Complex Conditionals"
    Break complex conditions into variables:
    
    ```python
    # Hard to read
    if age >= 18 and has_license and passed_test and not suspended
        # ...
    end
    
    # Easier to read
    let is_adult = age >= 18
    let can_drive = has_license and passed_test and not suspended
    
    if is_adult and can_drive
        # ...
    end
    ```

!!! warning "Watch for Division by Zero"
    Always check before dividing:
    
    ```python
    if denominator != 0
        let result = numerator / denominator
    else
        print("Cannot divide by zero")
    end
    ```

## Next Steps

- **[Control Flow](control-flow.md)** - Use operators in conditions and loops
- **[Functions](functions.md)** - Create reusable operations
- **[Math Functions](../stdlib/math.md)** - Advanced mathematical operations