# Basic Examples

Collection of simple, beginner-friendly Tourmaline programs to help you learn the language.

## Hello World

The simplest program in Tourmaline:

```python
print("Hello, World!")
```

**With a variable:**
```python
let message = "Hello, World!"
print(message)
```

## User Input and Output

### Simple Greeting

```python
let name = input("What is your name? ")
print("Hello, " + name + "!")
print("Nice to meet you!")
```

### Age Calculator

```python
print("=== AGE CALCULATOR ===\n")

let name = input("Enter your name: ")
let birth_year = int(input("Enter your birth year: "))
let current_year = 2024

let age = current_year - birth_year

print("\nHello, " + name + "!")
print("You are approximately " + str(age) + " years old.")
```

## Basic Calculations

### Simple Calculator

```python
print("=== SIMPLE CALCULATOR ===\n")

let num1 = float(input("Enter first number: "))
let num2 = float(input("Enter second number: "))

print("\nResults:")
print("Sum: " + str(num1 + num2))
print("Difference: " + str(num1 - num2))
print("Product: " + str(num1 * num2))

if num2 != 0
    print("Quotient: " + str(num1 / num2))
else
    print("Cannot divide by zero")
end
```

### Temperature Converter

```python
print("=== TEMPERATURE CONVERTER ===\n")

let celsius = float(input("Enter temperature in Celsius: "))
let fahrenheit = celsius * 9 / 5 + 32

print(str(celsius) + "°C = " + str(fahrenheit) + "°F")

# Reverse conversion
let fahr = float(input("\nEnter temperature in Fahrenheit: "))
let cels = (fahr - 32) * 5 / 9

print(str(fahr) + "°F = " + str(cels) + "°C")
```

## Conditional Logic

### Grade Calculator

```python
print("=== GRADE CALCULATOR ===\n")

let score = int(input("Enter your score (0-100): "))

if score >= 90
    print("Grade: A - Excellent!")
elif score >= 80
    print("Grade: B - Good job!")
elif score >= 70
    print("Grade: C - Satisfactory")
elif score >= 60
    print("Grade: D - Needs improvement")
else
    print("Grade: F - Please study more")
end
```

### Even or Odd Checker

```python
let number = int(input("Enter a number: "))

if number % 2 == 0
    print(str(number) + " is even")
else
    print(str(number) + " is odd")
end
```

### Voting Eligibility

```python
print("=== VOTING ELIGIBILITY CHECKER ===\n")

let age = int(input("Enter your age: "))
let citizen = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizen == "yes"
    print("\nYou are eligible to vote!")
elif age < 18
    let years_to_wait = 18 - age
    print("\nYou can vote in " + str(years_to_wait) + " years.")
else
    print("\nYou must be a citizen to vote.")
end
```

## Loops

### Countdown Timer

```python
print("=== COUNTDOWN TIMER ===\n")

let seconds = int(input("Enter countdown time (seconds): "))

print("\nStarting countdown...\n")

while seconds > 0
    print(str(seconds) + "...")
    seconds -= 1
end

print("Time's up!")
```

### Multiplication Table

```python
let number = int(input("Enter a number: "))

print("\nMultiplication table for " + str(number) + ":")

let i = 1
while i <= 10
    let result = number * i
    print(str(number) + " x " + str(i) + " = " + str(result))
    i += 1
end
```

### Sum of Numbers

```python
print("=== SUM CALCULATOR ===\n")
print("Enter numbers (0 to stop)")

let total = 0
let count = 0

while true
    let num = int(input("\nEnter number: "))
    
    if num == 0
        break  # Conceptual break
    end
    
    total += num
    count += 1
end

if count > 0
    let average = total / count
    print("\nTotal: " + str(total))
    print("Count: " + str(count))
    print("Average: " + str(average))
else
    print("\nNo numbers entered")
end
```

### List Iteration

```python
let fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("My favorite fruits:")

for fruit in fruits
    print("- " + fruit)
end

print("\nNumbered list:")

let index = 1
for fruit in fruits
    print(str(index) + ". " + fruit)
    index += 1
end
```

## Working with Lists

### Shopping List

```python
let shopping_list = []

print("=== SHOPPING LIST ===\n")

# Add items
append(shopping_list, "Milk")
append(shopping_list, "Bread")
append(shopping_list, "Eggs")
append(shopping_list, "Butter")

print("Your shopping list:")
for item in shopping_list
    print("- " + item)
end

print("\nTotal items: " + str(len(shopping_list)))
```

### Find Maximum

```python
let numbers = [23, 67, 12, 89, 45, 34, 78]

let maximum = numbers[0]

for num in numbers
    if num > maximum
        maximum = num
    end
end

print("Numbers: " + str(numbers))
print("Maximum value: " + str(maximum))
```

### Count Items

```python
let fruits = ["apple", "banana", "apple", "cherry", "apple", "banana"]

let apple_count = 0

for fruit in fruits
    if fruit == "apple"
        apple_count += 1
    end
end

print("Total fruits: " + str(len(fruits)))
print("Apples: " + str(apple_count))
```

## Functions

### Area Calculator

