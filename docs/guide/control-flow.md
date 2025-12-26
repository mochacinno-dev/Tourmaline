# Control Flow

Control flow statements let you control the order in which code executes. Learn about conditionals and loops in Tourmaline.

## Conditional Statements

### If Statement

Execute code only when a condition is true:

```python
let temperature = 25

if temperature > 30
    print("It's hot!")
end
```

!!! note
    All conditional blocks must end with `end`

### If-Else Statement

Provide alternative code when condition is false:

```python
let age = 16

if age >= 18
    print("You can vote")
else
    print("You cannot vote yet")
end
```

### If-Elif-Else Statement

Check multiple conditions in sequence:

```python
let score = 85

if score >= 90
    print("Grade: A")
elif score >= 80
    print("Grade: B")
elif score >= 70
    print("Grade: C")
elif score >= 60
    print("Grade: D")
else
    print("Grade: F")
end
```

**How It Works:**
1. Checks first condition (`score >= 90`)
2. If false, checks next condition (`score >= 80`)
3. Continues until a condition is true
4. Executes that block and skips the rest
5. If no condition is true, executes `else` block

### Nested If Statements

Place if statements inside other if statements:

```python
let age = 20
let has_license = true

if age >= 18
    if has_license
        print("You can drive")
    else
        print("You need a license")
    end
else
    print("You're too young to drive")
end
```

**Better Alternative:**
```python
let age = 20
let has_license = true

if age >= 18 and has_license
    print("You can drive")
elif age >= 18
    print("You need a license")
else
    print("You're too young to drive")
end
```

## While Loops

Execute code repeatedly while a condition is true:

```python
let count = 1

while count <= 5
    print("Count: " + str(count))
    count += 1
end
```

**Output:**
```
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

### Infinite Loops with Break Condition

```python
let running = true

while running
    let choice = input("Continue? (yes/no): ")
    
    if choice == "no"
        running = false
    end
end
```

### Common While Loop Patterns

**Countdown:**
```python
let countdown = 10

while countdown > 0
    print(str(countdown) + "...")
    countdown -= 1
end
print("Liftoff!")
```

**Input Validation:**
```python
let valid_input = false

while valid_input == false
    let age_str = input("Enter your age: ")
    
    try
        let age = int(age_str)
        if age > 0 and age < 150
            valid_input = true
            print("Valid age: " + str(age))
        else
            print("Please enter a realistic age")
        end
    except error
        print("Please enter a number")
    end
end
```

**Accumulator Pattern:**
```python
let total = 0
let count = 1

while count <= 10
    total += count
    count += 1
end

print("Sum of 1-10: " + str(total))  # 55
```

## For Loops

Iterate over items in a collection:

```python
let fruits = ["apple", "banana", "cherry"]

for fruit in fruits
    print("I like " + fruit)
end
```

**Output:**
```
I like apple
I like banana
I like cherry
```

### Iterating Over Ranges

Create a list of numbers to iterate:

```python
let numbers = [1, 2, 3, 4, 5]

for num in numbers
    print("Number: " + str(num))
end
```

### For Loop with Index

Track the position while iterating:

```python
let items = ["first", "second", "third"]
let index = 0

for item in items
    index += 1
    print(str(index) + ". " + item)
end
```

**Output:**
```
1. first
2. second
3. third
```

### Nested For Loops

Loop inside another loop:

```python
let rows = [1, 2, 3]

for row in rows
    let cols = [1, 2, 3]
    for col in cols
        print(str(row) + "x" + str(col) + "=" + str(row * col))
    end
end
```

**Output:**
```
1x1=1
1x2=2
1x3=3
2x1=2
2x2=4
2x3=6
3x1=3
3x2=6
3x3=9
```

## Practical Examples

### Menu System

```python
function show_menu()
    print("\n=== MAIN MENU ===")
    print("1. Option One")
    print("2. Option Two")
    print("3. Option Three")
    print("4. Exit")
end

let running = true

while running
    show_menu()
    let choice = input("\nEnter choice: ")
    
    if choice == "1"
        print("You selected Option One")
    elif choice == "2"
        print("You selected Option Two")
    elif choice == "3"
        print("You selected Option Three")
    elif choice == "4"
        print("Goodbye!")
        running = false
    else
        print("Invalid choice. Please try again.")
    end
end
```

### Number Classifier

```python
function classify_number(num)
    # Check if prime
    let is_prime = true
    if num < 2
        is_prime = false
    else
        let i = 2
        while i * i <= num
            if num % i == 0
                is_prime = false
            end
            i += 1
        end
    end
    
    # Check if even
    let is_even = num % 2 == 0
    
    # Report findings
    print("\nNumber: " + str(num))
    
    if is_even
        print("- Even number")
    else
        print("- Odd number")
    end
    
    if is_prime
        print("- Prime number")
    else
        print("- Not prime")
    end
    
    if num > 0
        print("- Positive")
    elif num < 0
        print("- Negative")
    else
        print("- Zero")
    end
end

let test_numbers = [2, 7, 10, 13, 15, 20]

for num in test_numbers
    classify_number(num)
end
```

### Grade Calculator

```python
let students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 78},
    {"name": "Charlie", "score": 85},
    {"name": "Diana", "score": 95}
]

print("=== GRADE REPORT ===\n")

