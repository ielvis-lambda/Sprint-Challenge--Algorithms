Add your answers to the Algorithms exercises here.

1a. 

This looks like constant runtime where `a` is always 0. 

Let's try a negative `n`. A negative number cubed is always going to be negative. which means that it will never be greater than `a` which is 0 so the while statement will never activate for a negative number. 

If n is 0, then 0 is not going to be greater than 0 so the while loop again won't activate. 

Finally if n is a positive number then after 1 iteration of the while loop the function will stop because n^3 is always less than n^2 so you'll get a = n^2 as the result every time regardless of input size for a positive number and a = 0 for n = 0 or negative number. This is why this function's time complexity is constant: O(1).

2b.

