# Lists & Dictionaries

Learn how to work with collections in Tourmaline: lists for ordered sequences and dictionaries for key-value pairs.

## Lists

Lists store ordered collections of items.

### Creating Lists

```python
# Empty list
let empty_list = []

# List with items
let numbers = [1, 2, 3, 4, 5]
let fruits = ["apple", "banana", "cherry"]

# Mixed types
let mixed = [1, "hello", true, 3.14]

# Nested lists
let matrix = [[1, 2], [3, 4], [5, 6]]
```

### Accessing Elements

Lists use zero-based indexing:

```python
let fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])  # apple (first item)
print(fruits[1])  # banana
print(fruits[2])  # cherry
print(fruits[3])  # date (last item)
```

**Negative Indexing:**
```python
let fruits = ["apple", "banana", "cherry"]

print(fruits[-1])  # cherry (last item)
# Note: Negative indexing might not be fully supported
```

### List Length

```python
let fruits = ["apple", "banana", "cherry"]
let count = len(fruits)
print(count)  # 3

# Check if empty
if len(fruits) > 0
    print("List has items")
end
```

### Modifying Lists

#### Update Element

```python
let fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ["apple", "blueberry", "cherry"]
```

## List Operations

### Adding Elements

#### `append()` - Add to End

```python
let fruits = ["apple", "banana"]
append(fruits, "cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# Add multiple items
append(fruits, "date")
append(fruits, "elderberry")
print(fruits)  # ["apple", "banana", "cherry", "date", "elderberry"]
```

#### `insert()` - Add at Position

```python
let fruits = ["apple", "cherry"]
insert(fruits, 1, "banana")  # Insert at index 1
print(fruits)  # ["apple", "banana", "cherry"]

# Insert at beginning
insert(fruits, 0, "apricot")
print(fruits)  # ["apricot", "apple", "banana", "cherry"]
```

### Removing Elements

#### `remove()` - Remove by Value

```python
let fruits = ["apple", "banana", "cherry", "banana"]
remove(fruits, "banana")  # Removes first occurrence
print(fruits)  # ["apple", "cherry", "banana"]
```

#### `pop()` - Remove by Index

```python
let fruits = ["apple", "banana", "cherry"]

# Remove last item
let last = pop(fruits)
print(last)    # cherry
print(fruits)  # ["apple", "banana"]

# Remove specific index
let first = pop(fruits, 0)
print(first)   # apple
print(fruits)  # ["banana"]
```

#### `clear()` - Remove All

```python
let fruits = ["apple", "banana", "cherry"]
clear(fruits)
print(fruits)  # []
print(len(fruits))  # 0
```

## Iterating Over Lists

### For Loop

```python
let fruits = ["apple", "banana", "cherry"]

for fruit in fruits
    print("I like " + fruit)
end
```

### With Index

```python
let fruits = ["apple", "banana", "cherry"]
let index = 0

for fruit in fruits
    index += 1
    print(str(index) + ". " + fruit)
end
```

### While Loop

```python
let fruits = ["apple", "banana", "cherry"]
let i = 0

while i < len(fruits)
    print(fruits[i])
    i += 1
end
```

## List Algorithms

### Sum of List

```python
function sum_list(numbers)
    let total = 0
    for num in numbers
        total += num
    end
    return total
end

let nums = [10, 20, 30, 40, 50]
print(sum_list(nums))  # 150
```

### Find Maximum

```python
function find_max(numbers)
    if len(numbers) == 0
        return nil
    end
    
    let maximum = numbers[0]
    for num in numbers
        if num > maximum
            maximum = num
        end
    end
    return maximum
end

let nums = [23, 67, 12, 89, 45]
print(find_max(nums))  # 89
```

### Find Minimum

```python
function find_min(numbers)
    if len(numbers) == 0
        return nil
    end
    
    let minimum = numbers[0]
    for num in numbers
        if num < minimum
            minimum = num
        end
    end
    return minimum
end

let nums = [23, 67, 12, 89, 45]
print(find_min(nums))  # 12
```

### Average

```python
function average(numbers)
    if len(numbers) == 0
        return 0
    end
    
    let total = 0
    for num in numbers
        total += num
    end
    
    return total / len(numbers)
end

let scores = [85, 92, 78, 90, 88]
print(average(scores))  # 86.6
```

### Search for Item

