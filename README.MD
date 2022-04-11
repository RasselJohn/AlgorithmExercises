*Algorithm's Exercises*
=================

Algorithm's exercises on Python with doctests.

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

- **10.py** - `n` natural numbers (`where 1 ≤ n ≤ 10^4 and every number ≤ 10`) are given.
Algorithm must print increasing sequence.

- **11.py** -
    Script must read text data and print `n` max numbers from it.
    But script has to perform extra conditions:
     • number is any digits sequence;  
     • number can include max **1000** digits;  
     • script should get only 1 param - `n`;  
     • it must have tests;  
     • **text data(file) may be very big (before 40Gb!).**

- **12.py** -
Script must check string with brackets on correctness.
There are 3 different ways(functions) for checking.
If string is correct - function returns 'Success'
else position(start from = 1(!)) with symbol which breaks sequence.
Examples:

```
Input         =>   Output
"({([])})"    =>   'Success'
"()[]}"       =>       5
"[]([]"       =>       3
"{*}"         =>   'Success'
```

- **13.py**
2 int numbers 'n','m' are given.
If anyone divides to another - print '1' otherwise '0'.
Attention! Conditions and loops ('if', 'while') are banned!

- **14.py**
Collection of commands are given (correct sequence of commands are guaranteed).
Function adds/removes int numbers in stack and control max value with access O(1).
Type of commands:
'push <num>' - add to stack,
'pop' - remove from stack,
'max' - just print max.
