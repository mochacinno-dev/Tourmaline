# List Operations

Tourmaline provides built-in functions for working with lists. These functions help you add, remove, and manage list elements.

## List Functions

### `append()`

Add an item to the end of a list.

**Syntax:**
```python
append(list, item)
```

**Parameters:**
- `list`: The list to modify
- `item`: The item to add

**Returns:** The modified list

**Examples:**
```python
let fruits = ["apple", "banana"]
append(fruits, "cherry")
print(fruits)  # ["apple", "banana", "cherry"]

# Append multiple times
append(fruits, "date")
append(fruits, "elderberry")
print(fruits)  # ["apple", "banana", "cherry", "date", "elderberry"]

# Append different types
let mixed = [1, 2]
append(mixed, "three")
append(mixed, true)
print(mixed)  # [1, 2, "three", true]
```

---

### `insert()`

Insert an item at a specific position.

**Syntax:**
```python
insert(list, index, item)
```

**Parameters:**
- `list`: The list to modify
- `index`: Position to insert at (0-based)
- `item`: The item to insert

**Returns:** The modified list

**Examples:**
```python
let fruits = ["apple", "cherry"]

# Insert at index 1
insert(fruits, 1, "banana")
print(fruits)  # ["apple", "banana", "cherry"]

# Insert at beginning (index 0)
insert(fruits, 0, "apricot")
print(fruits)  # ["apricot", "apple", "banana", "cherry"]

# Insert at end
insert(fruits, len(fruits), "date")
print(fruits)  # ["apricot", "apple", "banana", "cherry", "date"]
```

---

### `remove()`

Remove the first occurrence of an item.

**Syntax:**
```python
remove(list, item)
```

**Parameters:**
- `list`: The list to modify
- `item`: The item to remove

**Returns:** The modified list

**Raises:** Error if item not found

**Examples:**
```python
let fruits = ["apple", "banana", "cherry", "banana"]

# Remove first "banana"
remove(fruits, "banana")
print(fruits)  # ["apple", "cherry", "banana"]

# Remove "apple"
remove(fruits, "apple")
print(fruits)  # ["cherry", "banana"]

# Error if item doesn't exist
try
    remove(fruits, "grape")
except error
    print("Item not found: " + error)
end
```

---

### `pop()`

Remove and return an item at an index.

**Syntax:**
```python
pop(list)           # Remove last item
pop(list, index)    # Remove item at index
```

**Parameters:**
- `list`: The list to modify
- `index`: Position to remove from (optional, default: -1)

**Returns:** The removed item

**Raises:** Error if list is empty or index invalid

**Examples:**
```python
let fruits = ["apple", "banana", "cherry"]

# Remove last item
let last = pop(fruits)
print(last)    # "cherry"
print(fruits)  # ["apple", "banana"]

# Remove first item
let first = pop(fruits, 0)
print(first)   # "apple"
print(fruits)  # ["banana"]

# Remove from middle
let items = ["a", "b", "c", "d", "e"]
let middle = pop(items, 2)
print(middle)  # "c"
print(items)   # ["a", "b", "d", "e"]
```

---

### `clear()`

Remove all items from a list.

**Syntax:**
```python
clear(list)
```

**Parameters:**
- `list`: The list to clear

**Returns:** The empty list

**Examples:**
```python
let fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3

clear(fruits)
print(len(fruits))  # 0
print(fruits)       # []

# Safe to use on empty lists
clear(fruits)
print(fruits)       # []
```

---

## Practical Examples

### Stack Implementation

```python
# Stack (Last In, First Out)
let stack = []

function push(item)
    append(stack, item)
    print("Pushed: " + str(item))
end

function pop_stack()
    if len(stack) > 0
        let item = pop(stack)
        print("Popped: " + str(item))
        return item
    else
        print("Stack is empty")
        return nil
    end
end

function peek()
    if len(stack) > 0
        return stack[len(stack) - 1]
    else
        return nil
    end
end

push(1)
push(2)
push(3)
print("Top: " + str(peek()))  # 3
pop_stack()  # 3
pop_stack()  # 2
```

