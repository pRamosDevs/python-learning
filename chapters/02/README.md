# Chapter 2 — Variables and Simple Data Types

## 1. Overview

Chapter 2 introduces the fundamental building blocks used to write Python programs.

The chapter focuses on:

- Variables
- Assignment and reassignment
- Variable naming
- Strings
- String methods
- String immutability
- String concatenation
- f-strings
- Escape sequences
- Integers
- Floating-point numbers
- Arithmetic operators
- Operator precedence
- Underscores in numbers
- Multiple assignment
- Constants
- Comments
- Python's philosophy and the Zen of Python

The objective is not simply to memorize Python syntax. The important goal is to understand how Python represents values, associates names with values, evaluates expressions, and produces new values.

---

## 2. Learning Objectives

After completing this chapter, I should be able to:

- Explain what a variable is.
- Explain assignment and reassignment.
- Distinguish `=` from `==`.
- Create valid and readable variable names.
- Explain Python's case sensitivity.
- Distinguish Python keywords from built-in functions.
- Create and manipulate strings.
- Use common string methods.
- Explain why strings are immutable.
- Explain the difference between a method and a method call.
- Concatenate strings.
- Use f-strings.
- Use escape sequences.
- Distinguish integers from floating-point numbers.
- Perform basic arithmetic.
- Explain `/`, `//`, `%`, and `**`.
- Understand operator precedence.
- Use underscores in large numbers.
- Use multiple assignment.
- Understand Python's convention for constants.
- Write useful comments.
- Understand the main principles of the Zen of Python.

---

## 3. Variables

A variable is a **name associated with a value**.

Example:

```python
name = "Ada"
```

Here:

```text
name
  ↓
"Ada"
```

- `name` is the variable name.
- `"Ada"` is a string literal.
- `=` is the assignment operator.

The statement assigns the value `"Ada"` to the name `name`.

A useful mental model is:

```text
variable name
      ↓
     value
```

Variables allow a program to give meaningful names to values and use those values later.

### 3.1 Assignment

Python uses `=` for assignment.

```python
age = 25
```

This means:

> Assign the value `25` to `age`.

It does **not** mean that `age` and `25` are being tested for equality.

### 3.2 Equality

Python uses `==` to test equality.

```python
age == 25
```

This means:

> Is the value associated with `age` equal to `25`?

Therefore:

```python
age = 25
```

and:

```python
age == 25
```

have different purposes.

| Operator | Purpose |
|---|---|
| `=` | Assignment |
| `==` | Equality comparison |

### 3.3 Reassignment

A variable can be assigned a new value.

```python
message = "Hello"
message = "Goodbye"
```

After the second assignment:

```text
message
   ↓
"Goodbye"
```

Another example:

```python
age = 25
age = 26
```

The variable `age` has been reassigned.

The same variable name can therefore refer to different values at different points during program execution.

---

## 4. Variable Naming

Python variable names can contain:

- Letters
- Numbers
- Underscores

Examples:

```python
name
user_name
age
user1
total_score
```

A variable name cannot begin with a number.

Invalid:

```python
1user = "Ada"
```

Valid:

```python
user1 = "Ada"
```

Spaces cannot be used in variable names.

Invalid:

```python
user name = "Ada"
```

Use an underscore:

```python
user_name = "Ada"
```

Hyphens should not be used as part of variable names.

For example:

```python
user-name
```

is interpreted as an expression involving subtraction rather than as a single variable name.

### 4.1 Naming Conventions

Python commonly uses **snake_case** for variable names.

```python
first_name = "Ada"
last_name = "Lovelace"
birth_year = 1815
```

Variable names should communicate what the value represents.

Prefer:

```python
user_age = 25
```

over:

```python
x = 25
```

when the meaning of the value matters.

Good names improve:

- Readability
- Maintainability
- Debugging
- Understanding of the program

### 4.2 Case Sensitivity

Python is case-sensitive.

These are different names:

```python
name
Name
NAME
```

For example:

```python
name = "Ada"
Name = "Grace"
NAME = "Alan"
```

creates three different variables.

---

## 5. Keywords and Built-ins