for student in students
    let name = student["name"]
    let score = student["score"]
    let grade = ""
    
    if score >= 90
        grade = "A"
    elif score >= 80
        grade = "B"
    elif score >= 70
        grade = "C"
    elif score >= 60
        grade = "D"
    else
        grade = "F"
    end
    
    print(name + ": " + str(score) + " (" + grade + ")")
end
```

### Fibonacci Sequence Generator

```python
function fibonacci(n)
    print("Fibonacci sequence (first " + str(n) + " numbers):")
    
    if n >= 1
        print("1. 0")
    end
    
    if n >= 2
        print("2. 1")
    end
    
    if n > 2
        let prev = 0
        let curr = 1
        let pos = 3
        
        while pos <= n
            let next = prev + curr
            print(str(pos) + ". " + str(next))
            prev = curr
            curr = next
            pos += 1
        end
    end
end

fibonacci(10)
```

### Prime Number Finder

```python
function find_primes(limit)
    print("Prime numbers up to " + str(limit) + ":")
    let count = 0
    let num = 2
    
    while num <= limit
        let is_prime = true
        let i = 2
        
        while i * i <= num
            if num % i == 0
                is_prime = false
            end
            i += 1
        end
        
        if is_prime
            print("  " + str(num))
            count += 1
        end
        
        num += 1
    end
    
    print("\nTotal primes found: " + str(count))
end

find_primes(50)
```

### Pattern Generator

```python
function print_triangle(height)
    let row = 1
    
    while row <= height
        let col = 1
        while col <= row
            print("*")
            col += 1
        end
        print("\n")
        row += 1
    end
end

print("Triangle Pattern:")
print_triangle(5)
```

### List Statistics

```python
function calculate_statistics(numbers)
    if len(numbers) == 0
        print("List is empty")
        return
    end
    
    # Calculate sum
    let total = 0
    for num in numbers
        total += num
    end
    
    # Calculate average
    let average = total / len(numbers)
    
    # Find min and max
    let minimum = numbers[0]
    let maximum = numbers[0]
    
    for num in numbers
        if num < minimum
            minimum = num
        end
        if num > maximum
            maximum = num
        end
    end
    
    # Count positives and negatives
    let positive_count = 0
    let negative_count = 0
    let zero_count = 0
    
    for num in numbers
        if num > 0
            positive_count += 1
        elif num < 0
            negative_count += 1
        else
            zero_count += 1
        end
    end
    
    # Print report
    print("\n=== STATISTICS ===")
    print("Count: " + str(len(numbers)))
    print("Sum: " + str(total))
    print("Average: " + str(average))
    print("Minimum: " + str(minimum))
    print("Maximum: " + str(maximum))
    print("Range: " + str(maximum - minimum))
    print("Positive: " + str(positive_count))
    print("Negative: " + str(negative_count))
    print("Zero: " + str(zero_count))
end

let data = [15, -3, 42, 8, -12, 0, 23, 7, -5, 31]
calculate_statistics(data)
```

### Word Counter

```python
function count_words(text)
    let words = []
    let current_word = ""
    let i = 0
    
    # Simple word splitting (space-based)
    while i < len(text)
        # This is simplified; real implementation would be more complex
        i += 1
    end
    
    # For demonstration
    print("Total characters: " + str(len(text)))
end

let sample = "Hello world from Tourmaline"
count_words(sample)
```

## Control Flow Best Practices

### 1. Keep Conditions Simple

```python
# Less readable
if age >= 18 and has_license and not suspended and passed_test and has_insurance
    # ...
end

# More readable
let is_adult = age >= 18
let can_legally_drive = has_license and not suspended and passed_test
let is_insured = has_insurance

if is_adult and can_legally_drive and is_insured
    # ...
end
```

### 2. Avoid Deep Nesting

```python
# Too deeply nested
if condition1
    if condition2
        if condition3
            if condition4
                # code
            end
        end
    end
end

# Better: Early returns or flat structure
if not condition1
    return
end
if not condition2
    return
end
if not condition3
    return
end
if not condition4
    return
end
# code
```

### 3. Use Meaningful Loop Variables

```python
# Less clear
for x in y
    print(x)
end

# More clear
for student in students
    print(student)
end

for item in shopping_cart
    process_item(item)
end
```

### 4. Guard Against Infinite Loops

```python
# Dangerous: might loop forever
while true
    # code with no break condition
end

# Safer: include exit condition
let max_iterations = 1000
let count = 0

while count < max_iterations
    # code
    count += 1
    
    if some_condition
        break  # (conceptually)
    end
end
```

## Common Patterns

### Sentinel Loop

```python
let running = true

while running
    let command = input("Enter command (or 'quit'): ")
    
    if command == "quit"
        running = false
    else
        # Process command
        print("Processing: " + command)
    end
end
```

### Counter Loop

```python
let counter = 0
let target = 10

while counter < target
    print("Iteration: " + str(counter))
    counter += 1
end
```

### Search Pattern

```python
let items = ["apple", "banana", "cherry", "date"]
let search_term = "cherry"
let found = false

for item in items
    if item == search_term
        print("Found: " + item)
        found = true
    end
end

if not found
    print("Not found")
end
```

### Filter Pattern

```python
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let evens = []

for num in numbers
    if num % 2 == 0
        append(evens, num)
    end
end

print("Even numbers: " + str(evens))
```

## Next Steps

- **[Functions](functions.md)** - Organize control flow into reusable blocks
- **[Lists & Dictionaries](collections.md)** - Iterate over complex data
- **[Exception Handling](exceptions.md)** - Control flow for error handling