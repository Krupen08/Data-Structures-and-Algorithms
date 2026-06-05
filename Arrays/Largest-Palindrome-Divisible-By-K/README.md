# Largest Palindrome Divisible by K

## Problem Statement

Given:

* `n` = number of digits
* `k` = divisor

Find the largest `n`-digit palindrome that is divisible by `k`.

A palindrome is a number that reads the same forwards and backwards.

---

## Example

### Input

```python
n = 3
k = 5
```

### Output

```python
595
```

### Explanation

* `595` is a palindrome.
* `595` is divisible by `5`.
* There is no larger 3-digit palindrome divisible by `5`.

---

## Approach

1. Start from the largest `n`-digit number.
2. Traverse downwards until the smallest `n`-digit number.
3. Check if the current number is a palindrome.
4. If it is a palindrome and divisible by `k`, return it immediately.
5. Since we are iterating from largest to smallest, the first valid number found is the answer.

---

## Solution

```python
class Solution(object):

    def isPalindrome(self, x):
        temp = x
        rev = 0

        while temp != 0:
            d = temp % 10
            rev = rev * 10 + d
            temp = temp // 10

        return rev == x

    def check(self, n, k):

        for i in range(10**n - 1, 10**(n - 1) - 1, -1):

            if self.isPalindrome(i):

                if i % k == 0:
                    return i
```

---

## Complexity Analysis

### Time Complexity

```text
O(10^n × n)
```

For each `n`-digit number, we perform a palindrome check that takes up to `n` digit operations.

### Space Complexity

```text
O(1)
```

Only a few extra variables are used regardless of input size.

