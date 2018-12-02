General Note about List and Pointers
============
This note includes all thoughts about List and Pointers

## Shallow and deep copy in Python

If you use "=" to copy a variable A to variable B,
B only get a reference to the memory location which stores the values of A. So if you change B, you change the values in that location which leads to the change of A.

If you assign a new value to A, a new memory location will be assigned to A, that won't change B.

So, when there are value exchange in solutions, remember to think about the order.