```python
function contains(list, item)
    for element in list
        if element == item
            return true
        end
    end
    return false
end

let fruits = ["apple", "banana", "cherry"]
print(contains(fruits, "banana"))  # true
print(contains(fruits, "grape"))   # false
```

### Count Occurrences

```python
function count_item(list, target)
    let count = 0
    for item in list
        if item == target
            count += 1
        end
    end
    return count
end

let numbers = [1, 2, 3, 2, 4, 2, 5]
print(count_item(numbers, 2))  # 3
```

### Filter List

```python
function filter_positive(numbers)
    let result = []
    for num in numbers
        if num > 0
            append(result, num)
        end
    end
    return result
end

let nums = [-3, 5, -1, 0, 8, -7, 2]
let positives = filter_positive(nums)
print(positives)  # [5, 8, 2]
```

### Reverse List

```python
function reverse_list(list)
    let result = []
    let i = len(list) - 1
    
    while i >= 0
        append(result, list[i])
        i -= 1
    end
    
    return result
end

let nums = [1, 2, 3, 4, 5]
let reversed = reverse_list(nums)
print(reversed)  # [5, 4, 3, 2, 1]
```

## Dictionaries

Dictionaries store key-value pairs.

### Creating Dictionaries

```python
# Empty dictionary
let empty_dict = {}

# Dictionary with values
let person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Numbers as values
let scores = {
    "math": 95,
    "english": 87,
    "science": 92
}
```

### Accessing Values

```python
let person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(person["name"])  # Alice
print(person["age"])   # 30
print(person["city"])  # New York
```

### Modifying Dictionaries

```python
let person = {
    "name": "Alice",
    "age": 30
}

# Update existing value
person["age"] = 31

# Add new key-value pair
person["email"] = "alice@example.com"

print(person)
# {"name": "Alice", "age": 31, "email": "alice@example.com"}
```

### Dictionary with Various Types

```python
let config = {
    "debug": true,
    "port": 8080,
    "host": "localhost",
    "timeout": 30.5,
    "features": ["auth", "api", "db"]
}

print(config["debug"])     # true
print(config["port"])      # 8080
print(config["features"])  # ["auth", "api", "db"]
```

## Nested Collections

### List of Dictionaries

```python
let students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

for student in students
    let name = student["name"]
    let grade = student["grade"]
    print(name + ": " + str(grade))
end
```

### Dictionary with Lists

```python
let inventory = {
    "fruits": ["apple", "banana", "orange"],
    "vegetables": ["carrot", "lettuce", "tomato"],
    "dairy": ["milk", "cheese", "yogurt"]
}

print("Fruits:")
for fruit in inventory["fruits"]
    print("  - " + fruit)
end
```

### Nested Dictionaries

```python
let company = {
    "name": "TechCorp",
    "address": {
        "street": "123 Main St",
        "city": "Boston",
        "zip": "02101"
    },
    "employees": 150
}

print(company["name"])                    # TechCorp
print(company["address"]["city"])         # Boston
print(company["address"]["street"])       # 123 Main St
```

## Practical Examples

### Contact List Manager

```python
let contacts = []

function add_contact(name, phone, email)
    let contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    append(contacts, contact)
    print("Contact added: " + name)
end

function list_contacts()
    print("\n=== CONTACTS ===")
    let i = 0
    for contact in contacts
        i += 1
        print(str(i) + ". " + contact["name"])
        print("   Phone: " + contact["phone"])
        print("   Email: " + contact["email"])
    end
end

# Add contacts
add_contact("Alice", "555-1234", "alice@email.com")
add_contact("Bob", "555-5678", "bob@email.com")

# List all contacts
list_contacts()
```

### Grade Book

```python
let gradebook = {
    "Alice": [85, 92, 78, 90],
    "Bob": [78, 85, 82, 88],
    "Charlie": [92, 95, 89, 94]
}

function calculate_average_for_student(grades)
    let total = 0
    for grade in grades
        total += grade
    end
    return total / len(grades)
end

print("=== GRADE REPORT ===")

# Note: Direct dictionary iteration requires accessing keys
# This is a simplified example
let alice_avg = calculate_average_for_student(gradebook["Alice"])
let bob_avg = calculate_average_for_student(gradebook["Bob"])
let charlie_avg = calculate_average_for_student(gradebook["Charlie"])

print("Alice: " + str(alice_avg))
print("Bob: " + str(bob_avg))
print("Charlie: " + str(charlie_avg))
```

