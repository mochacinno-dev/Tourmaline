# Random Library

The random library provides functions for generating random numbers and making random selections.

## Importing the Library

```python
import random
```

!!! note
    You must import the random library before using any of its functions.

## Functions

### `random.randint()`

Generate a random integer between two values (inclusive).

**Syntax:**
```python
random.randint(a, b)
```

**Parameters:**
- `a`: Minimum value (inclusive)
- `b`: Maximum value (inclusive)

**Returns:** Random integer between a and b

**Examples:**
```python
import random

# Random number from 1 to 10
let num = random.randint(1, 10)
print(num)  # Could be 1, 2, 3, ..., 10

# Dice roll
let dice = random.randint(1, 6)
print("You rolled: " + str(dice))

# Random year
let year = random.randint(1900, 2024)
print(year)
```

---

### `random.random()`

Generate a random float between 0.0 and 1.0.

**Syntax:**
```python
random.random()
```

**Returns:** Random float in range [0.0, 1.0)

**Examples:**
```python
import random

let value = random.random()
print(value)  # e.g., 0.7234...

# Random percentage
let percent = random.random() * 100
print(str(percent) + "%")

# Random probability check
let chance = random.random()
if chance < 0.5
    print("Heads")
else
    print("Tails")
end
```

---

### `random.choice()`

Select a random element from a list.

**Syntax:**
```python
random.choice(list)
```

**Parameters:**
- `list`: List to choose from

**Returns:** Random element from the list

**Examples:**
```python
import random

let fruits = ["apple", "banana", "cherry", "date"]
let fruit = random.choice(fruits)
print("Selected: " + fruit)

# Random color
let colors = ["red", "blue", "green", "yellow"]
let color = random.choice(colors)
print("Color: " + color)

# Random greeting
let greetings = ["Hello", "Hi", "Hey", "Greetings"]
let greeting = random.choice(greetings)
print(greeting + "!")
```

---

### `random.uniform()`

Generate a random float between two values.

**Syntax:**
```python
random.uniform(a, b)
```

**Parameters:**
- `a`: Minimum value
- `b`: Maximum value

**Returns:** Random float between a and b

**Examples:**
```python
import random

# Random temperature
let temp = random.uniform(15.0, 30.0)
print("Temperature: " + str(temp) + "°C")

# Random price
let price = random.uniform(9.99, 99.99)
print("Price: $" + str(price))

# Random weight
let weight = random.uniform(0.5, 2.5)
print("Weight: " + str(weight) + " kg")
```

---

### `random.randrange()`

Generate a random integer from a range with optional step.

**Syntax:**
```python
random.randrange(start, stop, step)
random.randrange(start, stop)
random.randrange(stop)
```

**Parameters:**
- `start`: Starting value (default: 0)
- `stop`: Stopping value (exclusive)
- `step`: Step size (default: 1)

**Returns:** Random integer from the range

**Examples:**
```python
import random

# Random number from 0 to 9
let num1 = random.randrange(10)
print(num1)

# Random number from 5 to 14
let num2 = random.randrange(5, 15)
print(num2)

# Random even number from 0 to 98
let even = random.randrange(0, 100, 2)
print(even)

# Random multiple of 5
let mult5 = random.randrange(0, 100, 5)
print(mult5)  # 0, 5, 10, 15, ..., 95
```

---

### `random.shuffle()`

Shuffle a list in place.

**Syntax:**
```python
random.shuffle(list)
```

**Parameters:**
- `list`: List to shuffle

**Returns:** The shuffled list

**Examples:**
```python
import random

let cards = ["A", "K", "Q", "J", "10"]
let shuffled = random.shuffle(cards)
print(shuffled)  # Cards in random order

# Shuffle again
let cards2 = ["1", "2", "3", "4", "5"]
random.shuffle(cards2)
print(cards2)  # Different order
```

---

## Practical Examples

### Dice Roller

```python
import random

function roll_dice(num_dice, sides)
    print("Rolling " + str(num_dice) + "d" + str(sides) + ":")
    
    let total = 0
    let i = 1
    
    while i <= num_dice
        let roll = random.randint(1, sides)
        print("  Die " + str(i) + ": " + str(roll))
        total += roll
        i += 1
    end
    
    print("Total: " + str(total))
    return total
end

roll_dice(2, 6)   # Roll 2d6
roll_dice(3, 20)  # Roll 3d20
```

### Random Password Generator

```python
import random

function generate_password(length)
    let chars = ["a", "b", "c", "d", "e", "f", "g", "h",
                 "A", "B", "C", "D", "E", "F", "G", "H",
                 "1", "2", "3", "4", "5", "6", "7", "8"]
    
    let password = ""
    let i = 0
    
    while i < length
        let char = random.choice(chars)
        password = password + char
        i += 1
    end
    
    return password
end

let pwd = generate_password(12)
print("Generated password: " + pwd)
```

### Lottery Number Generator

```python
import random

function generate_lottery_numbers(count, max_number)
    let numbers = []
    
    while len(numbers) < count
        let num = random.randint(1, max_number)
        
        # Check if number already exists
        let exists = false
        for n in numbers
            if n == num
                exists = true
            end
        end
        
        if not exists
            append(numbers, num)
        end
    end
    
    return numbers
end

let lottery = generate_lottery_numbers(6, 49)
print("Your lottery numbers: " + str(lottery))
```

### Random Quiz Question Selector

```python
import random

let questions = [
    {"q": "What is 2+2?", "a": "4"},
    {"q": "What is 5*3?", "a": "15"},
    {"q": "What is 10/2?", "a": "5"},
    {"q": "What is 7-3?", "a": "4"}
]

function ask_random_question()
    let question = random.choice(questions)
    
    print("Question: " + question["q"])
    let answer = input("Your answer: ")
    
    if answer == question["a"]
        print("Correct!")
        return true
    else
        print("Wrong! The answer is " + question["a"])
        return false
    end
end

ask_random_question()
```

