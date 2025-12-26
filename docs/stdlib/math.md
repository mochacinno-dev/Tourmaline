# Math Functions

Tourmaline includes powerful mathematical functions for calculations, trigonometry, and more.

## Basic Math Functions

### `abs()`

Return the absolute value of a number.

**Syntax:**
```python
abs(number)
```

**Examples:**
```python
print(abs(5))      # 5
print(abs(-5))     # 5
print(abs(-3.14))  # 3.14
print(abs(0))      # 0
```

**Use Cases:**
```python
# Calculate distance
function distance(a, b)
    return abs(b - a)
end

print(distance(10, 25))   # 15
print(distance(25, 10))   # 15
```

---

### `pow()`

Raise a number to a power.

**Syntax:**
```python
pow(base, exponent)
```

**Examples:**
```python
print(pow(2, 3))    # 8 (2³)
print(pow(5, 2))    # 25 (5²)
print(pow(10, 0))   # 1 (anything⁰ = 1)
print(pow(2, -1))   # 0.5 (2⁻¹)
```

**Use Cases:**
```python
# Calculate compound interest
function compound_interest(principal, rate, years)
    return principal * pow(1 + rate, years)
end

let amount = compound_interest(1000, 0.05, 10)
print("Amount after 10 years: $" + str(amount))
```

---

### `sqrt()`

Calculate the square root.

**Syntax:**
```python
sqrt(number)
```

**Examples:**
```python
print(sqrt(16))    # 4.0
print(sqrt(25))    # 5.0
print(sqrt(2))     # 1.414...
print(sqrt(100))   # 10.0
```

**Use Cases:**
```python
# Pythagorean theorem
function hypotenuse(a, b)
    return sqrt(a * a + b * b)
end

print(hypotenuse(3, 4))  # 5.0

# Distance between points
function distance_2d(x1, y1, x2, y2)
    let dx = x2 - x1
    let dy = y2 - y1
    return sqrt(dx * dx + dy * dy)
end

print(distance_2d(0, 0, 3, 4))  # 5.0
```

---

## Rounding Functions

### `floor()`

Round down to the nearest integer.

**Syntax:**
```python
floor(number)
```

**Examples:**
```python
print(floor(3.7))    # 3
print(floor(3.2))    # 3
print(floor(3.9))    # 3
print(floor(-2.3))   # -3
print(floor(5.0))    # 5
```

**Use Cases:**
```python
# Calculate full dozens
function count_dozens(items)
    return floor(items / 12)
end

print(count_dozens(50))   # 4 dozens
print(count_dozens(37))   # 3 dozens
```

---

### `ceil()`

Round up to the nearest integer.

**Syntax:**
```python
ceil(number)
```

**Examples:**
```python
print(ceil(3.1))    # 4
print(ceil(3.7))    # 4
print(ceil(3.0))    # 3
print(ceil(-2.3))   # -2
```

**Use Cases:**
```python
# Calculate required boxes
function boxes_needed(items, box_capacity)
    return ceil(items / box_capacity)
end

print(boxes_needed(50, 12))  # 5 boxes
print(boxes_needed(37, 12))  # 4 boxes
```

---

### `round()`

Round to the nearest integer.

**Syntax:**
```python
round(number)
```

**Examples:**
```python
print(round(3.4))    # 3
print(round(3.5))    # 4
print(round(3.6))    # 4
print(round(-2.5))   # -2 or -3 (depends on implementation)
```

**Use Cases:**
```python
# Format currency
function format_price(price)
    let rounded = round(price * 100) / 100
    return "$" + str(rounded)
end

print(format_price(19.994))  # $19.99
```

---

## Trigonometric Functions

### `sin()`

Calculate sine (radians).

**Syntax:**
```python
sin(angle_in_radians)
```

**Examples:**
```python
let pi = 3.14159

print(sin(0))           # 0.0
print(sin(pi / 2))      # 1.0
print(sin(pi))          # 0.0 (approximately)
print(sin(3 * pi / 2))  # -1.0
```

