# Contributing to Tourmaline

Thank you for your interest in contributing to Tourmaline! This guide will help you get started.

## Ways to Contribute

There are many ways to help improve Tourmaline:

### 🐛 Report Bugs

Found a bug? Please report it!

1. Check if it's already reported in [GitHub Issues](https://github.com/mochacinno-dev/Tourmaline/issues)
2. If not, create a new issue with:
   - Clear description of the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Tourmaline version
   - Operating system

**Example Bug Report:**
```markdown
**Bug Description:**
Division by zero doesn't raise an error in certain cases

**Steps to Reproduce:**
1. Create variable: let x = 10
2. Create variable: let y = 0
3. Calculate: let z = x / y
4. No error is raised

**Expected Behavior:**
Should raise "Division by zero" error

**Environment:**
- Tourmaline: v1.0.0
- Python: 3.9
- OS: Windows 10
```

### 💡 Suggest Features

Have an idea for a new feature?

1. Check existing feature requests
2. Open a new issue with:
   - Clear description
   - Use cases
   - Example syntax (if applicable)
   - Why it would be valuable

### 📝 Improve Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add examples
- Improve code samples
- Translate documentation
- Write tutorials or guides

### 🔧 Submit Code

Ready to code? Great!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Code Contributions

### Getting Started

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Tourmaline.git
   cd Tourmaline
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Write clean, readable code
   - Follow existing code style
   - Add comments for complex logic

4. **Test Your Changes**
   ```bash
   python Tourmaline.py test_file.trm
   ```

5. **Commit**
   ```bash
   git add .
   git commit -m "Add: clear description of changes"
   ```

6. **Push and Create Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

### Code Style Guidelines

#### Python Code (Interpreter)

- Use 4 spaces for indentation
- Follow PEP 8 where reasonable
- Use descriptive variable names
- Add docstrings to functions

**Example:**
```python
def evaluate_expression(self, tokens: List[str]) -> Any:
    """
    Evaluate an expression from a list of tokens.
    
    Args:
        tokens: List of tokenized expression elements
        
    Returns:
        The evaluated result
        
    Raises:
        TourmalineError: If expression cannot be evaluated
    """
    # Implementation...
```

#### Tourmaline Code (Examples)

- Use consistent naming (snake_case for variables)
- Comment complex logic
- Keep functions focused and small
- Use meaningful variable names

**Example:**
```python
# Calculate the area of a circle
function calculate_circle_area(radius)
    let pi = 3.14159
    let area = pi * radius * radius
    return area
end
```

### Testing

Before submitting:

1. **Test basic functionality**
   - Run existing example programs
   - Test your specific changes
   - Try edge cases

2. **Test error handling**
   - Provide invalid input
   - Test boundary conditions
   - Ensure errors are caught

3. **Create test files**
   - Add `.trm` files demonstrating your feature
   - Include both success and error cases

### Pull Request Guidelines

**Title Format:**
- `Add: Feature description` for new features
- `Fix: Bug description` for bug fixes
- `Docs: Documentation improvement` for docs
- `Refactor: Code improvement` for refactoring

**Description Should Include:**
- What changes were made
- Why they were necessary
- How to test them
- Any breaking changes
- Related issues (if any)

**Example PR Description:**
```markdown
## Changes
Added support for list slicing with `list[start:end]` syntax

## Motivation
Users requested the ability to extract sublists more easily

## Testing
- Added test_slice.trm with various slice examples
- Tested with positive and negative indices
- Tested edge cases (empty lists, out of bounds)

## Breaking Changes
None

## Related Issues
Closes #42
```

## Project Structure

Understanding the codebase:

```
Tourmaline/
├── Tourmaline.py          # Main interpreter
├── LICENSE                # GPL-3.0 license
├── README.md             # Project overview
├── code/                 # Example programs
│   ├── example.trm
│   ├── main.trm
│   └── ...
└── scripts/              # Helper scripts
    ├── tli.sh
    └── tli.bat
```

### Key Components

**Tourmaline.py Sections:**
1. `TourmalineError` - Exception class
2. `TourmalineInterpreter` - Main interpreter
   - `tokenize()` - Lexical analysis
   - `parse_value()` - Value parsing
   - `evaluate_expression()` - Expression evaluation
   - `execute()` - Main execution loop
3. Built-in functions setup
4. Standard libraries setup

## Feature Development Process

### 1. Planning

- Discuss the feature in an issue first
- Get feedback from maintainers
- Consider backward compatibility
- Think about edge cases

### 2. Implementation

- Start with tests/examples
- Implement incrementally
- Keep commits focused
- Write clear commit messages

### 3. Documentation

- Update relevant docs
- Add examples
- Document new syntax
- Update README if needed

### 4. Review

- Self-review your code
- Test thoroughly
- Ensure it works on different systems
- Request feedback

## Areas Needing Help

Current priorities:

### High Priority

- 🐛 **Bug Fixes** - Especially parsing edge cases
- 📖 **Documentation** - More examples and tutorials
- ✅ **Testing** - Comprehensive test suite
- 🔧 **Error Messages** - More helpful messages

### Medium Priority

- 🎨 **Syntax Improvements** - Better error handling
- 📦 **Standard Library** - More built-in functions
- 🚀 **Performance** - Optimization opportunities
- 🌐 **Internationalization** - Non-English support

### Ideas for New Contributors

Easy first contributions:

1. **Add Example Programs**
   - Create `.trm` files demonstrating features
   - Add to `code/` directory

2. **Improve Error Messages**
   - Make them more descriptive
   - Add suggestions for fixes

3. **Write Tutorials**
   - Beginner guides
   - Specific use cases
   - Video tutorials

4. **Fix Typos**
   - Documentation typos
   - Code comments
   - Example programs

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Accept constructive criticism
- Focus on what's best for the project
- Show empathy toward others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information

### Enforcement

Violations may result in:
- Warning
- Temporary ban
- Permanent ban

Report issues to project maintainers.

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md (if created)
- Credited in release notes
- Acknowledged in relevant documentation
- Appreciated! 🎉

## Legal

By contributing, you agree that:

- Your contributions are your original work
- You have the right to submit them
- Your contributions will be under the GPL-3.0 license
- You understand the implications of the GPL-3.0

See [License](license.md) for details.

## Questions?

- **General Questions**: Open a GitHub Discussion
- **Bug Reports**: GitHub Issues
- **Security Issues**: Contact maintainers privately
- **Feature Ideas**: GitHub Issues with "enhancement" label

## Thank You!

Every contribution helps make Tourmaline better. Whether you're:
- Fixing a typo
- Adding a feature
- Writing documentation
- Reporting a bug
- Suggesting improvements

Your help is valuable and appreciated! 💎

---

**Ready to contribute? Check out the [open issues](https://github.com/mochacinno-dev/Tourmaline/issues) or [fork the repository](https://github.com/mochacinno-dev/Tourmaline) to get started!**