```python
function rectangle_area(width, height)
    return width * height
end

function triangle_area(base, height)
    return base * height / 2
end

function circle_area(radius)
    let pi = 3.14159
    return pi * radius * radius
end

print("=== AREA CALCULATOR ===\n")

let rect_width = float(input("Rectangle width: "))
let rect_height = float(input("Rectangle height: "))
print("Rectangle area: " + str(rectangle_area(rect_width, rect_height)))

print("")

let tri_base = float(input("Triangle base: "))
let tri_height = float(input("Triangle height: "))
print("Triangle area: " + str(triangle_area(tri_base, tri_height)))

print("")

let radius = float(input("Circle radius: "))
print("Circle area: " + str(circle_area(radius)))
```

### Text Formatter

```python
function make_title(text)
    # Simple title case (uppercase first letter)
    return text
end

function repeat_text(text, times)
    let result = ""
    let i = 0
    
    while i < times
        result = result + text
        i += 1
    end
    
    return result
end

function count_words(text)
    # Simplified word count
    return len(text)
end

let message = input("Enter a message: ")

print("\nOriginal: " + message)
print("Repeated 3x: " + repeat_text(message, 3))
print("Characters: " + str(count_words(message)))
```

## Random Programs

### Dice Roller

```python
import random

print("=== DICE ROLLER ===\n")

let roll_again = "yes"

while roll_again == "yes"
    let dice1 = random.randint(1, 6)
    let dice2 = random.randint(1, 6)
    let total = dice1 + dice2
    
    print("Dice 1: " + str(dice1))
    print("Dice 2: " + str(dice2))
    print("Total: " + str(total))
    
    print("")
    roll_again = input("Roll again? (yes/no): ")
    print("")
end

print("Thanks for playing!")
```

### Coin Flip

```python
import random

print("=== COIN FLIP SIMULATOR ===\n")

let flips = int(input("How many flips? "))

let heads = 0
let tails = 0

let i = 0
while i < flips
    let result = random.randint(0, 1)
    
    if result == 0
        heads += 1
        print("Flip " + str(i + 1) + ": Heads")
    else
        tails += 1
        print("Flip " + str(i + 1) + ": Tails")
    end
    
    i += 1
end

print("\n=== RESULTS ===")
print("Heads: " + str(heads))
print("Tails: " + str(tails))
```

### Random Compliment Generator

```python
import random

let compliments = [
    "You're awesome!",
    "You're doing great!",
    "You're amazing!",
    "You're wonderful!",
    "You're fantastic!",
    "You're brilliant!",
    "You're incredible!"
]

print("=== RANDOM COMPLIMENT GENERATOR ===\n")

let name = input("What's your name? ")
let compliment = random.choice(compliments)

print("\nHey " + name + ", " + compliment)
```

## Data Processing

### Student Grade Tracker

```python
let students = []

function add_student(name, grade)
    let student = {
        "name": name,
        "grade": grade
    }
    append(students, student)
end

function show_students()
    print("\n=== CLASS ROSTER ===")
    for student in students
        print(student["name"] + ": " + str(student["grade"]))
    end
end

function calculate_average()
    if len(students) == 0
        return 0
    end
    
    let total = 0
    for student in students
        total += student["grade"]
    end
    
    return total / len(students)
end

# Add students
add_student("Alice", 92)
add_student("Bob", 85)
add_student("Charlie", 78)
add_student("Diana", 95)

show_students()

let avg = calculate_average()
print("\nClass Average: " + str(avg))
```

### Simple Budget Tracker

```python
let expenses = []
let income = 0

function add_expense(description, amount)
    let expense = {
        "description": description,
        "amount": amount
    }
    append(expenses, expense)
    print("Added expense: " + description + " - $" + str(amount))
end

function show_summary()
    let total_expenses = 0
    
    print("\n=== EXPENSES ===")
    for expense in expenses
        print(expense["description"] + ": $" + str(expense["amount"]))
        total_expenses += expense["amount"]
    end
    
    print("\n=== SUMMARY ===")
    print("Income: $" + str(income))
    print("Expenses: $" + str(total_expenses))
    print("Balance: $" + str(income - total_expenses))
end

income = float(input("Enter your monthly income: $"))

print("\nEnter expenses (type 'done' when finished)")
# Simplified: pre-add expenses for demo
add_expense("Rent", 800.0)
add_expense("Groceries", 200.0)
add_expense("Transportation", 100.0)

show_summary()
```

## Interactive Programs

### Simple Quiz

```python
print("=== SIMPLE QUIZ ===\n")

let score = 0

# Question 1
print("Question 1: What is 5 + 7?")
let answer1 = input("Your answer: ")
if answer1 == "12"
    print("Correct!")
    score += 1
else
    print("Wrong! The answer is 12")
end

print("")

# Question 2
print("Question 2: What is the capital of France?")
let answer2 = input("Your answer: ")
if answer2 == "Paris" or answer2 == "paris"
    print("Correct!")
    score += 1
else
    print("Wrong! The answer is Paris")
end

print("")

# Question 3
print("Question 3: What is 3 x 4?")
let answer3 = input("Your answer: ")
if answer3 == "12"
    print("Correct!")
    score += 1
else
    print("Wrong! The answer is 12")
end

print("\n=== RESULTS ===")
print("You got " + str(score) + " out of 3 correct!")

if score == 3
    print("Perfect score!")
elif score >= 2
    print("Good job!")
else
    print("Keep practicing!")
end
```

## Next Steps

Ready for more advanced examples?

- **[Advanced Examples](advanced.md)** - Complex programs and algorithms
- **[Language Guide](../guide/variables.md)** - Deep dive into features
- **[Standard Library](../stdlib/builtins.md)** - Explore all functions