Python contains **keywords** that have special meaning in the language.

Examples:

```python
if
for
while
class
def
return
import
```

Keywords are part of Python's syntax and cannot normally be used as ordinary variable names.

Python also provides **built-in functions** and types.

For example:

```python
print()
```

`print` is a built-in function.

The distinction is:

```text
Python keyword
    ↓
Part of Python's language syntax

Python built-in
    ↓
Function/type provided by Python
```

For example:

```python
if
```

is a keyword.

Whereas:

```python
print()
```

calls a built-in function.

---

## 6. Strings

A string is a sequence of text characters.

Strings can be written with single quotes:

```python
name = 'Ada'
```

or double quotes:

```python
name = "Ada"
```

Both represent strings.

Examples:

```python
name = "Ada"
language = "Python"
message = "Hello, world!"
```

The quotation marks delimit the string literal.

### 6.1 String Literals and Variables

Consider:

```python
name = "Ada"
```

There are two different concepts here:

```text
name
 ↓
variable name

"Ada"
 ↓
string literal / value
```

The variable provides a name through which the value can be accessed.

---

## 7. String Methods

Strings provide methods that perform operations on string values.

Example:

```python
name = "ada lovelace"
print(name.title())
```

Output:

```text
Ada Lovelace
```

A method is an operation associated with an object.

Common string methods introduced in this chapter include:

```python
.title()
.upper()
.lower()
.strip()
.lstrip()
.rstrip()
.removeprefix()
```

---

## 8. `.title()`

`.title()` returns a version of the string with the first letter of each word capitalized.

```python
name = "ada lovelace"
print(name.title())
```

Output:

```text
Ada Lovelace
```

Importantly, `.title()` does not modify the original string.

```python
name = "ada lovelace"

name.title()

print(name)
```

Output:

```text
ada lovelace
```

To use the returned value as the new value of `name`:

```python
name = name.title()
```

Now:

```python
print(name)
```

produces:

```text
Ada Lovelace
```

---

## 9. Method vs Method Call

This is one of the most important distinctions from the chapter.

Consider:

```python
name.title
```

and:

```python
name.title()
```

They are different.

### Method reference

```python
name.title
```

references the method itself.

### Method call

```python
name.title()
```

calls the method and produces its result.

For example:

```python
name = "ada"
print(name.title())
```

produces:

```text
Ada
```

But:

```python
name = "ada"
name = name.title
print(name)
```

does not assign `"Ada"` to `name`.

Instead, `name` becomes a reference to the method.

The output is similar to:

```text
<built-in method title of str object at 0x...>
```

The exact representation can vary.

### Important rule

```python
.method
```

means:

> Reference the method.

```python
.method()
```

means:

> Call the method.

---

## 10. `.upper()`

`.upper()` returns an uppercase version of a string.

```python
name = "Ada Lovelace"
print(name.upper())
```

Output:

```text
ADA LOVELACE
```

The original string remains unchanged.

---

## 11. `.lower()`

`.lower()` returns a lowercase version of a string.

```python
name = "Ada Lovelace"
print(name.lower())
```

Output:

```text
ada lovelace
```

Again, the original string is not modified.

---

## 12. `.strip()`

`.strip()` removes leading and trailing whitespace.

Example:

```python
name = "  Ada  "
clean_name = name.strip()

print(clean_name)
```

Result:

```text
Ada
```

By default:

```python
.strip()
```

removes whitespace from both ends.

It does not remove whitespace from the middle of the string.

For example:

```text
"  Ada Lovelace  "
```

becomes:

```text
"Ada Lovelace"
```

---

## 13. `.lstrip()` and `.rstrip()`

`.lstrip()` removes leading whitespace.

```python
name = "   Ada"
print(name.lstrip())
```

Result:

```text
Ada
```

`.rstrip()` removes trailing whitespace.

```python
name = "Ada   "
print(name.rstrip())
```

Result:

```text
Ada
```

The distinction is:

```text
lstrip() → left side
rstrip() → right side
strip()  → both sides
```

---

## 14. `.removeprefix()`

