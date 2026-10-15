# Chapter 3 — Introducing Lists

## 1. Overview

Chapter 3 introduces **lists**, one of Python's fundamental data structures.

A list allows multiple values to be stored together in a single variable while preserving their order.

The chapter focuses on:

- Creating lists
- Accessing elements
- Understanding indexes
- Using individual values from a list
- Modifying elements
- Adding elements with `.append()` and `.insert()`
- Removing elements with `del`, `.pop()`, and `.remove()`
- Organizing lists
- Sorting lists permanently with `.sort()`
- Sorting lists temporarily with `sorted()`
- Reversing lists with `.reverse()`
- Finding the length of a list with `len()`
- Avoiding index errors

The objective is to understand how Python lists store ordered collections of values and how to access, modify, add, remove, and organize their elements.

---

## 2. Learning Objectives

After completing this chapter, I should be able to:

- Explain what a list is.
- Create a list using square brackets.
- Explain what an element is.
- Access individual elements using indexes.
- Explain why Python indexes start at `0`.
- Use positive and negative indexes.
- Access the last element using `-1`.
- Use values retrieved from a list.
- Apply string methods to string elements stored in a list.
- Explain why lists are mutable.
- Modify existing list elements.
- Add elements using `.append()`.
- Build a list dynamically using `.append()`.
- Insert elements at specific positions using `.insert()`.
- Remove elements using `del`.
- Remove and retrieve elements using `.pop()`.
- Remove elements by value using `.remove()`.
- Explain the difference between `del`, `.pop()`, and `.remove()`.
- Sort a list permanently using `.sort()`.
- Display a list in sorted order using `sorted()`.
- Explain the difference between `.sort()` and `sorted()`.
- Sort in reverse order using `reverse=True`.
- Reverse the current order of a list using `.reverse()`.
- Determine the number of elements using `len()`.
- Understand the relationship between list length and indexes.
- Recognize and debug `IndexError`.

---

## 3. What Is a List?

A **list** is an ordered collection of items.

Lists are created using square brackets `[]`, with individual elements separated by commas.

Example:

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]
```

Conceptually:

```text
bicycles
    ↓
["trek", "cannondale", "redline", "specialized"]
```

Each value stored inside the list is called an **element**.

In this example:

```text
"trek"
"cannondale"
"redline"
"specialized"
```

are the elements of the `bicycles` list.

A list therefore allows several related values to be grouped under a single variable name.

---

## 4. Printing a List

A complete list can be passed directly to `print()`.

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles)
```

Output:

```text
['trek', 'cannondale', 'redline', 'specialized']
```

Python displays the representation of the list, including:

- Square brackets
- Commas
- Quotation marks around strings

When working with individual values, it is often more useful to access specific elements instead of printing the entire list.

---

## 5. Accessing Elements in a List

Individual elements are accessed using their **index**.

Example:

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles[0])
```

Output:

```text
trek
```

The general syntax is:

```python
list_name[index]
```

Conceptually:

```text
Index:        0           1          2             3
              ↓           ↓          ↓             ↓
Value:      "trek"  "cannondale"  "redline"  "specialized"
```

Therefore:

```python
bicycles[0]
```

returns:

```text
trek
```

while:

```python
bicycles[2]
```

returns:

```text
redline
```

The index identifies the position of an element inside the list.

---

## 6. Index Positions Start at `0`

Python uses **zero-based indexing**.

This means that the first element is stored at index `0`, not index `1`.

Consider:

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]
```

The relationship between indexes and elements is:

```text
Index:        0           1          2             3
              ↓           ↓          ↓             ↓
Element:    "trek"  "cannondale"  "redline"  "specialized"
```

Therefore:

```python
bicycles[0]
```

means:

> Access the first element.

While:

```python
bicycles[1]
```

means:

> Access the second element.

A common mistake is to assume that index `1` represents the first element.

---

## 7. Using String Methods with List Elements

When an element retrieved from a list is a string, it can be used like any other string.

Example:

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles[0].title())
```

Output:

```text
Trek
```

Python first evaluates:

```python
bicycles[0]
```

which produces:

```text
"trek"
```

Then:

```python
.title()
```

is called on that string.

Conceptually:

```text
bicycles[0]
     ↓
   "trek"
     ↓
  .title()
     ↓
   "Trek"
