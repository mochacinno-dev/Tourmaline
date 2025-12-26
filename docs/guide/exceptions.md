# Exception Handling

Learn how to handle errors gracefully in Tourmaline using try-except blocks.

## What Are Exceptions?

Exceptions are errors that occur during program execution. Without proper handling, exceptions cause programs to crash. Tourmaline provides `try-except` blocks to catch and handle errors.

## Basic Try-Except

### Simple Exception Handling

```python
try
    let result = 10 / 0  # This will cause an error
except
    print("An error occurred!")
end
```

**Output:**
```
An error occurred!
```

### Capturing the Error Message

```python
try
    let number = int("not a number")
except error
    print("Error: " + error)
end
```

**Output:**
```
Error: Cannot convert 'not a number' to integer: ...
```

## Common Error Scenarios

### Type Conversion Errors

```python
function safe_int_convert(value)
    try
        return int(value)
    except error
        print("Cannot convert '" + value + "' to integer")
        return nil
    end
end

print(safe_int_convert("42"))      # 42
print(safe_int_convert("hello"))   # Error message, returns nil
```

### Division by Zero

```python
function safe_divide(a, b)
    try
        return a / b
    except error
        print("Division error: " + error)
        return nil
    end
end

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error message, returns nil
```

### List Index Errors

```python
function safe_get(list, index)
    try
        return list[index]
    except error
        print("Index out of range: " + error)
        return nil
    end
end

let fruits = ["apple", "banana", "cherry"]
print(safe_get(fruits, 1))   # banana
print(safe_get(fruits, 10))  # Error message, returns nil
```

### Dictionary Key Errors

```python
function safe_lookup(dict, key)
    try
        return dict[key]
    except error
        print("Key '" + key + "' not found")
        return nil
    end
end

let person = {"name": "Alice", "age": 30}
print(safe_lookup(person, "name"))     # Alice
print(safe_lookup(person, "email"))    # Error message, returns nil
```

## Input Validation with Exceptions

### Getting Valid Integer Input

```python
function get_integer(prompt)
    while true
        let input_str = input(prompt)
        
        try
            let number = int(input_str)
            return number
        except error
            print("Please enter a valid integer")
        end
    end
end

let age = get_integer("Enter your age: ")
print("You are " + str(age) + " years old")
```

### Getting Valid Float Input

```python
function get_float(prompt)
    while true
        let input_str = input(prompt)
        
        try
            let number = float(input_str)
            return number
        except error
            print("Please enter a valid number")
        end
    end
end

let price = get_float("Enter price: $")
print("Price: $" + str(price))
```

### Range-Validated Input

```python
function get_number_in_range(prompt, min_val, max_val)
    while true
        let input_str = input(prompt)
        
        try
            let number = int(input_str)
            
            if number >= min_val and number <= max_val
                return number
            else
                print("Please enter a number between " + str(min_val) + " and " + str(max_val))
            end
        except error
            print("Please enter a valid integer")
        end
    end
end

let rating = get_number_in_range("Rate from 1-5: ", 1, 5)
print("You rated: " + str(rating))
```

## Multiple Operations with Error Handling

### Calculator with Error Handling

```python
function safe_calculator(a, b, operation)
    try
        if operation == "+"
            return a + b
        elif operation == "-"
            return a - b
        elif operation == "*"
            return a * b
        elif operation == "/"
            if b == 0
                print("Error: Cannot divide by zero")
                return nil
            end
            return a / b
        else
            print("Error: Unknown operation")
            return nil
        end
    except error
        print("Calculation error: " + error)
        return nil
    end
end

print(safe_calculator(10, 5, "+"))   # 15
print(safe_calculator(10, 5, "/"))   # 2.0
print(safe_calculator(10, 0, "/"))   # Error message
```

### List Processing with Error Handling

```python
function process_numbers(str_list)
    let results = []
    let errors = 0
    
    for str_num in str_list
        try
            let number = int(str_num)
            append(results, number)
        except error
            print("Skipping invalid value: " + str_num)
            errors += 1
        end
    end
    
    print("\nProcessed " + str(len(results)) + " numbers")
    print("Encountered " + str(errors) + " errors")
    
    return results
end

let inputs = ["42", "hello", "17", "3.14", "world", "99"]
let numbers = process_numbers(inputs)
print("Valid numbers: " + str(numbers))
```

## Nested Try-Except

You can nest try-except blocks for complex error handling:

```python
function complex_operation(data)
    try
        print("Starting operation...")
        
        try
            let value = int(data)
            print("Converted to: " + str(value))
            
            let result = 100 / value
            print("Result: " + str(result))
        except inner_error
            print("Inner error: " + inner_error)
        end
        
        print("Operation completed")
        
    except outer_error
        print("Outer error: " + outer_error)
    end
end

complex_operation("10")      # Success
complex_operation("0")       # Inner error (division by zero)
complex_operation("hello")   # Inner error (conversion)
```

## Error Recovery Patterns

### Retry Pattern

```python
function retry_operation(max_attempts)
    let attempts = 0
    
    while attempts < max_attempts
        attempts += 1
        print("\nAttempt " + str(attempts) + ":")
        
        let value = input("Enter a number: ")
        
        try
            let number = int(value)
            print("Success! You entered: " + str(number))
            return number
        except error
            print("Invalid input. Please try again.")
            
            if attempts >= max_attempts
                print("Maximum attempts reached.")
                return nil
            end
        end
    end
end

let result = retry_operation(3)
```

### Fallback Pattern

