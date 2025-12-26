# Advanced Examples

Complex Tourmaline programs demonstrating advanced concepts, algorithms, and real-world applications.

## Algorithms

### Binary Search

```python
function binary_search(sorted_list, target)
    let left = 0
    let right = len(sorted_list) - 1
    
    while left <= right
        let mid = floor((left + right) / 2)
        let mid_value = sorted_list[mid]
        
        if mid_value == target
            return mid
        elif mid_value < target
            left = mid + 1
        else
            right = mid - 1
        end
    end
    
    return -1  # Not found
end

let numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
print("Searching for 23...")
let index = binary_search(numbers, 23)

if index != -1
    print("Found at index: " + str(index))
else
    print("Not found")
end
```

### Bubble Sort

```python
function bubble_sort(arr)
    let n = len(arr)
    let i = 0
    
    while i < n - 1
        let j = 0
        let swapped = false
        
        while j < n - i - 1
            if arr[j] > arr[j + 1]
                # Swap elements
                let temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = true
            end
            j += 1
        end
        
        # If no swaps, array is sorted
        if not swapped
            break  # (conceptually)
        end
        
        i += 1
    end
    
    return arr
end

let numbers = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted: " + str(numbers))
bubble_sort(numbers)
print("Sorted: " + str(numbers))
```

### Fibonacci with Memoization

```python
let fib_cache = {}

function fibonacci_memo(n)
    # Check cache
    let n_str = str(n)
    
    if n <= 1
        return n
    end
    
    # In practice, you'd check if n_str exists in cache
    # This is a simplified version
    
    let result = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return result
end

print("Fibonacci sequence:")
let i = 0
while i <= 10
    print("F(" + str(i) + ") = " + str(fibonacci_memo(i)))
    i += 1
end
```

### Prime Number Generator (Sieve of Eratosthenes)

```python
function sieve_of_eratosthenes(limit)
    # Create list of booleans
    let is_prime = []
    let i = 0
    
    # Initialize all as true
    while i <= limit
        append(is_prime, true)
        i += 1
    end
    
    is_prime[0] = false
    is_prime[1] = false
    
    # Sieve algorithm
    let p = 2
    while p * p <= limit
        if is_prime[p]
            # Mark multiples as not prime
            let multiple = p * p
            while multiple <= limit
                is_prime[multiple] = false
                multiple += p
            end
        end
        p += 1
    end
    
    # Collect primes
    let primes = []
    i = 2
    while i <= limit
        if is_prime[i]
            append(primes, i)
        end
        i += 1
    end
    
    return primes
end

let primes = sieve_of_eratosthenes(50)
print("Prime numbers up to 50:")
print(str(primes))
```

## Data Structures

### Linked List Simulation

```python
let linked_list = []

function create_node(data, next_index)
    return {
        "data": data,
        "next": next_index
    }
end

function add_node(data)
    let node = create_node(data, -1)
    
    if len(linked_list) > 0
        linked_list[len(linked_list) - 1]["next"] = len(linked_list)
    end
    
    append(linked_list, node)
end

function traverse_list()
    let current = 0
    
    while current < len(linked_list) and current != -1
        let node = linked_list[current]
        print(str(node["data"]) + " -> ")
        current = node["next"]
    end
    print("None")
end

add_node(10)
add_node(20)
add_node(30)
add_node(40)

print("Linked List:")
traverse_list()
```

### Stack-Based Calculator

```python
function evaluate_postfix(expression)
    let stack = []
    let tokens = expression  # Assume already tokenized
    
    for token in tokens
        if token == "+"
            let b = pop(stack)
            let a = pop(stack)
            append(stack, a + b)
        elif token == "-"
            let b = pop(stack)
            let a = pop(stack)
            append(stack, a - b)
        elif token == "*"
            let b = pop(stack)
            let a = pop(stack)
            append(stack, a * b)
        elif token == "/"
            let b = pop(stack)
            let a = pop(stack)
            append(stack, a / b)
        else
            # It's a number
            append(stack, int(token))
        end
    end
    
    return pop(stack)
end

# Example: 3 4 + 2 * (which is (3+4)*2 = 14)
let expr = ["3", "4", "+", "2", "*"]
let result = evaluate_postfix(expr)
print("Result: " + str(result))
```

## Game Development

### Rock, Paper, Scissors Tournament