```

This demonstrates that an element accessed from a list can be used in expressions and operations just like a value stored in an individual variable.

---

## 8. Negative Indexing

Python also allows elements to be accessed starting from the end of a list.

The index:

```text
-1
```

represents the last element.

Example:

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]

print(bicycles[-1])
```

Output:

```text
specialized
```

Similarly:

```python
bicycles[-2]
```

returns:

```text
redline
```

and:

```python
bicycles[-3]
```

returns:

```text
cannondale
```

The same list can therefore be viewed using positive and negative indexes:

```text
Positive:      0           1          2             3
               ↓           ↓          ↓             ↓
            "trek"  "cannondale"  "redline"  "specialized"
               ↑           ↑          ↑             ↑
Negative:     -4          -3         -2            -1
```

Positive indexes count from the beginning.

Negative indexes count backward from the end.

---

## 9. Using Individual Values from a List

Values accessed from a list can be used in expressions.

Example:

```python
bicycles = ["trek", "cannondale", "redline", "specialized"]

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
```

Output:

```text
My first bicycle was a Trek.
```

This combines several concepts:

```text
List
  ↓
Index
  ↓
Element
  ↓
String method
  ↓
f-string
  ↓
Output
```

The expression:

```python
bicycles[0].title()
```

is evaluated first, and its result is inserted into the f-string.

---

## 10. Lists Are Mutable

Lists can be changed after they are created.

This means that lists are **mutable**.

For example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]
```

can later be modified.

This creates an important distinction from strings:

```text
String
   ↓
Immutable

List
   ↓
Mutable
```

A list can therefore have its elements:

- Modified
- Added
- Removed
- Reorganized

---

## 11. Modifying Elements

An existing element can be replaced by assigning a new value to its index.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles[0] = "ducati"
```

Before:

```text
["honda", "yamaha", "suzuki"]
    ↑
  index 0
```

After:

```text
["ducati", "yamaha", "suzuki"]
```

The general syntax is:

```python
list_name[index] = new_value
```

This operation does not create an additional element.

It replaces the value currently stored at that position.

---

## 12. Adding Elements with `.append()`

The `.append()` method adds an element to the **end** of a list.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.append("ducati")
```

The list becomes:

```text
["honda", "yamaha", "suzuki", "ducati"]
```

The general syntax is:

```python
list_name.append(value)
```

Conceptually:

```text
["honda", "yamaha", "suzuki"]
                  ↓
          append("ducati")
                  ↓
["honda", "yamaha", "suzuki", "ducati"]
```

---

## 13. Building a List with `.append()`

`.append()` can be used to build a list gradually.

Start with an empty list:

```python
motorcycles = []
```

Then add elements:

```python
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
```

The final list is:

```text
["honda", "yamaha", "suzuki"]
```

Conceptually:

```text
[]
 ↓ append("honda")

["honda"]
 ↓ append("yamaha")

["honda", "yamaha"]
 ↓ append("suzuki")

["honda", "yamaha", "suzuki"]
```

This allows a list to grow as new values become available.

---

## 14. Inserting Elements with `.insert()`

The `.insert()` method adds an element at a specific position.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]

motorcycles.insert(0, "ducati")
```

The list becomes:

```text
["ducati", "honda", "yamaha", "suzuki"]
```

The syntax is:

```python
list_name.insert(index, value)
```

Existing elements are shifted to make space for the new element.

Conceptually:

```text
Before:

["honda", "yamaha", "suzuki"]
    ↑
  index 0

Insert "ducati" at index 0
              ↓

After:

["ducati", "honda", "yamaha", "suzuki"]
```

---

## 15. Removing Elements with `del`

If the index of an element is known, the `del` statement can remove it.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]

del motorcycles[0]
```

The list becomes:

```text
["yamaha", "suzuki"]
```

The general syntax is:

```python
del list_name[index]
```

`del` is useful when:

- The position of the element is known.
- The removed value does not need to be used afterward.

---

## 16. Removing Elements with `.pop()`

The `.pop()` method removes an element from a list and **returns the removed value**.

Without an index, `.pop()` removes the last element.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]

popped_motorcycle = motorcycles.pop()
```

