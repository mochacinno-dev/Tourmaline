# Your First Program

Let's build a complete Tourmaline program from scratch! We'll create a simple number guessing game that demonstrates key programming concepts.

## Project Overview

We'll create a game where:
- The computer picks a random number between 1 and 100
- The player tries to guess the number
- The program gives hints ("too high" or "too low")
- The game tracks the number of attempts

## Step 1: Create the File

Create a new file called `guessing_game.trm`:

```bash
# On Windows
notepad guessing_game.trm

# On Linux/macOS
nano guessing_game.trm
```

## Step 2: Add the Header

Start with a descriptive header:

```python
########################
# Number Guessing Game
# My First Tourmaline Program
########################
```

## Step 3: Import Libraries

We need the random library to generate random numbers:

```python
import random
```

## Step 4: Display Welcome Message

```python
print("=" * 40)
print("  WELCOME TO THE NUMBER GUESSING GAME!")
print("=" * 40)
print("\nI'm thinking of a number between 1 and 100.")
print("Can you guess what it is?\n")
```

!!! tip
    String multiplication isn't directly supported, so we use multiple concatenations for visual separators

## Step 5: Generate Random Number

```python
let secret_number = random.randint(1, 100)
let attempts = 0
let game_over = false
```

## Step 6: Create the Game Loop

```python
while not game_over
    # Get player's guess
    let guess_str = input("Enter your guess: ")
    
    # Convert to integer
    let guess = 0
    try
        guess = int(guess_str)
    except error
        print("Please enter a valid number!\n")
        # Continue to next iteration
    end
    
    # Skip if conversion failed
    if guess == 0
        # Continue
    else
        attempts += 1
        
        # Check the guess
        if guess < secret_number
            print("Too low! Try again.\n")
        elif guess > secret_number
            print("Too high! Try again.\n")
        else
            print("\n🎉 Congratulations! You guessed it!")
            print("The number was " + str(secret_number))
            print("It took you " + str(attempts) + " attempts.")
            game_over = true
        end
    end
end
```

## Complete Program

Here's the full program:

```python
########################
# Number Guessing Game
# My First Tourmaline Program
########################

import random

# Welcome message
print("========================================")
print("  WELCOME TO THE NUMBER GUESSING GAME!")
print("========================================")
print("")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?")
print("")

# Generate random number
let secret_number = random.randint(1, 100)
let attempts = 0
let game_over = false

# Main game loop
while game_over == false
    # Get player's guess
    let guess_str = input("Enter your guess: ")
    
    # Validate and convert input
    try
        let guess = int(guess_str)
        attempts += 1
        
        # Check the guess
        if guess < secret_number
            print("Too low! Try again.")
            print("")
        elif guess > secret_number
            print("Too high! Try again.")
            print("")
        else
            print("")
            print("Congratulations! You guessed it!")
            print("The number was " + str(secret_number))
            print("It took you " + str(attempts) + " attempts.")
            game_over = true
        end
    except error
        print("Please enter a valid number!")
        print("")
    end
end

print("")
print("Thanks for playing!")
```

## Step 7: Run Your Program

```bash
python Tourmaline.py guessing_game.trm
```

## Example Game Session

```
========================================
  WELCOME TO THE NUMBER GUESSING GAME!
========================================

I'm thinking of a number between 1 and 100.
Can you guess what it is?

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
Too high! Try again.

Enter your guess: 31
Too low! Try again.

Enter your guess: 34

Congratulations! You guessed it!
The number was 34
It took you 5 attempts.

Thanks for playing!
```

## What You Learned

This program demonstrates:

✓ **Importing libraries** (`import random`)  
✓ **Variables** (`let secret_number = ...`)  
✓ **Random number generation** (`random.randint()`)  
✓ **User input** (`input()`)  
✓ **Type conversion** (`int()`)  
✓ **Exception handling** (`try/except`)  
✓ **Loops** (`while`)  
✓ **Conditionals** (`if/elif/else`)  
✓ **Comparison operators** (`<`, `>`, `==`)  
✓ **String concatenation** (`+`)  

## Improvements & Challenges

Try enhancing your game:

### Challenge 1: Add Difficulty Levels

```python
print("Choose difficulty:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

let choice = input("Enter choice: ")

if choice == "1"
    let secret_number = random.randint(1, 50)
elif choice == "2"
    let secret_number = random.randint(1, 100)
else
    let secret_number = random.randint(1, 500)
end
```

### Challenge 2: Limit the Number of Attempts