```python
function get_config_value(config, key, default)
    try
        return config[key]
    except error
        print("Using default value for '" + key + "'")
        return default
    end
end

let settings = {
    "theme": "dark",
    "font_size": 14
}

let theme = get_config_value(settings, "theme", "light")
let language = get_config_value(settings, "language", "en")

print("Theme: " + theme)         # dark
print("Language: " + language)   # en (default)
```

### Graceful Degradation

```python
function load_user_data(user_id)
    let default_user = {
        "id": 0,
        "name": "Guest",
        "role": "visitor"
    }
    
    try
        # Simulate data loading
        if user_id <= 0
            # Force an error
            let x = 1 / 0
        end
        
        # Return user data
        return {
            "id": user_id,
            "name": "User" + str(user_id),
            "role": "member"
        }
    except error
        print("Could not load user data, using defaults")
        return default_user
    end
end

let user1 = load_user_data(123)
print("User: " + user1["name"])

let user2 = load_user_data(-1)
print("User: " + user2["name"])  # Guest
```

## Practical Examples

### File Data Parser

```python
function parse_csv_line(line)
    # Simplified CSV parsing
    let data = []
    
    try
        # In a real implementation, you'd split by commas
        # This is a demonstration
        append(data, line)
        return data
    except error
        print("Error parsing line: " + error)
        return []
    end
end
```

### Safe Dictionary Builder

```python
function build_person(name, age_str, email)
    try
        let age = int(age_str)
        
        if age < 0 or age > 150
            print("Warning: Unusual age value")
        end
        
        return {
            "name": name,
            "age": age,
            "email": email
        }
    except error
        print("Error creating person: " + error)
        return {
            "name": name,
            "age": 0,
            "email": email
        }
    end
end

let person1 = build_person("Alice", "30", "alice@email.com")
let person2 = build_person("Bob", "invalid", "bob@email.com")

print(person1["age"])  # 30
print(person2["age"])  # 0 (default)
```

### Batch Processor

```python
function process_batch(items)
    let successful = 0
    let failed = 0
    let results = []
    
    print("Processing " + str(len(items)) + " items...")
    
    for item in items
        try
            # Simulate processing
            let processed = int(item) * 2
            append(results, processed)
            successful += 1
        except error
            print("Failed to process: " + str(item))
            failed += 1
        end
    end
    
    print("\n=== BATCH RESULTS ===")
    print("Successful: " + str(successful))
    print("Failed: " + str(failed))
    print("Success Rate: " + str(successful * 100 / len(items)) + "%")
    
    return results
end

let data = ["10", "20", "bad", "30", "error", "40"]
let results = process_batch(data)
print("Processed values: " + str(results))
```

### Transaction Handler

```python
function process_transaction(amount_str, account_balance)
    try
        let amount = float(amount_str)
        
        if amount <= 0
            print("Error: Amount must be positive")
            return account_balance
        end
        
        if amount > account_balance
            print("Error: Insufficient funds")
            return account_balance
        end
        
        let new_balance = account_balance - amount
        print("Transaction successful!")
        print("New balance: $" + str(new_balance))
        return new_balance
        
    except error
        print("Transaction failed: " + error)
        return account_balance
    end
end

let balance = 1000.0
balance = process_transaction("50.00", balance)    # Success
balance = process_transaction("2000.00", balance)  # Insufficient funds
balance = process_transaction("invalid", balance)  # Error
print("Final balance: $" + str(balance))
```

## Best Practices

### 1. Catch Specific Errors

```python
# Good: Handle expected errors
try
    let number = int(user_input)
except error
    print("Please enter a valid number")
end
```

### 2. Provide Helpful Error Messages

```python
# Less helpful
try
    let x = int(value)
except error
    print("Error")
end

# More helpful
try
    let x = int(value)
except error
    print("Cannot convert '" + value + "' to a number. Please enter digits only.")
end
```

### 3. Don't Hide Errors Silently

```python
# Bad: Silently ignoring errors
try
    risky_operation()
except error
    # Do nothing - error is hidden!
end

# Good: At least log the error
try
    risky_operation()
except error
    print("Warning: Operation failed - " + error)
end
```

### 4. Use Exceptions for Exceptional Cases

```python
# Don't use for normal control flow
# Bad:
try
    let value = dict[key]
except error
    let value = default
end

# Better: Check first if possible
# (Though Tourmaline requires the try-except for missing keys)
```

### 5. Clean Up Resources

```python
function process_data(data)
    let result = nil
    
    try
        # Process data
        result = complex_operation(data)
    except error
        print("Processing failed: " + error)
    end
    
    # Always execute cleanup
    print("Cleaning up...")
    
    return result
end
```

## Common Error Types

| Scenario | Error Type | Example |
|----------|-----------|---------|
| Invalid conversion | Type conversion | `int("hello")` |
| Division by zero | Math error | `10 / 0` |
| Invalid index | Index error | `list[999]` |
| Missing key | Key error | `dict["missing"]` |
| Invalid operation | Operation error | Varies |

## Testing Error Handling

```python
function test_error_handling()
    print("Testing error handling...\n")
    
    # Test 1: Type conversion
    print("Test 1: Type Conversion")
    try
        let x = int("invalid")
        print("FAIL: Should have raised error")
    except error
        print("PASS: Caught conversion error")
    end
    
    # Test 2: Division by zero
    print("\nTest 2: Division by Zero")
    try
        let y = 10 / 0
        print("FAIL: Should have raised error")
    except error
        print("PASS: Caught division error")
    end
    
    print("\nAll tests completed!")
end

test_error_handling()
```

## Next Steps

- **[Built-in Functions](../stdlib/builtins.md)** - Functions that may raise exceptions
- **[Examples](../examples/basic.md)** - See error handling in practice
- **[Advanced Examples](../examples/advanced.md)** - Complex error handling scenarios