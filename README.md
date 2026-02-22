# GOIT PyCore HW-05: Task Collection

A collection of Python tasks from the GOIT PyCore course with an integrated CLI navigation system.

## Project Structure

```
goit-pycore-hw-05/
├── main.py          # Main CLI navigator
├── task1.py         # Task 1: Caching Fibonacci
├── task2.py         # Task 2: Generator Numbers
└── task4.py         # Task 4: Phone Contact Parser
```

## Tasks Overview

### Task 1: Caching Fibonacci

A closure-based Fibonacci function with memoization. `caching_fibonacci()` returns a `fibonacci(n)` function that caches previously computed values for efficient repeated lookups.

- **Concept:** Closures, memoization
- **Output:** Fibonacci numbers with O(n) complexity thanks to caching

### Task 2: Generator Numbers

A generator `generator_numbers(text)` that extracts decimal numbers from a text string, and a `sum_profit(text, func)` higher-order function that sums them.

- **Concept:** Generators, regular expressions, higher-order functions
- **Output:** Total sum of all decimal numbers found in the input text

### Task 4: Phone Contact Parser

Interactive contact management bot with add, update, search, and display functions. Uses an `input_error` decorator for graceful error handling.

- **Concept:** Decorators, error handling
- **Commands:**
  - `add <name> <phone>` — Add new contact
  - `change <name> <phone>` — Update contact
  - `phone <name>` — Show phone number
  - `all` — Show all contacts
  - `hello` — Greet
  - `close` / `exit` — Exit program

## Usage

### Using the CLI Navigator (Recommended)

Run the main CLI menu:

```bash
python main.py
```

Select a task by entering its number:

- **1** — Run Task 4 (Contact Manager)
- **0** — Exit

### Running Individual Tasks

**Task 1:** Caching Fibonacci

```bash
python task1.py
```

**Task 2:** Generator Numbers

```bash
python task2.py
```

**Task 4:** Phone Contact Parser

```bash
python task4.py
```

## Requirements

- Python 3.10+

## Andrii Nazarenko

Created as part of GOIT PyCore course homework assignment #05.