### Random Walk Simulator

```python
import random

function random_walk(steps)
    let x = 0
    let y = 0
    
    print("Starting at (0, 0)")
    
    let i = 0
    while i < steps
        let direction = random.randint(1, 4)
        
        if direction == 1
            y += 1
            print("Step " + str(i + 1) + ": North")
        elif direction == 2
            y -= 1
            print("Step " + str(i + 1) + ": South")
        elif direction == 3
            x += 1
            print("Step " + str(i + 1) + ": East")
        else
            x -= 1
            print("Step " + str(i + 1) + ": West")
        end
        
        i += 1
    end
    
    print("\nFinal position: (" + str(x) + ", " + str(y) + ")")
    
    # Calculate distance from origin
    let distance = sqrt(x * x + y * y)
    print("Distance from start: " + str(distance))
end

random_walk(10)
```

### Card Deck Shuffler

```python
import random

function create_deck()
    let suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    let ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    let deck = []
    
    for suit in suits
        for rank in ranks
            let card = rank + " of " + suit
            append(deck, card)
        end
    end
    
    return deck
end

function deal_hand(deck, cards)
    let hand = []
    let i = 0
    
    while i < cards
        let card = random.choice(deck)
        append(hand, card)
        i += 1
    end
    
    return hand
end

let deck = create_deck()
print("Deck created with " + str(len(deck)) + " cards")

let hand = deal_hand(deck, 5)
print("\nYour hand:")
for card in hand
    print("  " + card)
end
```

### Random Event Generator

```python
import random

function random_event()
    let events = [
        "You found a treasure chest!",
        "A wild monster appeared!",
        "You discovered a hidden path.",
        "It started raining.",
        "You met a friendly traveler.",
        "Nothing interesting happened."
    ]
    
    let weights = [5, 20, 15, 25, 15, 20]  # Probability weights
    
    # Simple weighted selection
    let total = 100
    let roll = random.randint(1, total)
    
    if roll <= 5
        return events[0]
    elif roll <= 25
        return events[1]
    elif roll <= 40
        return events[2]
    elif roll <= 65
        return events[3]
    elif roll <= 80
        return events[4]
    else
        return events[5]
    end
end

print("=== ADVENTURE GAME ===")
let i = 1
while i <= 5
    print("\nStep " + str(i) + ": " + random_event())
    i += 1
end
```

### Monte Carlo Simulation

```python
import random

function estimate_pi(iterations)
    let inside_circle = 0
    let i = 0
    
    while i < iterations
        let x = random.random()
        let y = random.random()
        
        # Check if point is inside quarter circle
        if x * x + y * y <= 1
            inside_circle += 1
        end
        
        i += 1
    end
    
    # Estimate pi
    let pi_estimate = 4.0 * inside_circle / iterations
    return pi_estimate
end

print("Estimating pi with Monte Carlo method...")
print("10,000 iterations: " + str(estimate_pi(10000)))
```

### Random Color Generator

```python
import random

function random_hex_color()
    let hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", 
                     "8", "9", "A", "B", "C", "D", "E", "F"]
    
    let color = "#"
    let i = 0
    
    while i < 6
        let char = random.choice(hex_chars)
        color = color + char
        i += 1
    end
    
    return color
end

print("Random colors:")
let i = 1
while i <= 5
    print(str(i) + ". " + random_hex_color())
    i += 1
end
```

## Common Patterns

### Random Choice with Weights

```python
import random

function weighted_choice()
    let roll = random.randint(1, 100)
    
    if roll <= 50
        return "Common"     # 50% chance
    elif roll <= 80
        return "Uncommon"   # 30% chance
    elif roll <= 95
        return "Rare"       # 15% chance
    else
        return "Legendary"  # 5% chance
    end
end

print(weighted_choice())
```

### Random Range with Decimals

```python
import random

# Random float between a and b with n decimal places
function random_decimal(a, b, decimals)
    let value = random.uniform(a, b)
    let multiplier = pow(10, decimals)
    return round(value * multiplier) / multiplier
end

print(random_decimal(0, 100, 2))  # e.g., 45.73
```

### Random Sample (Multiple Choices)

```python
import random

function random_sample(list, count)
    let result = []
    let available = []
    
    # Copy list
    for item in list
        append(available, item)
    end
    
    while len(result) < count and len(available) > 0
        let item = random.choice(available)
        append(result, item)
        remove(available, item)
    end
    
    return result
end

let items = ["A", "B", "C", "D", "E"]
let sample = random_sample(items, 3)
print(sample)  # e.g., ["C", "A", "E"]
```

## Tips & Best Practices

!!! tip "Seed for Reproducibility"
    Tourmaline's random library doesn't expose seeding, but be aware that random numbers are pseudo-random and follow a sequence.

!!! tip "Use Appropriate Functions"
    - Use `randint()` for discrete integers
    - Use `uniform()` for continuous ranges
    - Use `choice()` for selecting from lists

!!! warning "List Mutation"
    `shuffle()` modifies the list in place:
    ```python
    let original = [1, 2, 3]
    random.shuffle(original)
    # original is now shuffled
    ```

!!! tip "Random != Fair"
    Random selections can produce unexpected patterns. Over many iterations, distribution should be even.

## Next Steps

- **[Built-in Functions](builtins.md)** - Core functions
- **[Math Functions](math.md)** - Mathematical operations
- **[Examples](../examples/basic.md)** - See random in action