**Use Cases:**
```python
# Calculate y-coordinate on unit circle
function circle_y(angle_degrees)
    let pi = 3.14159
    let radians = angle_degrees * pi / 180
    return sin(radians)
end

print(circle_y(90))   # 1.0 (top of circle)
print(circle_y(270))  # -1.0 (bottom of circle)
```

---

### `cos()`

Calculate cosine (radians).

**Syntax:**
```python
cos(angle_in_radians)
```

**Examples:**
```python
let pi = 3.14159

print(cos(0))           # 1.0
print(cos(pi / 2))      # 0.0 (approximately)
print(cos(pi))          # -1.0
print(cos(2 * pi))      # 1.0
```

**Use Cases:**
```python
# Calculate x-coordinate on unit circle
function circle_x(angle_degrees)
    let pi = 3.14159
    let radians = angle_degrees * pi / 180
    return cos(radians)
end

print(circle_x(0))    # 1.0 (right side)
print(circle_x(180))  # -1.0 (left side)
```

---

### `tan()`

Calculate tangent (radians).

**Syntax:**
```python
tan(angle_in_radians)
```

**Examples:**
```python
let pi = 3.14159

print(tan(0))        # 0.0
print(tan(pi / 4))   # 1.0 (approximately)
```

**Use Cases:**
```python
# Calculate slope
function calculate_slope(angle_degrees)
    let pi = 3.14159
    let radians = angle_degrees * pi / 180
    return tan(radians)
end

print(calculate_slope(45))  # 1.0 (45° slope)
```

---

## Practical Examples

### Circle Calculations

```python
let pi = 3.14159

function circle_area(radius)
    return pi * radius * radius
end

function circle_circumference(radius)
    return 2 * pi * radius
end

let r = 5
print("Radius: " + str(r))
print("Area: " + str(circle_area(r)))
print("Circumference: " + str(circle_circumference(r)))
```

### Triangle Calculations

```python
function triangle_area(base, height)
    return base * height / 2
end

function right_triangle_hypotenuse(a, b)
    return sqrt(a * a + b * b)
end

print("Triangle (base=6, height=8):")
print("Area: " + str(triangle_area(6, 8)))
print("Hypotenuse: " + str(right_triangle_hypotenuse(6, 8)))
```

### Quadratic Formula

```python
function solve_quadratic(a, b, c)
    # ax² + bx + c = 0
    let discriminant = b * b - 4 * a * c
    
    if discriminant < 0
        print("No real solutions")
        return nil
    end
    
    let sqrt_disc = sqrt(discriminant)
    let x1 = (-b + sqrt_disc) / (2 * a)
    let x2 = (-b - sqrt_disc) / (2 * a)
    
    print("Solutions:")
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
end

# Solve x² - 5x + 6 = 0
solve_quadratic(1, -5, 6)  # x = 3 and x = 2
```

### Statistics Calculations

```python
function standard_deviation(numbers)
    # Calculate mean
    let sum = 0
    for num in numbers
        sum += num
    end
    let mean = sum / len(numbers)
    
    # Calculate variance
    let variance_sum = 0
    for num in numbers
        let diff = num - mean
        variance_sum += diff * diff
    end
    let variance = variance_sum / len(numbers)
    
    # Return standard deviation
    return sqrt(variance)
end

let data = [10, 12, 23, 23, 16, 23, 21, 16]
print("Standard Deviation: " + str(standard_deviation(data)))
```

### Scientific Calculations

```python
# Speed of light calculation
function time_for_light(distance_km)
    let speed_of_light = 299792.458  # km/s
    return distance_km / speed_of_light
end

let earth_to_moon = 384400  # km
let time_seconds = time_for_light(earth_to_moon)
print("Light takes " + str(time_seconds) + " seconds to reach the Moon")

# Gravitational force
function gravity_force(mass1, mass2, distance)
    let G = 0.0000000000667430  # Gravitational constant
    return G * mass1 * mass2 / (distance * distance)
end
```