`.removeprefix()` removes an exact prefix when it occurs at the beginning of a string.

Example:

```python
url = "https://example.com"
clean_url = url.removeprefix("https://")

print(clean_url)
```

Output:

```text
example.com
```

If the specified prefix is not present at the beginning, the original string is returned unchanged.

Example:

```python
url = "http://example.com"

print(url.removeprefix("https://"))
```

Result:

```text
http://example.com
```

---

## 15. String Immutability

Strings are **immutable**.

This means that string operations do not modify the existing string in place.

Instead, string methods return new string values.

Example:

```python
name = "ada"

name.title()

print(name)
```

Output:

```text
ada
```

The result of `.title()` was produced but not stored.

To keep the result:

```python
name = name.title()
```

Conceptually:

```text
Original string
      ↓
 string method
      ↓
New string
```

not:

```text
Original string
      ↓
modified in place
```

This is a fundamental concept for understanding Python strings.

---

## 16. String Concatenation

Strings can be combined using `+`.

Example:

```python
first_name = "Ada"
last_name = "Lovelace"

full_name = first_name + " " + last_name
```

The result is:

```text
Ada Lovelace
```

This operation is called **string concatenation**.

The `" "` is a string containing one space.

Without it:

```python
first_name + last_name
```

would produce:

```text
AdaLovelace
```

---

## 17. f-Strings

An f-string provides a convenient way to insert values into a string.

Example:

```python
name = "Ada"
age = 25

message = f"My name is {name} and I am {age} years old."

print(message)
```

Output:

```text
My name is Ada and I am 25 years old.
```

The `f` before the opening quote tells Python that this is an f-string.

Expressions inside `{}` are evaluated and their results are inserted into the string.

### 17.1 Expressions in f-Strings

The content inside `{}` can be an expression.

Example:

```python
age = 25

print(f"Next year I will be {age + 1}.")
```

Output:

```text
Next year I will be 26.
```

Python evaluates:

```python
age + 1
```

and inserts the result into the string.

---

## 18. Escape Sequences

Python strings support escape sequences.

### New line

```text
\n
```

Example:

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

### Tab

```text
\t
```

Example:

```python
print("Name:\tAda")
```

### Backslash

```text
\\
```

### Double quote

```text
\"
```

Example:

```python
print("She said \"Hello\".")
```

Common escape sequences:

| Escape sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double quote |

---

## 19. Integers

An integer (`int`) is a whole number.

Examples:

```python
age = 25
quantity = 10
temperature = -5
```

Integers can be:

- Positive
- Negative
- Zero

Examples:

```text
10
-10
0
```

---

## 20. Floating-Point Numbers

A floating-point number (`float`) represents a number with a decimal component.

Examples:

```python
height = 1.89
temperature = 21.5
price = 19.99
```

The fundamental distinction is:

```text
int
↓
whole number

float
↓
floating-point number
```

For example:

```python
age = 25
height = 1.89
```

`age` is an integer while `height` is a floating-point number.

---

## 21. Arithmetic Operators

Python provides standard arithmetic operators.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `10 / 3` | `3.3333333333333335` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulo | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

---

## 22. Division

The `/` operator performs division.

```python
10 / 3
```

Result:

```text
3.3333333333333335
```

Division with `/` produces a floating-point result.

This is different from floor division:

```python
10 // 3
```

which produces:

```text
3
```

---

## 23. Floor Division

The `//` operator performs floor division.

```python
10 // 3
```

Result:

```text
3
```

For positive numbers:

```text
10 / 3  → 3.333...
10 // 3 → 3
```

Floor division should not be understood simply as "remove the decimal part".

It performs mathematical floor division.

For example:

```python
-10 // 3
```

produces:

```text
-4
```

because floor division rounds toward negative infinity.

---

## 24. Modulo

The `%` operator returns the remainder of a division.

```python
10 % 3
```

Result:

```text
1
```

Because:

```text
10 = 3 × 3 + 1
```

Modulo is commonly useful for checking divisibility.

For example:

```python
10 % 2
```

produces:

```text
0
```

A remainder of zero means the number is evenly divisible by the divisor.