### Shopping Cart

```python
let cart = []

function add_item(name, price, quantity)
    let item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    append(cart, item)
    print("Added: " + name + " x" + str(quantity))
end

function calculate_total()
    let total = 0
    for item in cart
        let item_total = item["price"] * item["quantity"]
        total += item_total
    end
    return total
end

function show_cart()
    print("\n=== SHOPPING CART ===")
    for item in cart
        let name = item["name"]
        let price = item["price"]
        let qty = item["quantity"]
        let subtotal = price * qty
        
        print(name + " - $" + str(price) + " x " + str(qty) + " = $" + str(subtotal))
    end
    
    print("\nTotal: $" + str(calculate_total()))
end

# Add items to cart
add_item("Apple", 0.99, 5)
add_item("Bread", 2.50, 2)
add_item("Milk", 3.99, 1)

# Show cart
show_cart()
```

### Inventory System

```python
let inventory = {}

function add_product(id, name, quantity, price)
    inventory[id] = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    print("Added product: " + name)
end

function update_quantity(id, change)
    if id in inventory  # Conceptual check
        let product = inventory[id]
        product["quantity"] = product["quantity"] + change
        print("Updated: " + product["name"])
    else
        print("Product not found")
    end
end

# Build inventory
add_product("P001", "Laptop", 10, 999.99)
add_product("P002", "Mouse", 50, 19.99)
add_product("P003", "Keyboard", 30, 79.99)
```

### Data Analysis

```python
let survey_data = [
    {"age": 25, "rating": 5, "satisfied": true},
    {"age": 34, "rating": 4, "satisfied": true},
    {"age": 42, "rating": 3, "satisfied": false},
    {"age": 28, "rating": 5, "satisfied": true},
    {"age": 51, "rating": 2, "satisfied": false}
]

function analyze_survey(data)
    let total_rating = 0
    let satisfied_count = 0
    let total_age = 0
    
    for response in data
        total_rating += response["rating"]
        total_age += response["age"]
        
        if response["satisfied"]
            satisfied_count += 1
        end
    end
    
    let count = len(data)
    let avg_rating = total_rating / count
    let avg_age = total_age / count
    let satisfaction_rate = satisfied_count * 100 / count
    
    print("=== SURVEY ANALYSIS ===")
    print("Responses: " + str(count))
    print("Average Rating: " + str(avg_rating))
    print("Average Age: " + str(avg_age))
    print("Satisfaction Rate: " + str(satisfaction_rate) + "%")
end

analyze_survey(survey_data)
```

## Best Practices

### 1. Use Descriptive Keys

```python
# Less clear
let p = {"n": "Alice", "a": 30}

# More clear
let person = {"name": "Alice", "age": 30}
```

### 2. Check Before Accessing

```python
# Safer dictionary access
let person = {"name": "Alice"}

# Check if key exists (conceptual)
# In practice, use try-except or careful structure
```

### 3. Keep Lists Homogeneous

```python
# Good: Same type
let numbers = [1, 2, 3, 4, 5]
let names = ["Alice", "Bob", "Charlie"]

# Less ideal: Mixed types (use dictionaries instead)
let mixed = [1, "Alice", true]
```

### 4. Use Clear Variable Names

```python
# Less clear
for x in y
    print(x)
end

# More clear
for student in students
    print(student["name"])
end
```

## Common Patterns

### List Comprehension (Manual)

```python
# Double all numbers
let numbers = [1, 2, 3, 4, 5]
let doubled = []

for num in numbers
    append(doubled, num * 2)
end

print(doubled)  # [2, 4, 6, 8, 10]
```

### Dictionary Lookup

```python
let colors = {
    "red": "#FF0000",
    "green": "#00FF00",
    "blue": "#0000FF"
}

let color_name = "red"
let hex_code = colors[color_name]
print(hex_code)  # #FF0000
```

### Frequency Counter

```python
let items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
let counts = {}

# Manual counting (simplified)
# In practice, you'd iterate and check/update counts
```

## Next Steps

- **[Functions](functions.md)** - Pass collections to functions
- **[List Operations](../stdlib/lists.md)** - More list functions
- **[Examples](../examples/basic.md)** - See collections in action