After this operation:

```python
print(motorcycles)
```

produces:

```text
['honda', 'yamaha']
```

while:

```python
print(popped_motorcycle)
```

produces:

```text
suzuki
```

Conceptually:

```text
["honda", "yamaha", "suzuki"]
                       ↓
                     pop()
                       ↓
                   "suzuki"
```

The element is removed from the list, but the returned value can still be used.

---

## 17. Popping Elements from Any Position

An index can be passed to `.pop()`.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]

first_owned = motorcycles.pop(0)

print(first_owned)
```

Output:

```text
honda
```

The list becomes:

```text
["yamaha", "suzuki"]
```

Therefore:

```python
motorcycles.pop()
```

removes and returns the last element.

While:

```python
motorcycles.pop(index)
```

removes and returns the element at the specified index.

---

## 18. `del` vs `.pop()`

Both can remove an element using its position, but they have different purposes.

### `del`

```python
del motorcycles[0]
```

removes the element.

### `.pop()`

```python
removed_motorcycle = motorcycles.pop(0)
```

removes the element **and returns its value**.

A useful mental model is:

```text
Do I need the removed value?
           │
      ┌────┴────┐
      │         │
     No        Yes
      │         │
     del      .pop()
```

Use `del` when the value only needs to be removed.

Use `.pop()` when the removed value still needs to be used.

---

## 19. Removing an Element by Value with `.remove()`

Sometimes the position of an element is unknown, but its value is known.

The `.remove()` method removes an element based on its value.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]

motorcycles.remove("ducati")
```

The list becomes:

```text
["honda", "yamaha", "suzuki"]
```

The general syntax is:

```python
list_name.remove(value)
```

Unlike `del` and `.pop()`, `.remove()` does not require the index.

---

## 20. Using a Variable with `.remove()`

The value that will be removed can first be stored in a variable.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]

too_expensive = "ducati"

motorcycles.remove(too_expensive)

print(f"\nA {too_expensive.title()} is too expensive for me.")
```

The value stored in `too_expensive` remains available even though the matching element has been removed from the list.

### Important

`.remove()` removes only the **first occurrence** of the specified value.

If the same value appears more than once, only the first matching element is removed.

---

## 21. Comparing Ways to Remove Elements

The three removal techniques solve different problems.

| Operation | Uses | Removed value available? |
|---|---|---|
| `del list[index]` | Index | No |
| `list.pop()` | Index / last element | Yes |
| `list.remove(value)` | Value | Value can already be known/stored |

A useful decision model is:

```text
What do I know / need?
        │
        ├── Know index + don't need removed value
        │        ↓
        │       del
        │
        ├── Know index + need removed value
        │        ↓
        │      .pop()
        │
        └── Know the value
                 ↓
             .remove()
```

---

## 22. Sorting a List Permanently with `.sort()`

The `.sort()` method changes the order of the original list.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]

cars.sort()

print(cars)
```

Output:

```text
['audi', 'bmw', 'subaru', 'toyota']
```

Conceptually:

```text
Original:

["bmw", "audi", "toyota", "subaru"]
                 ↓
               .sort()
                 ↓
["audi", "bmw", "subaru", "toyota"]
```

The original list itself has been reordered.

---

## 23. Sorting in Reverse Order

`.sort()` can also organize a list in reverse order.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]

cars.sort(reverse=True)

print(cars)
```

Output:

```text
['toyota', 'subaru', 'bmw', 'audi']
```

The argument:

```python
reverse=True
```

causes the sorting order to be reversed.

The original list is still modified.

---

## 24. Temporarily Sorting with `sorted()`

Sometimes a list should be displayed in sorted order without changing its original order.

Python provides the `sorted()` function for this purpose.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
```

The sorted representation is:

```text
['audi', 'bmw', 'subaru', 'toyota']
```

but the original list remains:

```text
['bmw', 'audi', 'toyota', 'subaru']
```

Therefore:

```text
.sort()
   ↓
Changes the original list

sorted()
   ↓
Returns a sorted result
without changing the original list
```

This is one of the most important distinctions in the chapter.

---