```python
let max_attempts = 10
let attempts = 0

while attempts < max_attempts and game_over == false
    # Game logic here
    attempts += 1
    
    if game_over == false
        let remaining = max_attempts - attempts
        print("Attempts remaining: " + str(remaining))
    end
end

if game_over == false
    print("Game Over! The number was " + str(secret_number))
end
```

### Challenge 3: Add a Hint System

```python
function give_hint(number)
    if number % 2 == 0
        print("Hint: The number is even")
    else
        print("Hint: The number is odd")
    end
end

# In the game loop, after 5 attempts:
if attempts == 5
    print("Here's a hint:")
    give_hint(secret_number)
end
```

### Challenge 4: Play Again Feature

```python
let playing = true

while playing
    # [Entire game code here]
    
    print("")
    let again = input("Play again? (yes/no): ")
    
    if again == "yes" or again == "y"
        print("")
        secret_number = random.randint(1, 100)
        attempts = 0
        game_over = false
    else
        playing = false
        print("Thanks for playing!")
    end
end
```

## More Project Ideas

Now that you've built your first program, try these:

### Simple Calculator

```python
function add(a, b)
    return a + b
end

function subtract(a, b)
    return a - b
end

function multiply(a, b)
    return a * b
end

function divide(a, b)
    if b == 0
        print("Error: Cannot divide by zero")
        return nil
    end
    return a / b
end

print("=== Simple Calculator ===")
let num1 = float(input("Enter first number: "))
let num2 = float(input("Enter second number: "))

print("\nResults:")
print("Sum: " + str(add(num1, num2)))
print("Difference: " + str(subtract(num1, num2)))
print("Product: " + str(multiply(num1, num2)))
print("Quotient: " + str(divide(num1, num2)))
```

### Todo List Manager

```python
let todos = []

function show_menu()
    print("\n=== TODO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
end

let running = true

while running
    show_menu()
    let choice = input("\nChoice: ")
    
    if choice == "1"
        let task = input("Enter task: ")
        append(todos, task)
        print("Task added!")
    elif choice == "2"
        print("\nYour tasks:")
        let i = 1
        for task in todos
            print(str(i) + ". " + task)
            i += 1
        end
    elif choice == "3"
        let index = int(input("Task number to remove: "))
        pop(todos, index - 1)
        print("Task removed!")
    elif choice == "4"
        running = false
        print("Goodbye!")
    else
        print("Invalid choice!")
    end
end
```

### Rock, Paper, Scissors

```python
import random

let choices = ["rock", "paper", "scissors"]
let player_score = 0
let computer_score = 0

while true
    print("\n=== ROCK, PAPER, SCISSORS ===")
    print("Score - You: " + str(player_score) + " | Computer: " + str(computer_score))
    
    let player = input("\nYour choice (rock/paper/scissors/quit): ")
    
    if player == "quit"
        break
    end
    
    let computer = random.choice(choices)
    print("Computer chose: " + computer)
    
    if player == computer
        print("It's a tie!")
    elif player == "rock" and computer == "scissors"
        print("You win! Rock beats scissors.")
        player_score += 1
    elif player == "paper" and computer == "rock"
        print("You win! Paper beats rock.")
        player_score += 1
    elif player == "scissors" and computer == "paper"
        print("You win! Scissors beats paper.")
        player_score += 1
    else
        print("Computer wins!")
        computer_score += 1
    end
end

print("\nFinal Score - You: " + str(player_score) + " | Computer: " + str(computer_score))
```

## Debugging Tips

### Common Issues

**Problem:** `Undefined variable` error
```python
# Wrong:
print(name)  # name not declared

# Right:
let name = "Alice"
print(name)
```

**Problem:** Type conversion errors
```python
# Wrong:
let age = input("Age: ")
if age > 18  # age is a string!

# Right:
let age_str = input("Age: ")
let age = int(age_str)
if age > 18
```

**Problem:** Infinite loops
```python
# Wrong:
while true
    print("Forever!")
end

# Right:
let running = true
while running
    let choice = input("Continue? (yes/no): ")
    if choice == "no"
        running = false
    end
end
```

## Next Steps

Congratulations on building your first Tourmaline program! Continue learning:

- **[Language Guide](../guide/variables.md)** - Deep dive into all features
- **[Standard Library](../stdlib/builtins.md)** - Explore built-in functions
- **[Examples](../examples/basic.md)** - More code examples
- **[Advanced Examples](../examples/advanced.md)** - Complex programs

---

!!! success
    You're now a Tourmaline programmer! Keep practicing and building projects to improve your skills.