### Queue Implementation

```python
# Queue (First In, First Out)
let queue = []

function enqueue(item)
    append(queue, item)
    print("Enqueued: " + str(item))
end

function dequeue()
    if len(queue) > 0
        let item = pop(queue, 0)
        print("Dequeued: " + str(item))
        return item
    else
        print("Queue is empty")
        return nil
    end
end

enqueue("First")
enqueue("Second")
enqueue("Third")
dequeue()  # First
dequeue()  # Second
```

### Todo List Manager

```python
let todos = []

function add_todo(task)
    append(todos, task)
    print("Added: " + task)
end

function remove_todo(task)
    try
        remove(todos, task)
        print("Removed: " + task)
    except error
        print("Task not found: " + task)
    end
end

function show_todos()
    print("\n=== TODO LIST ===")
    if len(todos) == 0
        print("No tasks")
    else
        let i = 1
        for task in todos
            print(str(i) + ". " + task)
            i += 1
        end
    end
end

add_todo("Buy groceries")
add_todo("Do laundry")
add_todo("Call mom")
show_todos()
remove_todo("Do laundry")
show_todos()
```

### Shopping Cart

```python
let cart = []

function add_to_cart(item, price)
    let product = {
        "name": item,
        "price": price
    }
    append(cart, product)
    print("Added " + item + " - $" + str(price))
end

function remove_from_cart(item)
    let i = 0
    let found = false
    
    while i < len(cart)
        if cart[i]["name"] == item
            pop(cart, i)
            print("Removed " + item)
            found = true
        end
        i += 1
    end
    
    if not found
        print(item + " not in cart")
    end
end

function get_total()
    let total = 0
    for item in cart
        total += item["price"]
    end
    return total
end

function show_cart()
    print("\n=== SHOPPING CART ===")
    for item in cart
        print(item["name"] + " - $" + str(item["price"]))
    end
    print("Total: $" + str(get_total()))
end

add_to_cart("Apple", 0.99)
add_to_cart("Bread", 2.50)
add_to_cart("Milk", 3.99)
show_cart()
remove_from_cart("Bread")
show_cart()
```

### History Tracker

```python
let history = []
let max_history = 10

function add_to_history(action)
    append(history, action)
    
    # Keep only last max_history items
    while len(history) > max_history
        pop(history, 0)
    end
end

function show_history()
    print("\n=== HISTORY ===")
    for action in history
        print("- " + action)
    end
end

function clear_history()
    clear(history)
    print("History cleared")
end

add_to_history("Opened file")
add_to_history("Edited text")
add_to_history("Saved file")
show_history()
```

### List Sorter (Manual)

```python
function bubble_sort(numbers)
    let n = len(numbers)
    let i = 0
    
    while i < n - 1
        let j = 0
        while j < n - i - 1
            if numbers[j] > numbers[j + 1]
                # Swap
                let temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
            end
            j += 1
        end
        i += 1
    end
    
    return numbers
end

let nums = [64, 34, 25, 12, 22, 11, 90]
print("Before: " + str(nums))
bubble_sort(nums)
print("After: " + str(nums))
```

### Playlist Manager

```python
let playlist = []

function add_song(title, artist)
    let song = {
        "title": title,
        "artist": artist
    }
    append(playlist, song)
    print("Added: " + title + " by " + artist)
end

function remove_song(title)
    let i = 0
    while i < len(playlist)
        if playlist[i]["title"] == title
            pop(playlist, i)
            print("Removed: " + title)
            return
        end
        i += 1
    end
    print("Song not found: " + title)
end

function show_playlist()
    print("\n=== PLAYLIST ===")
    let i = 1
    for song in playlist
        print(str(i) + ". " + song["title"] + " - " + song["artist"])
        i += 1
    end
end

add_song("Imagine", "John Lennon")
add_song("Bohemian Rhapsody", "Queen")
add_song("Hotel California", "Eagles")
show_playlist()
```

