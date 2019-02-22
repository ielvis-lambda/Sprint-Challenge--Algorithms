# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

```
b)  sum = 0

    for i in range(n):
      i += 1
      for j in range(i + 1, n):
        j += 1
        for k in range(j + 1, n):
          k += 1
          for l in range(k + 1, 10 + k):
            l += 1
            sum += 1
```

```
c)  def bunnieEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an _n_-story building and plenty of eggs. Suppose also
that an egg gets broken if it is thrown off floor _f_ or higher, and doesn't get
broken if dropped off a floor less than floor _f_. Devise a strategy to
determine the value of _f_ such that the number of dropped eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode and give the
runtime complexity of your solution.

If I have an _n_ -story building then I'm assuming that I have an ordered list of stories that the building is from 0 to _n_. 

To do this I would implement a recursive binary search function with a runtime of n log n. Since our floors get split into halves each time our runtime increases as a logarithm rather than linearly or exponentially because we are able to split our data in half each time. 

PsuedoCode: 

Function - FindEggBreak is going to take in the array of floors numbers. 

I would have a helper function called DidItBreak which would be the person physically dropping the egg fron floor _f_ and reporting if it broke or not. 

I would initialize this function to return f = undefined if n = 0 since there is no height to drop the egg from. 

Then I would pass the array into a binary search algorithm that would split the room list in half and check if the egg broke at each halfway mark working it's way down until it finds the lowest room # that it could break. 

Example: Pass in a 20 story building where the egg breaks after 8 stories. 

Function will split into two array from 1 to 10 and 11 to 20. 

It would check floor 15 by passing it to the helper function DidItBreak and return true which would eliminate floors 15-20. 

Then it would check our lower half-middle which would be 5 and false eliminating 0 to 5. 

So now we narrowed it down to the possibilities of floor 6 to 15 where the egg breaks having only broken 2 eggs. This would repeat until we get to  our solution of _f_ = 8. 