---

## 25. Exponentiation

The `**` operator performs exponentiation.

```python
2 ** 3
```

Result:

```text
8
```

This represents:

```text
2³ = 8
```

Another example:

```python
5 ** 2
```

produces:

```text
25
```

---

## 26. Operator Precedence

Python follows rules that determine the order in which operations are evaluated.

Example:

```python
2 + 3 * 4
```

Result:

```text
14
```

Multiplication is evaluated before addition.

Parentheses can explicitly control the order:

```python
(2 + 3) * 4
```

Result:

```text
20
```

A useful principle is:

> Use parentheses when they make the intended order of evaluation clearer.

---

## 27. Underscores in Numbers

Python allows underscores inside numeric literals to improve readability.

Example:

```python
universe_age = 14_000_000_000
```

This represents the same value as:

```python
14000000000
```

The underscores do not change the value.

They are visual separators.

Another example:

```python
population = 1_000_000
```

is equivalent to:

```python
population = 1000000
```

The first version is easier to read.

---

## 28. Multiple Assignment

Python allows several variables to be assigned in one statement.

Example:

```python
x, y, z = 1, 2, 3
```

This results in:

```text
x → 1
y → 2
z → 3
```

Another example:

```python
first_name, last_name = "Ada", "Lovelace"
```

Conceptually, this is equivalent to:

```python
first_name = "Ada"
last_name = "Lovelace"
```

Multiple assignment is useful when several related variables need to be initialized together.

---

## 29. Constants

Python does not enforce a special constant variable type.

Instead, programmers use a naming convention.

Constants are traditionally written using uppercase letters:

```python
MAX_CONNECTIONS = 500
```

This communicates that the value is intended to remain constant.

However, Python does not prevent reassignment:

```python
MAX_CONNECTIONS = 500
MAX_CONNECTIONS = 1000
```

This is technically valid.

Therefore:

```text
UPPERCASE NAME
      ↓
programmer convention
```

not:

```text
UPPERCASE NAME
      ↓
Python-enforced constant
```

---

## 30. Comments

Comments allow programmers to add information for human readers.

A comment begins with:

```text
#
```

Example:

```python
# Store the maximum number of allowed connections.
MAX_CONNECTIONS = 500
```

Good comments explain:

- Intent
- Context
- Non-obvious decisions
- Important constraints

Avoid comments that merely repeat what obvious code already says.

For example:

```python
# Assign 25 to age.
age = 25
```

adds little useful information.

A good comment should provide information that is not already obvious from the code.

---

## 31. The Zen of Python

Python includes a collection of design principles known as **The Zen of Python**.

It can be displayed using:

```python
import this
```

Some important principles include:

```text
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Readability counts.
```

The Zen of Python emphasizes qualities such as:

- Readability
- Simplicity
- Explicitness
- Clear design
- Avoiding unnecessary complexity

These principles are useful when deciding not only whether code works, but also whether the code is understandable and maintainable.

---

## 32. Important Conceptual Distinctions

### Variable vs Value

```python
name = "Ada"
```

```text
name  → variable name
"Ada" → value / string literal
```

### Assignment vs Equality

```python
age = 25
```

means:

> Assign `25` to `age`.

While:

```python
age == 25
```

means:

> Test whether `age` is equal to `25`.

### Method vs Method Call

```python
name.title
```

references the method.

```python
name.title()
```

calls the method.

### String Mutation vs New Value

Strings are immutable.

Therefore:

```python
name.title()
```

produces a new string value rather than modifying `name` in place.

To replace the value associated with `name`:

```python
name = name.title()
```

### Integer vs Float

```python
25
```

is an integer.

```python
25.0
```

is a floating-point number.

### Keyword vs Built-in

```python
if
```

is a Python keyword.

```python
print()
```

calls a Python built-in function.

---

## 33. Common Mistakes

### Mistake 1 — Forgetting `()` when calling a method

Incorrect:

```python
name = name.title
```

This assigns the method itself.

Correct:

```python
name = name.title()
```

This calls the method and assigns its returned value.

### Mistake 2 — Assuming methods modify strings