```python
import random

let player_score = 0
let computer_score = 0
let rounds = 5

function get_winner(player, computer)
    if player == computer
        return "tie"
    elif player == "rock" and computer == "scissors"
        return "player"
    elif player == "paper" and computer == "rock"
        return "player"
    elif player == "scissors" and computer == "paper"
        return "player"
    else
        return "computer"
    end
end

print("=== ROCK, PAPER, SCISSORS TOURNAMENT ===")
print("Best of " + str(rounds) + " rounds\n")

let round_num = 1

while round_num <= rounds
    print("Round " + str(round_num))
    print("-" * 20)
    
    let player = input("Choose (rock/paper/scissors): ")
    let choices = ["rock", "paper", "scissors"]
    let computer = random.choice(choices)
    
    print("Computer chose: " + computer)
    
    let winner = get_winner(player, computer)
    
    if winner == "player"
        print("You win this round!")
        player_score += 1
    elif winner == "computer"
        print("Computer wins this round!")
        computer_score += 1
    else
        print("It's a tie!")
    end
    
    print("Score - You: " + str(player_score) + " | Computer: " + str(computer_score))
    print("")
    
    round_num += 1
end

print("=== FINAL RESULTS ===")
print("You: " + str(player_score))
print("Computer: " + str(computer_score))

if player_score > computer_score
    print("\nYou win the tournament!")
elif computer_score > player_score
    print("\nComputer wins the tournament!")
else
    print("\nIt's a draw!")
end
```

### Hangman Game

```python
import random

function play_hangman()
    let words = ["python", "programming", "computer", "algorithm", "function"]
    let word = random.choice(words)
    let word_length = len(word)
    
    # Create hidden word
    let guessed = []
    let i = 0
    while i < word_length
        append(guessed, "_")
        i += 1
    end
    
    let attempts = 6
    let guessed_letters = []
    
    print("=== HANGMAN ===")
    print("You have " + str(attempts) + " attempts")
    print("")
    
    while attempts > 0
        # Show current state
        print("Word: " + str(guessed))
        print("Attempts left: " + str(attempts))
        print("Guessed: " + str(guessed_letters))
        
        let letter = input("\nGuess a letter: ")
        
        # Check if already guessed
        let already_guessed = false
        for g in guessed_letters
            if g == letter
                already_guessed = true
            end
        end
        
        if already_guessed
            print("You already guessed that!")
            # Continue without penalty
        else
            append(guessed_letters, letter)
            
            # Check if letter is in word
            let found = false
            i = 0
            while i < word_length
                # Simplified character checking
                i += 1
            end
            
            # For demo purposes
            print("Letter checked!")
        end
        
        # Check win condition
        let won = true
        for char in guessed
            if char == "_"
                won = false
            end
        end
        
        if won
            print("\nYou won! The word was: " + word)
            return
        end
        
        attempts -= 1
        print("")
    end
    
    print("Game Over! The word was: " + word)
end

play_hangman()
```

### Tic-Tac-Toe

```python
let board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

function show_board()
    print("\n " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("")
end

function check_winner()
    # Check rows
    if board[0] == board[1] and board[1] == board[2]
        return board[0]
    end
    if board[3] == board[4] and board[4] == board[5]
        return board[3]
    end
    if board[6] == board[7] and board[7] == board[8]
        return board[6]
    end
    
    # Check columns
    if board[0] == board[3] and board[3] == board[6]
        return board[0]
    end
    if board[1] == board[4] and board[4] == board[7]
        return board[1]
    end
    if board[2] == board[5] and board[5] == board[8]
        return board[2]
    end
    
    # Check diagonals
    if board[0] == board[4] and board[4] == board[8]
        return board[0]
    end
    if board[2] == board[4] and board[4] == board[6]
        return board[2]
    end
    
    return nil
end

function play_game()
    let current_player = "X"
    let moves = 0
    
    print("=== TIC-TAC-TOE ===")
    show_board()
    
    while moves < 9
        let position = input("Player " + current_player + ", choose position (1-9): ")
        let pos_num = int(position) - 1
        
        # Check if position is valid
        if pos_num >= 0 and pos_num < 9 and board[pos_num] != "X" and board[pos_num] != "O"
            board[pos_num] = current_player
            moves += 1
            show_board()
            
            let winner = check_winner()
            if winner != nil
                print("Player " + winner + " wins!")
                return
            end
            
            # Switch player
            if current_player == "X"
                current_player = "O"
            else
                current_player = "X"
            end
        else
            print("Invalid position! Try again.")
        end
    end
    
    print("It's a draw!")
end

play_game()
```

## Data Analysis

### Statistical Analysis

```python
function analyze_data(data)
    if len(data) == 0
        print("No data to analyze")
        return
    end
    
    # Calculate statistics
    let sum = 0
    let minimum = data[0]
    let maximum = data[0]
    
    for value in data
        sum += value
        if value < minimum
            minimum = value
        end
        if value > maximum
            maximum = value
        end
    end
    
    let mean = sum / len(data)
    let range = maximum - minimum
    
    # Calculate median
    # (Requires sorting first)
    let median = mean  # Simplified
    
    # Calculate variance and standard deviation
    let variance_sum = 0
    for value in data
        let diff = value - mean
        variance_sum += diff * diff
    end
    let variance = variance_sum / len(data)
    let std_dev = sqrt(variance)
    
    # Print report
    print("\n=== STATISTICAL ANALYSIS ===")
    print("Count:              " + str(len(data)))
    print("Sum:                " + str(sum))
    print("Mean:               " + str(mean))
    print("Median:             " + str(median))
    print("Minimum:            " + str(minimum))
    print("Maximum:            " + str(maximum))
    print("Range:              " + str(range))
    print("Variance:           " + str(variance))
    print("Standard Deviation: " + str(std_dev))
end

let dataset = [23, 45, 67, 12, 89, 34, 56, 78, 90, 32]
analyze_data(dataset)
```