## 25. Using `sorted()` in Reverse Order

`sorted()` also accepts:

```python
reverse=True
```

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]

print(sorted(cars, reverse=True))
```

The list is displayed in reverse sorted order without changing the original list.

Therefore:

```python
cars.sort(reverse=True)
```

changes `cars`.

While:

```python
sorted(cars, reverse=True)
```

does not change `cars`.

---

## 26. Reversing a List with `.reverse()`

The `.reverse()` method reverses the **current order** of a list.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]

cars.reverse()

print(cars)
```

Output:

```text
['subaru', 'toyota', 'audi', 'bmw']
```

An important distinction is:

```text
sort
  ↓
Arrange according to sorting rules

reverse
  ↓
Reverse the existing sequence
```

`.reverse()` does not perform alphabetical sorting.

It simply reverses the current order of the elements.

For example:

```text
Before:

A → B → C → D

After .reverse():

D → C → B → A
```

---

## 27. `.sort(reverse=True)` vs `.reverse()`

These operations can sometimes appear to produce similar results, but they perform different operations.

### `.sort(reverse=True)`

```python
cars.sort(reverse=True)
```

means:

> Sort the elements according to the sorting rules in reverse order.

### `.reverse()`

```python
cars.reverse()
```

means:

> Reverse whatever order the elements currently have.

Therefore:

```text
.sort(reverse=True)
        ↓
SORT + reverse sorting direction

.reverse()
        ↓
REVERSE current sequence
```

They should not be treated as equivalent operations.

---

## 28. Finding the Length of a List with `len()`

The `len()` function returns the number of elements in a list.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]

print(len(cars))
```

Output:

```text
4
```

Conceptually:

```text
["bmw", "audi", "toyota", "subaru"]
   1       2        3         4

Number of elements = 4
```

`len()` returns the **number of elements**, not the final index.

---

## 29. List Length vs Last Index

Because Python indexes start at `0`, the length of a list and its final positive index are different.

Example:

```python
cars = ["bmw", "audi", "toyota", "subaru"]
```

The list contains:

```text
4 elements
```

but its indexes are:

```text
0
1
2
3
```

Therefore:

```text
Length = 4

Last positive index = 3
```

For a non-empty list:

```text
last positive index = len(list) - 1
```

This distinction is important when avoiding index errors.

---

## 30. Index Errors

Trying to access an index that does not exist causes an `IndexError`.

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles[3])
```

The valid indexes are:

```text
0
1
2
```

There is no element at index `3`.

Python therefore raises an error similar to:

```text
IndexError: list index out of range
```

Conceptually:

```text
["honda", "yamaha", "suzuki"]
    0         1         2

Index 3
   ↓
Does not exist
   ↓
IndexError
```

---

## 31. Using `-1` for the Last Element

Instead of calculating the last positive index, Python allows the last element to be accessed using:

```python
-1
```

Example:

```python
motorcycles = ["honda", "yamaha", "suzuki"]

print(motorcycles[-1])
```

Output:

```text
suzuki
```

This is often more convenient than calculating:

```python
motorcycles[len(motorcycles) - 1]
```

However, negative indexing does not solve the problem of an empty list.

Example:

```python
motorcycles = []

print(motorcycles[-1])
```

This still causes:

```text
IndexError: list index out of range
```

because the list contains no elements.

---

## 32. Important Conceptual Distinctions

### List vs Element

```python
cars = ["bmw", "audi", "toyota"]
```

Here:

```text
cars
 ↓
Entire list

"bmw"
 ↓
Individual element
```

---

### Index vs Element

Consider:

```python
cars[1]
```

Here:

```text
1
↓
Index

"audi"
↓
Element stored at that index
```

The index identifies the position.

The element is the value stored at that position.

---

### Positive vs Negative Indexing

Positive indexing counts from the beginning:

```text
  0         1         2
  ↓         ↓         ↓
"bmw"     "audi"   "toyota"
```

Negative indexing counts from the end:

```text
 -3        -2        -1
  ↓         ↓         ↓
"bmw"     "audi"   "toyota"
```

---

### Modify vs Append vs Insert

Modify:

```python
cars[0] = "mercedes"
```

means:

> Replace an existing element.

Append:

```python
cars.append("honda")
```

means:

> Add an element to the end.

Insert:

```python
cars.insert(0, "honda")
```

means:

> Add an element at a specified position.

Conceptually:

```text
Modify
   ↓
Replace

.append()
   ↓
Add to end

.insert()
   ↓
Add at position
```

---

### `del` vs `.pop()` vs `.remove()`

```text
del
 ↓
Remove using INDEX

.pop()
 ↓
Remove using INDEX
+
return removed value

.remove()
 ↓
Remove using VALUE
```

---

### `.sort()` vs `sorted()`

```text
.sort()
   ↓
Original list changes

sorted()
   ↓
Original list remains unchanged
```

---

### `.sort(reverse=True)` vs `.reverse()`

```text
.sort(reverse=True)
        ↓
Sort in reverse order

.reverse()
        ↓
Reverse current order
```

These are different operations.

---

### Length vs Index

```text
List:

["bmw", "audi", "toyota"]

Number of elements:
3

Indexes:
0, 1, 2
```

Therefore:

```text
length ≠ last index
```

---

## 33. Common Mistakes

### Mistake 1 — Assuming Indexing Starts at `1`

Given:

```python
cars = ["bmw", "audi", "toyota"]
```

This:

```python
cars[1]
```

returns:

```text
audi
```

not:

```text
bmw
```

The first element is:

```python
cars[0]
```

---

### Mistake 2 — Accessing an Index That Does Not Exist

Given:

```python
cars = ["bmw", "audi", "toyota"]
```

this is invalid:

```python
cars[3]
```

because the valid indexes are:

```text
0
1
2
```

---

### Mistake 3 — Confusing Index and Value

This:

```python
del cars[0]
```

removes using an **index**.

This:

```python
cars.remove("bmw")
```

removes using a **value**.

They solve different problems.

---

### Mistake 4 — Using `del` When the Removed Value Is Needed

This:

```python
del cars[0]
```

removes the element without returning it.

If the removed value is needed:

```python
removed_car = cars.pop(0)
```

is more appropriate.

---

### Mistake 5 — Assuming `.pop()` Only Removes the Last Element

Without an argument:

```python
cars.pop()
```

removes the last element.

But an index can also be supplied:

```python
cars.pop(0)
```

which removes the first element.

---

### Mistake 6 — Assuming `.remove()` Uses an Index

Incorrect mental model:

```python
cars.remove(0)
```

when the intention is to remove the element at index `0`.

`.remove()` works with a **value**.

For example:

```python
cars.remove("bmw")
```

---

### Mistake 7 — Assuming `sorted()` Changes the Original List

```python
cars = ["bmw", "audi", "toyota"]

sorted(cars)
```

does not permanently change `cars`.

To permanently sort the list:

```python
cars.sort()
```

---

### Mistake 8 — Confusing Sorting with Reversing

```python
cars.reverse()
```

does not mean:

> Sort the list in descending order.

It means:

> Reverse the current order of the elements.

---

### Mistake 9 — Confusing Length with Last Index

Given:

```python
cars = ["bmw", "audi", "toyota"]
```

the length is:

```text
3
```

but the final index is:

```text
2
```

because indexing begins at `0`.

---

## 34. Debugging Example

Consider:

```python
cars = ["bmw", "audi", "toyota"]

print(cars[3])

cars.remove(0)

sorted(cars)

print(cars)
```

There are several concepts to examine.

### Problem 1 — Invalid Index

```python
print(cars[3])
```

The list contains three elements, so the valid indexes are:

```text
0
1
2
```

Correct examples:

```python
print(cars[2])
```

or, for the last element:

```python
print(cars[-1])
```

---

### Problem 2 — `.remove()` Uses a Value

```python
cars.remove(0)
```

attempts to remove the value `0`.

If the intention is to remove the element at index `0`, use:

```python
del cars[0]
```

or:

```python
cars.pop(0)
```

depending on whether the removed value is needed.

---

### Problem 3 — `sorted()` Does Not Modify the Original List

```python
sorted(cars)
```

produces a sorted result, but that result is not being used.

To permanently change the list:

```python
cars.sort()
```

Or use the returned sorted value directly:

```python
print(sorted(cars))
```

---

## 35. Micro-Challenge: List Operations

Consider:

```python
cars = ["bmw", "audi", "toyota"]
```

### A

```python
cars.append("honda")
print(cars)
```

Result:

```text
['bmw', 'audi', 'toyota', 'honda']
```

The new element is added to the end.

### B

```python
cars.insert(0, "honda")
print(cars)
```

Result:

```text
['honda', 'bmw', 'audi', 'toyota']
```

The new element is inserted at index `0`.

### C

```python
car = cars.pop()
print(car)
print(cars)
```

The final element is removed and stored in `car`.

### D

```python
cars.sort()
print(cars)
```

The original list is permanently sorted.

### E

```python
print(sorted(cars))
print(cars)
```

The first line displays the list in sorted order.

The second confirms that the original list remains in its previous order.

---

## 36. Practical Examples

### Creating a List

```python
names = ["ada", "grace", "alan"]
```

### Accessing an Element

```python
print(names[0])
```

### Accessing the Last Element

```python
print(names[-1])
```

### Using an Element

```python
message = f"Hello, {names[0].title()}!"

print(message)
```

### Modifying an Element

```python
names[0] = "guido"
```

### Appending an Element

```python
names.append("linus")
```

### Inserting an Element

```python
names.insert(0, "dennis")
```

### Removing with `del`

```python
del names[0]
```

### Removing with `.pop()`

```python
removed_name = names.pop()
```

### Popping a Specific Position

```python
removed_name = names.pop(0)
```

### Removing by Value

```python
names.remove("ada")
```

### Permanent Sorting

```python
names.sort()
```

### Temporary Sorting

```python
print(sorted(names))
```

### Reverse Sorting

```python
names.sort(reverse=True)
```

### Reversing the Current Order

```python
names.reverse()
```

### Finding the Length

```python
print(len(names))
```

---

## 37. Practice Exercises

### Exercise 1 — Names

Create a list containing several people's names.

Print each person's name individually by accessing the appropriate index.

---

### Exercise 2 — Greetings

Using the previous list, print a personalized message for each person.

Example:

```python
names = ["ada", "grace", "alan"]

message = f"Hello, {names[0].title()}!"

print(message)
```

---

### Exercise 3 — Your Own List

Create a list containing examples of a type of transportation you would like to own.

Use individual elements from the list to print statements about them.

---

### Exercise 4 — Guest List

Create a list containing people you would invite to dinner.

Use each person's name to print an invitation.

---

### Exercise 5 — Changing Guest List

Suppose one guest cannot attend.

Modify the list by replacing that guest with another person.

Print a new invitation for each person.

---

### Exercise 6 — More Guests

Add additional guests to the list.

Use:

```python
.insert()
```

to add guests at different positions.

Use:

```python
.append()
```

to add another guest at the end.

Print new invitations.

---

### Exercise 7 — Shrinking Guest List

Suppose only a limited number of people can attend.

Use:

```python
.pop()
```

to remove guests one at a time.

For each removed guest, print a message explaining that they can no longer be invited.

Print messages for the guests who remain.

Finally, use:

```python
del
```

to remove the remaining elements when appropriate.

---

### Exercise 8 — Seeing the World

Create a list containing places you would like to visit.

Practice using:

```python
sorted()
```

```python
sorted(list_name, reverse=True)
```

```python
.reverse()
```

```python
.sort()
```

```python
.sort(reverse=True)
```

Observe which operations change the original list and which do not.

---

### Exercise 9 — Dinner Guests

Use:

```python
len()
```

to determine how many people are currently in the guest list.

---

### Exercise 10 — Every Function

Create a list containing any type of values relevant to the exercise.

Practice the operations introduced in this chapter:

```python
list_name[index]
```

```python
list_name[index] = value
```

```python
.append()
```

```python
.insert()
```

```python
del
```

```python
.pop()
```

```python
.remove()
```

```python
.sort()
```

```python
sorted()
```

```python
.reverse()
```

```python
len()
```

The objective is to understand when and why each operation is used.

---

## 38. Knowledge Check

Before considering the chapter understood, I should be able to answer these questions without looking at the notes.