Incorrect mental model:

```python
name = "ada"
name.title()
```

and expecting `name` to become `"Ada"`.

Correct:

```python
name = "ada"
name = name.title()
```

### Mistake 3 — Confusing `=` and `==`

Assignment:

```python
age = 25
```

Equality comparison:

```python
age == 25
```

### Mistake 4 — Assuming `/` performs integer division

```python
10 / 3
```

produces:

```text
3.3333333333333335
```

not:

```text
3
```

Floor division is:

```python
10 // 3
```

### Mistake 5 — Assuming constants are enforced

```python
MAX_CONNECTIONS = 500
```

does not prevent:

```python
MAX_CONNECTIONS = 1000
```

Uppercase is a convention.

---

## 34. Debugging Example

Consider:

```python
name = "ada lovelace"
print(name.title)

age = "25"
result = age + 5

MAX_CONNECTIONS = 500
max_connections = 1000

print(f"My name is {name} and I am {age} years old.")
```

There are multiple problems to identify.

### Problem 1 — Method reference instead of method call

```python
print(name.title)
```

references the method instead of calling it.

Correct:

```python
print(name.title())
```

### Problem 2 — String and integer

```python
age = "25"
result = age + 5
```

`age` is a string while `5` is an integer.

The two values cannot be added together using `+`.

If `age` represents a numeric value:

```python
age = 25
result = age + 5
```

Now:

```text
result → 30
```

### Problem 3 — Case sensitivity

These are different variables:

```python
MAX_CONNECTIONS = 500
max_connections = 1000
```

Python treats uppercase and lowercase names as distinct.

---

## 35. Micro-Challenge: Method Calls

### A

```python
name = "ada"
name.title()
print(name)
```

Output:

```text
ada
```

The method was called, but the returned value was not assigned back to `name`.

### B

```python
name = "ada"
name = name.title()
print(name)
```

Output:

```text
Ada
```

The returned value was assigned back to `name`.

### C

```python
name = "ada"
name = name.title
print(name)
```

`name` becomes a reference to the method itself.

The output is similar to:

```text
<built-in method title of str object at 0x...>
```

It does **not** produce `"Ada"`.

### D

```python
name = "ada"
print(name.title())
```

Output:

```text
Ada
```

The method is called and its returned value is passed directly to `print()`.

The original `name` remains:

```text
"ada"
```

---

## 36. Practical Examples

### Variables

```python
name = "Ada"
age = 25
```

### Reassignment

```python
age = 25
age = 26
```

### String transformation

```python
name = "ada lovelace"

print(name.title())
print(name.upper())
print(name.lower())
```

### String cleaning

```python
username = "   ada   "
clean_username = username.strip()

print(clean_username)
```

### Prefix removal

```python
url = "https://example.com"
domain = url.removeprefix("https://")

print(domain)
```

### Concatenation

```python
first_name = "Ada"
last_name = "Lovelace"

full_name = first_name + " " + last_name
```

### f-string

```python
name = "Ada"
age = 25

message = f"My name is {name} and I am {age} years old."

print(message)
```

### Arithmetic

```python
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
```

### Multiple assignment

```python
x, y, z = 1, 2, 3
```

### Constant convention

```python
MAX_CONNECTIONS = 500
```

---

## 37. Practice Exercises

### Exercise 1 — Variables

Create a variable called `message`.

Assign it one value and then reassign it to another value.

Print the final value.

### Exercise 2 — String Methods

Create:

```python
name = "ada lovelace"
```

Produce:

- Title case
- Uppercase
- Lowercase

without changing the original variable.

### Exercise 3 — Cleaning Input

Create:

```python
username = "   ada   "
```

Use `.strip()` to create a cleaned value.

Print both values.

### Exercise 4 — Prefix Removal

Create:

```python
url = "https://example.com"
```

Remove `"https://"` using `.removeprefix()`.

### Exercise 5 — f-Strings

Create variables for:

```text
first_name
last_name
age
```

Use an f-string to produce:

```text
My name is ... and I am ... years old.
```

### Exercise 6 — Arithmetic

Create two integer variables.