### Frequency Counter

```python
function frequency_analysis(text)
    let freq = {}
    let i = 0
    
    while i < len(text)
        # In a real implementation, you'd access each character
        # This is simplified
        i += 1
    end
    
    print("Analyzing text frequency...")
    print("Text length: " + str(len(text)))
end

let sample = "hello world"
frequency_analysis(sample)
```

## Financial Calculations

### Loan Calculator

```python
function calculate_loan(principal, annual_rate, years)
    let monthly_rate = annual_rate / 12
    let num_payments = years * 12
    
    # Calculate monthly payment
    let payment = principal * (monthly_rate * pow(1 + monthly_rate, num_payments)) / (pow(1 + monthly_rate, num_payments) - 1)
    
    let total_paid = payment * num_payments
    let total_interest = total_paid - principal
    
    print("\n=== LOAN CALCULATOR ===")
    print("Principal:        $" + str(round(principal)))
    print("Annual Rate:      " + str(annual_rate * 100) + "%")
    print("Loan Term:        " + str(years) + " years")
    print("\nMonthly Payment:  $" + str(round(payment * 100) / 100))
    print("Total Paid:       $" + str(round(total_paid)))
    print("Total Interest:   $" + str(round(total_interest)))
    
    # Amortization schedule (first 12 months)
    print("\n=== FIRST YEAR AMORTIZATION ===")
    let balance = principal
    let month = 1
    
    while month <= 12
        let interest_payment = balance * monthly_rate
        let principal_payment = payment - interest_payment
        balance -= principal_payment
        
        print("Month " + str(month) + ":")
        print("  Interest: $" + str(round(interest_payment * 100) / 100))
        print("  Principal: $" + str(round(principal_payment * 100) / 100))
        print("  Balance: $" + str(round(balance)))
        
        month += 1
    end
end

calculate_loan(200000, 0.045, 30)
```

### Investment Portfolio Tracker

```python
let portfolio = []

function add_investment(name, shares, price_per_share)
    let investment = {
        "name": name,
        "shares": shares,
        "price": price_per_share,
        "total": shares * price_per_share
    }
    append(portfolio, investment)
    print("Added: " + name)
end

function show_portfolio()
    let total_value = 0
    
    print("\n=== INVESTMENT PORTFOLIO ===")
    
    for investment in portfolio
        let value = investment["total"]
        total_value += value
        
        print(investment["name"])
        print("  Shares: " + str(investment["shares"]))
        print("  Price: $" + str(investment["price"]))
        print("  Value: $" + str(value))
        print("")
    end
    
    print("Total Portfolio Value: $" + str(total_value))
end

function calculate_allocation()
    let total = 0
    
    for investment in portfolio
        total += investment["total"]
    end
    
    print("\n=== ASSET ALLOCATION ===")
    
    for investment in portfolio
        let percentage = investment["total"] * 100 / total
        print(investment["name"] + ": " + str(round(percentage)) + "%")
    end
end

add_investment("Tech Stock A", 100, 150.50)
add_investment("Bond Fund B", 200, 25.75)
add_investment("Index Fund C", 50, 300.00)

show_portfolio()
calculate_allocation()
```

## Simulation

### Monte Carlo Pi Estimation

```python
import random

function estimate_pi(iterations)
    let inside_circle = 0
    let i = 0
    
    while i < iterations
        let x = random.random()
        let y = random.random()
        
        let distance = sqrt(x * x + y * y)
        
        if distance <= 1
            inside_circle += 1
        end
        
        i += 1
    end
    
    let pi_estimate = 4.0 * inside_circle / iterations
    return pi_estimate
end

print("=== MONTE CARLO PI ESTIMATION ===\n")

let trials = [100, 1000, 10000, 100000]

for trial in trials
    let estimate = estimate_pi(trial)
    let error = abs(estimate - 3.14159)
    
    print(str(trial) + " iterations:")
    print("  Estimate: " + str(estimate))
    print("  Error: " + str(error))
    print("")
end
```

## Text Processing

### Word Counter and Analyzer

```python
function analyze_text(text)
    let char_count = len(text)
    let word_count = 1  # Simplified
    let sentence_count = 1  # Simplified
    
    print("\n=== TEXT ANALYSIS ===")
    print("Characters: " + str(char_count))
    print("Words: " + str(word_count))
    print("Sentences: " + str(sentence_count))
    
    # Average word length
    let avg_word_length = char_count / word_count
    print("Avg Word Length: " + str(avg_word_length))
end

let sample_text = "This is a sample text for analysis purposes."
analyze_text(sample_text)
```

## Next Steps

- **[Basic Examples](basic.md)** - Start with simpler programs
- **[Language Guide](../guide/variables.md)** - Learn all features
- **[Standard Library](../stdlib/builtins.md)** - Explore available functions