*Algorithm's Exercises*
=================

Algorithm's exercises on Python with doctests. Some tasks were taken from the LeetCode.

- **01.py** - Get prime numbers in interval.

- **02.py** - Get sequences with numbers and operators ('+' or '-'), where result equals the certain sum.

- **03.py** - Check number on primary.

- **04.py** - Convert greek number to arabic number.

- **05.py** - Reverse 2 variables without third.

- **06.py** - Convert string to **Haffman's** code through tree.

- **07.py** - Convert **Haffman's** code to string.

- **08.py** - Realizing of **max-heap**.

- **09.py** - Given:
    - integer number `n (where 1 ≤ n ≤ 10^5)`;
    - array `A[1…n] (where 1 ≤ A[i] ≤ 10^9`);
    - integer number `k (where 1 ≤ k ≤ 10^5)`;
    - array `B[1…k](where 1 ≤ B[j] ≤ 10^9)`.  
      For each item in `B` there should print an index `i( where 1 ≤ i ≤ n)` for `A[i]=B[j]`, else to print `-1`
      if this item does not exist.

          Sample Input:
          5 1 5 8 12 13
          5 8 1 23 1 11
          
          Sample Output:
          3 1 -1 1 -1

- **10.py** - `n` natural numbers (`where 1 ≤ n ≤ 10^4 and every number ≤ 10`) are given. Algorithm must print
  increasing sequence.

- **11.py** - Script must read text data and print `n` max numbers from it. Script has to perform extra conditions:
  • number is any digits sequence;  
  • number can include max **1000** digits;  
  • script should get only 1 param - `n`;  
  • it must have tests;  
  • **text data(file) may be very big (before 40Gb!).**

- **12.py** - Script must check string with brackets on correctness. There are 3 different ways(functions) for checking.
  If string is correct - function returns 'Success' else position(start from = 1(!)) with symbol which breaks sequence.
  Examples:

```
Input         =>   Output
"({([])})"    =>   'Success'
"()[]}"       =>       5
"[]([]"       =>       3
"{*}"         =>   'Success'
```

- **13.py** - Two int numbers ('n','m') are given. If anyone divides to another - print '1' otherwise '0'. Attention!
  Conditions and loops ('if', 'while') are banned!

- **14.py** - Collection of commands are given (correct sequence of commands are guaranteed). Function adds/removes int
  numbers in stack and control max value with access O(1). Type of commands:
  'push <num>' - add to stack,
  'pop' - remove from stack,
  'max' - just print max.

- **15.py** - By the number 'n' (1≤n≤10^9) find max number 'k', which allows to set 'n' like a sum of 'k' different(!)
  summands. Function must return array of summands(where len(summands)==k).

- **16.py** - Given an array of integers nums and an integer target, return indices of the two numbers such that they
  add up to target.

- **17.py** - Given an integer x, return true if x is a palindrome, and false otherwise without(!) converting the
  integer to a string.

- **18.py** - Given two strings s and t, return true if t is an anagram of s, and false otherwise.

- **19.py** - Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
  non-zero elements.

- **20.py** - Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal,
  otherwise, return false.

- **21.py** - An array is monotonic if it is either monotone increasing or monotone decreasing. An array nums is
  monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j,
  nums[i] >= nums[j]. Given an integer array nums, return true if the given array is monotonic, or false otherwise.

- **22.py** - You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
  reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a LINKED
  LIST(!). You may assume the two numbers do not contain any leading zero, except the number 0 itself.

- **23.py** - Given a string `s`, find the length of the longest substring without repeating characters.