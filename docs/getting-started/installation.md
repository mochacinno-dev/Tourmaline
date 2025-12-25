# Installation

This guide will help you install Tourmaline on your system.

## Prerequisites

Tourmaline requires Python 3.6 or higher to run. Before installing Tourmaline, make sure you have Python installed:

```bash
# Check your Python version
python --version
# or
python3 --version
```

!!! note
    If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/)

## Installation Methods

### Method 1: Download from GitHub (Recommended)

1. **Clone the Repository**

```bash
git clone https://github.com/mochacinno-dev/Tourmaline.git
cd Tourmaline
```

2. **Verify Installation**

```bash
python Tourmaline.py --version
```

### Method 2: Direct Download

1. Visit the [Tourmaline GitHub repository](https://github.com/mochacinno-dev/Tourmaline)
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file to your desired location
5. Navigate to the extracted folder

## Running Tourmaline

### Interactive Mode (REPL)

Start the interactive interpreter:

```bash
python Tourmaline.py
```

You should see:

```
Tourmaline Language Interpreter (TLI) v1.0.0 - Tourmal Waters
Type 'exit' to quit
Interactive mode (type 'exit' to quit):
>>> 
```

### Running Script Files

Execute a Tourmaline script file:

```bash
python Tourmaline.py yourfile.trm
```

!!! tip
    Tourmaline supports three file extensions: `.trm`, `.tli`, and `.tour`

## Setting Up Shell Scripts (Optional)

For easier access, you can use the provided shell scripts:

### Linux/macOS

```bash
chmod +x scripts/tli.sh
./scripts/tli.sh yourfile.trm
```

Optionally, add to your PATH:

```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$PATH:/path/to/Tourmaline/scripts"
```

Then you can run:

```bash
tli.sh yourfile.trm
```

### Windows

Use the batch script:

```cmd
scripts\tli.bat yourfile.trm
```

## Verifying Your Installation

Create a test file called `hello.trm`:

```python
print("Hello from Tourmaline!")

let version = "1.0.0"
print("Running version: " + version)
```

Run it:

```bash
python Tourmaline.py hello.trm
```

Expected output:

```
Hello from Tourmaline!
Running version: 1.0.0
```

## Troubleshooting

### Python Not Found

If you get a "python: command not found" error, try:

- Use `python3` instead of `python`
- Ensure Python is added to your system PATH
- Reinstall Python and check "Add to PATH" during installation

### Permission Denied (Linux/macOS)

If you get permission errors:

```bash
chmod +x Tourmaline.py
chmod +x scripts/tli.sh
```

### Import Errors

If you encounter import errors, ensure you're using Python 3.6+:

```bash
python3 --version
```

## Next Steps

Now that Tourmaline is installed, you're ready to:

- **[Start with the Quick Start Guide](quick-start.md)**
- **[Write Your First Program](first-program.md)**
- **[Explore the Language Guide](../guide/variables.md)**

---

!!! warning
    Tourmaline is under active development. Check the GitHub repository for updates and new features!