### Undo/Redo System

```python
let undo_stack = []
let redo_stack = []

function do_action(action)
    append(undo_stack, action)
    clear(redo_stack)  # Clear redo when new action is done
    print("Action: " + action)
end

function undo()
    if len(undo_stack) > 0
        let action = pop(undo_stack)
        append(redo_stack, action)
        print("Undid: " + action)
    else
        print("Nothing to undo")
    end
end

function redo()
    if len(redo_stack) > 0
        let action = pop(redo_stack)
        append(undo_stack, action)
        print("Redid: " + action)
    else
        print("Nothing to redo")
    end
end

do_action("Type 'Hello'")
do_action("Type ' World'")
undo()
undo()
redo()
```

## List Manipulation Patterns

### Remove All Occurrences

```python
function remove_all(list, item)
    let count = 0
    let i = 0
    
    while i < len(list)
        if list[i] == item
            pop(list, i)
            count += 1
        else
            i += 1
        end
    end
    
    print("Removed " + str(count) + " occurrences")
    return list
end

let nums = [1, 2, 3, 2, 4, 2, 5]
remove_all(nums, 2)
print(nums)  # [1, 3, 4, 5]
```

### Insert Sorted

```python
function insert_sorted(list, item)
    let i = 0
    
    # Find insertion point
    while i < len(list) and list[i] < item
        i += 1
    end
    
    insert(list, i, item)
    return list
end

let sorted_list = [1, 3, 5, 7, 9]
insert_sorted(sorted_list, 4)
insert_sorted(sorted_list, 6)
print(sorted_list)  # [1, 3, 4, 5, 6, 7, 9]
```

### Replace Item

```python
function replace(list, old_item, new_item)
    let i = 0
    while i < len(list)
        if list[i] == old_item
            list[i] = new_item
            return true
        end
        i += 1
    end
    return false
end

let items = ["a", "b", "c", "d"]
replace(items, "b", "x")
print(items)  # ["a", "x", "c", "d"]
```

### Reverse List

```python
function reverse(list)
    let reversed = []
    let i = len(list) - 1
    
    while i >= 0
        append(reversed, list[i])
        i -= 1
    end
    
    return reversed
end

let nums = [1, 2, 3, 4, 5]
let rev = reverse(nums)
print(rev)  # [5, 4, 3, 2, 1]
```

## Best Practices

### Check Before Removing

```python
# Good: Handle errors
try
    remove(list, item)
except error
    print("Item not found")
end

# Better: Check first (when possible)
let found = false
for element in list
    if element == item
        found = true
    end
end

if found
    remove(list, item)
end
```

### Use Appropriate Method

```python
# Remove last item: use pop()
let last = pop(list)

# Remove specific item: use remove()
remove(list, "item")

# Remove at index: use pop(list, index)
let item = pop(list, 3)
```

### Avoid Index Errors

```python
# Check length before accessing
if len(list) > 0
    let item = pop(list)
end

# Use try-except
try
    let item = pop(list, index)
except error
    print("Index out of range")
end
```

## Quick Reference

| Function | Purpose | Example | Modifies List |
|----------|---------|---------|--------------|
| `append(list, item)` | Add to end | `append(fruits, "apple")` | Yes |
| `insert(list, i, item)` | Add at position | `insert(fruits, 0, "apple")` | Yes |
| `remove(list, item)` | Remove first match | `remove(fruits, "apple")` | Yes |
| `pop(list)` | Remove last | `pop(fruits)` | Yes |
| `pop(list, i)` | Remove at index | `pop(fruits, 0)` | Yes |
| `clear(list)` | Remove all | `clear(fruits)` | Yes |

## Next Steps

- **[Lists & Dictionaries](../guide/collections.md)** - Complete guide
- **[Built-in Functions](builtins.md)** - Other useful functions
- **[Examples](../examples/basic.md)** - See lists in action