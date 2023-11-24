# List

A list is a collection of items which internally uses array data structure.

There are other container types to store items like - tuples, sets, dictionary. Depending on the purpose we use different containters.

1. Advantages:

   - List speciality is RANDOM ACCESS, dynamic size i.e. appending elements the size will grow itself.
   - cache friendlyness i.e. locality of reference

2. Disadvantages:
   - Insertion / deletion are slow
   - search is also slow for unsorted list

# Some Important Functions

## General purpose functions

1. max(list):
   Will get the max element from the list

2. min(list):
   Will get the min element from the list

3. sum(list):
   Will get the sum of all elements of the list. Will work only for numeric types.

4. list.reverse():
   returns the reversed list

5. list.sort():
   modifies the order of list, default is asc

6. sorted(list):
   sorts and returns a new list

7. list.reverse():
   modifies the same list in the reverse fashion.

8. reversed(list):
   similar to the sorted function this function returns a new reversed list.

- the max, min, sum, sort will only work if all the element types are same

## Insertion and Presence

1. append(e):
   It will append the element to the end of list.

2. insert(location, e):
   Elements will be shifted the new elememnt will be inserted there.

3. in:
   This operator in python tells us in python whether the element/item is present in the collection or not.
   We can use for other collections as well.

4. count(e):
   Returns the count of occurences of an elemnent in the list.

5. index(e, start_index_inclusive, end_index_exclusive):
   It will return the first occurence index of element. If not present then will raise error. So need to be careful while callinng.

## Removal

1. remove(e):
   Wil remove the element and return the nee list. Mindful of using it as it may throw value error if not present.

2. pop(index):
   Index is optional if not passed it removes the last element from the list. It returns the popped item.

3. del l[index] / del l[start_index_incl:end_index_exc]:
   We can use the del keyword for deleting the element from the collection using the index.
   This keyword can also be used for other collections as well.

## Slicing (list, tuple, string)

1. list[start_inclusive, stop_exclusive, step]:

   - Slicing is a technique in Python used to extract a portion of a list (or other iterable) by specifying a start index, an end index, and an optional step.
   - It returns the new list
   - List slicing returns a list, tuple slicing returns tuple, string returns string
   - start, stop optional, default will take start and end index
   - step is also optional, default will take 1
   - We can step as negative values, in those cases the start should be greater than stop
   - l = [1, 2, 3, 4, 5] print(l[0:5:2]) // [1, 3, 5]
   - l = [1, 2, 3, 4, 5] print(l[-1:-6:-1]) // [5,4,3,2,1]
   - We have shortcut for above i.e. l[::-1] // will get reverse of list

   - Note:
   - If we are trying to return the same exact input after slicing,
     - list -> it will return new list
     - tuple -> it will return same
     - string -> it will also return same
     - Example: t1 = (1,2,3) t2 = (t1[::-1]) print(t1 is t2)

List slicing in Python is a technique used to extract a portion of a list, creating a new list containing the specified elements. It involves specifying a range of indices using the colon (`:`) operator. The syntax for list slicing is as follows:

```python
new_list = original_list[start:stop:step]
```

- `start`: The index from which the slicing begins. If omitted, it defaults to the start of the list.
- `stop`: The index at which the slicing stops. The element at this index is not included. If omitted, it defaults to the end of the list.
- `step`: The step or increment between indices. If omitted, it defaults to 1.

Here are some examples to illustrate list slicing:

```python
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Extract elements from index 2 to 5 (exclusive)
sliced_list = original_list[2:5]
# Result: [3, 4, 5]

# Extract elements from the beginning to index 3 (exclusive)
first_part = original_list[:3]
# Result: [1, 2, 3]

# Extract elements from index 5 to the end
second_part = original_list[5:]
# Result: [6, 7, 8, 9]

# Extract every second element starting from index 1
every_second = original_list[1::2]
# Result: [2, 4, 6, 8]

# Reverse the list using slicing
reversed_list = original_list[::-1]
# Result: [9, 8, 7, 6, 5, 4, 3, 2, 1]
```

List slicing is a powerful and flexible feature in Python, allowing you to easily manipulate and create new lists based on existing ones.

Yes, list slicing can be used on the left-hand side (LHS) of an expression to modify or replace elements within a list. When used on the LHS, the sliced portion of the list is replaced with the elements specified on the right-hand side (RHS) of the assignment.

Here's an example:

```python
original_list = [1, 2, 3, 4, 5]

# Replace elements from index 1 to 3 with new values
original_list[1:4] = [10, 20, 30]

print(original_list)
# Output: [1, 10, 20, 30, 5]
```

In this example, the elements from index 1 to 3 in `original_list` are replaced with the values `[10, 20, 30]`. The list slicing on the LHS allows you to target a specific portion of the list and update it with new values.

List slicing on the LHS is a convenient way to modify elements in a specific range within a list without creating an entirely new list.

## Comprehension in python

- Its a shortcut syntax to create a iterable from another iterable.
- an iterable is an object capable of returning its elements one at a time. It provides a way to iterate over a sequence of values, and many built-in objects in Python are iterable like (list, set, dict, tuples, string, range, files).
- We can select some or all items from the iterables and create a new iterable.

- Example:

```
    l1 = [x for x in range(10) if x%2==0] # comprehension example

    # Alternate code
    res = [];
    for x in range(10):
        if x % 2 == 0:
            res.append(x)
    print(res)
    # So the Comprehension tech is lesse line of code


    l = [1, 2, 3, 4]
    l1 = [x*2 for x in l] # list comprehension
    s1 = {x for x in l if x%2 == 0} # set comprehension
    d1 = {x: x*2 for x in l} # dic comprehension
    d2 = {x: f"ID{x}" for x in l} # dic comprehension
```

## Iterables vs Iterators

In Python, the terms "iterable" and "iterator" refer to distinct concepts, although they are closely related:

1. **Iterable:**

   - An iterable is any object capable of returning its elements one at a time.
   - It can be looped over using constructs like `for` loops, list comprehensions, and other iterable-related operations.
   - Examples of iterables include lists, tuples, strings, sets, dictionaries (when iterating over keys), ranges, files when used in a loop, and more.

2. **Iterator:**
   - An iterator is an object representing a stream of data, and it is responsible for producing the next value in the sequence.
   - Iterators implement the `__iter__()` and `__next__()` methods.
   - The `__iter__()` method returns the iterator object itself, and the `__next__()` method returns the next value in the sequence. When there are no more elements, it raises the `StopIteration` exception.
   - Iterators maintain an internal state, remembering the current position in the sequence.
   - Examples of iterators include instances of classes that implement the iterator protocol, such as the result of `iter(iterable)`.

Here's an example illustrating the difference:

```python
# Iterable
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# Iterator
my_iterable = iter(my_list)
print(next(my_iterable))  # Output: 1
print(next(my_iterable))  # Output: 2
```

In this example, `my_list` is an iterable, and the `for` loop automatically creates an iterator from it. The `iter()` function can also be used explicitly to obtain an iterator. The `next()` function is used to retrieve the next element from the iterator.

In summary, all iterators are iterables, but not all iterables are iterators. Iterables provide a way to get an iterator, and iterators are responsible for producing the next value in a sequence.