### Lists

- What is a list?
- What is an element?
- How is a list created?
- Why is a list considered ordered?
- What does it mean for a list to be mutable?
- How is a list different from a string regarding mutability?

### Indexing

- What is an index?
- Why does the first element have index `0`?
- How do I access the first element?
- How do I access the second element?
- What does index `-1` represent?
- What does index `-2` represent?
- What is the difference between positive and negative indexing?
- What is the relationship between the length of a list and its last positive index?

### Modifying Lists

- How do I replace an existing element?
- Does assigning a value to an existing index add a new element or replace one?
- What does `.append()` do?
- How can `.append()` be used to build a list?
- What does `.insert()` do?
- What information does `.insert()` require?
- What happens to existing elements when another element is inserted?

### Removing Elements

- What does `del` do?
- When should `del` be used?
- What does `.pop()` do?
- What does `.pop()` remove when no index is provided?
- What does `.pop(0)` do?
- What is the difference between `del` and `.pop()`?
- What does `.remove()` do?
- Does `.remove()` use an index or a value?
- What is the difference between `.pop()` and `.remove()`?
- What happens when `.remove()` is used when a value appears more than once?

### Organizing Lists

- What does `.sort()` do?
- Does `.sort()` modify the original list?
- What does `sorted()` do?
- Does `sorted()` modify the original list?
- What is the difference between `.sort()` and `sorted()`?
- What does `reverse=True` do?
- What does `.reverse()` do?
- What is the difference between `.sort(reverse=True)` and `.reverse()`?

### Length and Errors

- What does `len()` return?
- Why does a list containing three elements have a last positive index of `2`?
- What causes an `IndexError`?
- What does `list_name[-1]` normally return?
- Why does `[-1]` fail on an empty list?

---

## 39. Chapter Summary

Chapter 3 introduces lists and the fundamental operations required to work with ordered collections of values.

The central model is:

```text
List
  ↓
Elements
  ↓
Indexes
  ↓
Access
  ↓
Modify
  ↓
Add / Remove
  ↓
Organize
```

The most important concepts are:

1. A list is an ordered collection of elements.
2. Lists are created using square brackets `[]`.
3. Individual values inside a list are called elements.
4. Elements are accessed using indexes.
5. Python indexing starts at `0`.
6. Positive indexes count from the beginning of a list.
7. Negative indexes count backward from the end.
8. `-1` represents the last element.
9. Elements retrieved from a list can be used in expressions and method calls.
10. Lists are mutable.
11. Assigning a new value to an existing index modifies that element.
12. `.append()` adds an element to the end of a list.
13. `.append()` can be used to build a list gradually.
14. `.insert()` adds an element at a specified position.
15. `del` removes an element using its index.
16. `.pop()` removes an element and returns its value.
17. `.pop()` without an index removes the last element.
18. `.pop(index)` removes an element from a specified position.
19. `.remove()` removes an element using its value.
20. `.remove()` removes only the first matching occurrence.
21. `del`, `.pop()`, and `.remove()` solve different removal problems.
22. `.sort()` permanently changes the order of a list.
23. `sorted()` produces a sorted result without changing the original list.
24. `reverse=True` reverses the sorting direction.
25. `.reverse()` reverses the current order of the list.
26. `.reverse()` and `.sort(reverse=True)` are different operations.
27. `len()` returns the number of elements in a list.
28. List length and the final positive index are different because indexing starts at `0`.
29. Accessing an index that does not exist produces an `IndexError`.
30. Negative indexing cannot retrieve an element from an empty list.

A useful quick-reference model is:

```text
CREATE
  ↓
[]

ACCESS
  ↓
list[index]
list[-1]

MODIFY
  ↓
list[index] = value

ADD
  ↓
.append(value)
.insert(index, value)

REMOVE
  ↓
del list[index]
.pop(index)
.remove(value)

ORGANIZE
  ↓
.sort()
sorted()
.reverse()

SIZE
  ↓
len()
```

---

## 40. Chapter Status

**Completed**

Chapter 3 established the fundamental concepts required for creating, accessing, modifying, extending, reducing, and organizing Python lists.

The next chapter introduces:

**Chapter 4 — Working with Lists**