Calculate:

- Addition
- Subtraction
- Multiplication
- Division
- Floor division
- Remainder
- Exponentiation

Print every result.

### Exercise 7 — Operator Precedence

Predict the result before running the code:

```python
result_1 = 2 + 3 * 4
result_2 = (2 + 3) * 4
result_3 = 2 ** 3 + 1
result_4 = 10 // 3
result_5 = 10 % 3
```

Then verify the results.

### Exercise 8 — Multiple Assignment

Create `x`, `y`, and `z` and assign:

```text
10
20
30
```

using a single statement.

### Exercise 9 — Debugging

Fix the following:

```python
name = "ada lovelace"
name = name.title
age = "25"
result = age + 5

print(f"My name is {name} and I am {age} years old.")
```

The final program should:

- Store `name` correctly.
- Store `age` as a number.
- Calculate the age five years later.
- Print a correct sentence.

---

## 38. Knowledge Check

Before considering the chapter understood, I should be able to answer these without looking at the notes.

### Variables

- What is a variable?
- What does assignment mean?
- What is the difference between `=` and `==`?
- What happens when a variable is reassigned?
- What makes a variable name valid?
- Why is `name = name.title()` different from `name = name.title`?

### Strings

- What is a string?
- What is a string literal?
- What does string immutability mean?
- Why does `.title()` not modify the original string?
- What does `.strip()` do?
- What is the difference between `.lstrip()` and `.rstrip()`?
- What does `.removeprefix()` do?
- What is string concatenation?

### Methods

- What is a method?
- What is the difference between a method reference and a method call?
- Why are the parentheses in `.title()` important?

### f-Strings

- What does the `f` prefix mean?
- What happens inside `{}`?
- Can an expression be placed inside `{}`?

### Numbers

- What is the difference between `int` and `float`?
- What does `/` return?
- What does `//` do?
- What does `%` return?
- What does `**` do?
- Why does operator precedence matter?

### Variables and Conventions

- What is multiple assignment?
- What is a constant?
- Does Python enforce constants?
- Why are constants conventionally written in uppercase?
- Why are descriptive variable names important?

### Python Language

- What is a keyword?
- What is a built-in?
- What is the difference between a keyword and a built-in function?
- What is the purpose of comments?
- What is the Zen of Python?

---

## 39. Chapter Summary

Chapter 2 establishes the fundamental concepts required to begin writing Python programs.

The central model is:

```text
Names
  ↓
Values
  ↓
Expressions
  ↓
Operations
  ↓
Results
```

The most important concepts are:

1. A variable is a name associated with a value.
2. `=` performs assignment.
3. `==` performs equality comparison.
4. Variables can be reassigned.
5. Python variable names are case-sensitive.
6. Variable names should follow Python naming conventions and communicate meaning.
7. Strings represent sequences of text.
8. String methods such as `.title()`, `.upper()`, and `.lower()` return transformed strings.
9. `.strip()`, `.lstrip()`, and `.rstrip()` remove whitespace from specific positions.
10. `.removeprefix()` removes an exact prefix when present.
11. Strings are immutable.
12. A method reference and a method call are different concepts.
13. `()` is required to call a method.
14. `+` can concatenate strings.
15. f-strings allow values and expressions to be embedded in strings.
16. Escape sequences provide special characters such as new lines and tabs.
17. Integers and floating-point numbers are different numeric types.
18. Python provides arithmetic operators such as `+`, `-`, `*`, `/`, `//`, `%`, and `**`.
19. Operator precedence determines the order of evaluation.
20. Parentheses can explicitly control evaluation order.
21. Underscores can improve the readability of large numeric literals.
22. Multiple assignment allows several variables to be assigned in one statement.
23. Uppercase constants are a naming convention, not a Python-enforced restriction.
24. Comments should provide useful context and intent.
25. Python emphasizes readability, simplicity, and explicitness.

---

## 40. Chapter Status

**Completed**

Chapter 2 established the fundamental Python concepts required for working with variables, strings, numbers, expressions, operators, and basic output.

The next chapter introduces:

**Chapter 3 — Introducing Lists**