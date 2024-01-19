# Sorting

Like any other programming languages python is also having its inbuilt sorting function.
There are 2 methods:

1. sort():

   - Works only for list container
   - sort in place, can be asc / desc / custom

2. sorted():

   - Works for any kind of iterable containers(inbuilt and custom).

     - inbuilt like - list, tuple, string, dict, set

   - Since some of the containers are immutable. As a result the sorted() doesn't modify the passed container instead sorts and returns a brand new.

- Both the sorting uses TIM SORT (combination of merge and insertion sort internally) and both are stable (i.e. if 2 items are having same value then the original order is retained.

  - In worst case TIM SORT takes O(nlogn)
