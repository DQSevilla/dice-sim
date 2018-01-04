# dice-sim

An experiment for simulating an n-sided die (a D-n) with only coin flips.

## Overall Goals:
- Given n, an arbitrary number of sides of a die, we want a program that:
  - Simulates one or more rolls of the die by repeatedly flipping one coin
  - Returns the minimum expected number of coin flips required to simulate a single roll of the die

This is an exercise and experiment in finding a lower and upper bound on the expected value of the number of coin flips it takes to sufficiently simulate a roll of a die.

## Methods of simulating a D-n with coin flips:
> Formal proofs for the 1/n probabilities and expected number of flips are not written here, intuitions are.

### Trivial cases:
- A D-1 always takes a value of 1 with any roll, with 0 expected flips, and rolling a D-2 is just a coin flip, `1 := H, 2 := T`

### The general algorithm:
- This is a general method which maps a valid sequence of successive coin flips to a roll.

- __Procedure__: Flip a coin up to n times, keeping track of each flip in a sequence. If after any flip you have encountered more than one heads _and_ more than one tails, restart the procedure. After the nth flip, if every flip in the current sequence was the same face, restart. Otherwise, the number flip that has a different face than all the others is the number you rolled. 
  - e.g. Both `[H, T, H]` and `[T, H, T]` represent rolling a 2 with a D-3.
  - e.g. Getting the overall sequence `[H, T, H, T, T, T, T, H, T]` indicates that you rolled a 4 with a D-5.
    - The first four flips are an invalid sequence, unlike the next five. Think of it as `[H, T, H, T], [T, T, T, H, T]`.

- __Why it works__: Can be proven correct by observing how the sample space for the overall sequence of flips is transformed when invalid sequences are removed, and valid complementary sequences (switch heads and tails) are combined. To convince yourself, look at the D-3 case.

- __Efficiency__: This algorithm is not very efficient as it's expected number of flips is __2<sup>n-1</sup>__.

### The obvious simulation of a D-2<sup>k</sup>:
- Clearly if you wish to simulate a n = 2<sup>k</sup> sided die, k &isin; __&#8469;__, you can simply use successive coin flips to split the working sample space in half each time. I call this _binary splitting_.

- __Procedure__: Flip a coin. If it is heads, consider a D-(n/2) numbered `1, ..., n/2`, else consider one numbered `n/2 + 1, ..., n`. Repeat the procedure for the new die until it becomes A D-1. The number associated with it is the result of the overall roll.
  - e.g. `[H, H, T]` represents rolling a 2 with a D-8.
    - Space of numbers are transformed: `[1, ..., 8] -> [1, 2, 3, 4] -> [1, 2] -> [2]`.

- __Why it works__: It is easy to see that each roll has a 1/n = 1/2<sup>k</sup> probability, as each of the n numbers maps to exactly one of n sequences of flips.

- __Efficiency__: This is the most efficient way to simulate a D-2<sup>k</sup>, with exactly __log<sub>2</sub>n = k__ flips.

### Simulating any D-n with a D-2<sup>k</sup>:
- It would be nice if we could use the previous method for a general D-n, and in fact we can.

- __Procedure__: Using the above method, simulate a D-2<sup>k</sup>, where 2<sup>k</sup> is the smallest power of two that is greater than n. If the result of the roll is greater than n, restart the simulation. Otherwise, that number is the result of the roll.
  - e.g. To simulate a D-30 we try simulating a D-32. All results of that roll are valid and applied to our D-30 result except for `[T, T, T, T, H]` and `[T, T, T, T, T]` (31 and 32 respectively).

- __Why it works__: By "throwing out" invalid rolls we limit the sample space to exactly that of our D-n. While it may seem that, for example, rolling a 31 when simulating a D-31 with a D-32 is less likely than any other roll, it is not. Think of the probabilities as a long run average. Over "time" the probability of any given roll is exactly 1/31.

- __Efficiency__: The exact expected number of flips depends on how far removed the number in question is from the next highest power of two. In general it is __&Omega;(log n)__ flips. Note that this method alone is the most efficient way to simulate a D-n if n is prime.

### Splitting:
- The above method is the best we have seen so far but we can do even better. Well, for most numbers that is. Splitting is the generalized form of our second method of simulating a D-2<sup>k</sup>. However, splitting by itself only works if it is _binary splitting_, with n = 2<sup>k</sup>. Otherwise, it must be used in conjunction with a different simulation method, the most efficient being the previous one. As you will see, splitting does _not_ work if n is prime.

- __Procedure__: Simulate a D-i using any of the above methods, where i is the smallest factor of n such that i > 1. Now split the D-n into i dice, each with n/i sides, and choose the die corresponding to the number rolled with the D-i (rolling a 1 corresponds to `1, ..., n/i`, a 2 corresponds to `n/i + 1, ..., 2n/i`, etc until n). Keep splitting until the number of sides of the current die is prime, which you can simulate using the previously discussed methods.
  - e.g. To simulate a D-30, flip a coin. If heads, simulate a standard D-15, else, simulate a D-15 numbered 16 through 30. To simulate the D-15, either simulate a D-16, or, simulate a D-3, and with that result, choose between the three possible D-5s, numbered either `1, ..., 5`, `6, ..., 10`, or `11, ..., 15`. Finally, since 5 is prime, simulate it using a previous method.

- __Why it works__: The language used in the procedure might sound a bit confusing but it's quite simple. If there is a smallest number that evenly divides n other than 1, then we can split our D-n into one of several possible dice, just like we did when splitting by two. Probabilities are preserved because each die split into is equally likely to be chosen, and the rest of the method relies on previously discussed ones, which we have also shown to achieve 1/n probabilities.

- __Efficiency__: This is an open issue. We only know that it is always more efficient to split in half than to simulate by the next highest power of two beforehand. But for odd sided die, we haven't yet figured out whether splitting into factors is more efficient than simply simulating by the next power. Again the efficiency is approximately __&Omega;(log n)__, but it is generally more efficient than the above method.

## Further results:

### Simulating any D-k with any other D-n:

One immediately interesting result of these methods is that because we can "throw out" values in our rolls (flip sequences) to simulate a smaller die, we can do the same with regular die. If we have a D-k, we can simulate a coin flip by considering a D-k', where k' = k if even, or k' = k-1 if k is odd. Then, if our roll is within the first half of the values, we flipped a heads, else, we flipped a tails. And because we know coin flips can simulate a D-n, we can simulate a D-n with any D-k, for all positive integers n and k. Simulating a D-n with a D-k may also have interesting, more efficient methods than this simple binary choice approach. Additionally, this may give more insight into general probability simulation given that a variable is uniformly random.