### Geometric Mean

```python
function geometric_mean(numbers)
    let product = 1
    for num in numbers
        product *= num
    end
    
    let n = len(numbers)
    return pow(product, 1.0 / n)
end

let values = [2, 8, 4]
print("Geometric Mean: " + str(geometric_mean(values)))
```

### Compound Interest Calculator

```python
function calculate_investment(principal, annual_rate, years, compounds_per_year)
    let rate_per_period = annual_rate / compounds_per_year
    let total_periods = compounds_per_year * years
    
    let amount = principal * pow(1 + rate_per_period, total_periods)
    let interest = amount - principal
    
    print("Initial Investment: $" + str(principal))
    print("Annual Rate: " + str(annual_rate * 100) + "%")
    print("Years: " + str(years))
    print("Compounds per Year: " + str(compounds_per_year))
    print("\nFinal Amount: $" + str(round(amount)))
    print("Interest Earned: $" + str(round(interest)))
    
    return amount
end

calculate_investment(10000, 0.05, 10, 4)
```

### Projectile Motion

```python
function projectile_range(velocity, angle_degrees)
    let pi = 3.14159
    let g = 9.81  # Gravity (m/s²)
    
    # Convert to radians
    let angle_rad = angle_degrees * pi / 180
    
    # Calculate range
    let range = velocity * velocity * sin(2 * angle_rad) / g
    
    return range
end

print("Projectile launched at 30 m/s:")
print("At 30°: " + str(projectile_range(30, 30)) + " meters")
print("At 45°: " + str(projectile_range(30, 45)) + " meters")
print("At 60°: " + str(projectile_range(30, 60)) + " meters")
```

## Quick Reference

| Function | Purpose | Example | Result |
|----------|---------|---------|--------|
| `abs(x)` | Absolute value | `abs(-5)` | 5 |
| `pow(x, y)` | x to power y | `pow(2, 3)` | 8 |
| `sqrt(x)` | Square root | `sqrt(16)` | 4.0 |
| `floor(x)` | Round down | `floor(3.7)` | 3 |
| `ceil(x)` | Round up | `ceil(3.2)` | 4 |
| `round(x)` | Round nearest | `round(3.5)` | 4 |
| `sin(x)` | Sine (radians) | `sin(0)` | 0.0 |
| `cos(x)` | Cosine (radians) | `cos(0)` | 1.0 |
| `tan(x)` | Tangent (radians) | `tan(0)` | 0.0 |

## Constants

Define commonly-used mathematical constants:

```python
let PI = 3.14159265359
let E = 2.71828182846
let GOLDEN_RATIO = 1.61803398875

# Use in calculations
let circle_area = PI * radius * radius
let exponential = pow(E, 2)
```

## Tips & Best Practices

!!! tip "Convert Degrees to Radians"
    Trigonometric functions use radians:
    ```python
    let degrees = 90
    let pi = 3.14159
    let radians = degrees * pi / 180
    print(sin(radians))  # 1.0
    ```

!!! tip "Check for Domain Errors"
    Some functions have restrictions:
    ```python
    # sqrt() requires non-negative numbers
    if value >= 0
        let result = sqrt(value)
    else
        print("Cannot take square root of negative number")
    end
    ```

!!! warning "Floating Point Precision"
    Be aware of floating-point rounding:
    ```python
    let result = sqrt(2) * sqrt(2)
    # Might be 1.9999999 or 2.0000001, not exactly 2
    
    # Use rounding for comparisons
    let rounded = round(result * 100) / 100
    ```

## Next Steps

- **[Random Library](random.md)** - Generate random numbers
- **[Built-in Functions](builtins.md)** - Other useful functions
- **[Examples](../examples/advanced.md)** - Math in practice